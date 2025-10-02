#!/usr/bin/env python3
import asyncio
import sys
from socket import IPPROTO_TCP, TCP_NODELAY

HOST = ""     # all interfaces
PORT = 5000

# Global state
clients = {}  # writer -> username

async def broadcast(line: str):
    """Send a line to all clients (including sender)."""
    data = (line.rstrip("\n") + "\n").encode("utf-8", "ignore")
    dead = []
    for w in list(clients.keys()):
        try:
            w.write(data)
        except Exception:
            dead.append(w)
    # drain once to flush
    await asyncio.gather(*(w.drain() for w in clients.keys() if not w.is_closing()), return_exceptions=True)
    # cleanup dead
    for w in dead:
        clients.pop(w, None)
        try: w.close()
        except: pass

async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    # Lower latency for tiny messages
    try:
        sock = writer.get_extra_info("socket")
        if sock is not None:
            sock.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
    except Exception:
        pass

    peer = writer.get_extra_info("peername")
    # 1) Ask username
    writer.write(b"ENTER_USERNAME\n")
    await writer.drain()
    name_bytes = await reader.readline()
    if not name_bytes:
        writer.close(); await writer.wait_closed(); return
    username = name_bytes.decode("utf-8", "ignore").strip() or f"user_{peer[1]}"

    # ensure uniqueness
    existing = set(clients.values())
    base = username
    i = 2
    while username in existing:
        username = f"{base}{i}"; i += 1

    clients[writer] = username

    # Welcome + join notice
    writer.write(f"Welcome, {username}! Type /quit to exit. Use /list to see who is online.\n".encode())
    await writer.drain()
    await broadcast(f"*** {username} joined ***")
    print(f"[+] {username} connected from {peer}", flush=True)

    try:
        while True:
            line = await reader.readline()
            if not line:
                break
            msg = line.decode("utf-8", "ignore").strip()
            if not msg:
                continue

            # Commands
            if msg == "/quit":
                writer.write(b"Goodbye!\n"); await writer.drain()
                break
            if msg == "/list":
                names = ", ".join(sorted(clients.values()))
                writer.write(f"Online: {names}\n".encode()); await writer.drain()
                continue

            # Normal chat: echo to everyone immediately
            chat_line = f"{username}: {msg}"
            print(chat_line, flush=True)           # server console sees it live
            await broadcast(chat_line)

    except Exception:
        pass
    finally:
        # Cleanup
        uname = clients.pop(writer, None)
        try:
            writer.close()
            await writer.wait_closed()
        except:
            pass
        if uname:
            await broadcast(f"*** {uname} left ***")
            print(f"[-] {uname} disconnected", flush=True)

async def main():
    server = await asyncio.start_server(handle_client, HOST, PORT)
    # Lower latency on listener’s accepted sockets (best effort)
    try:
        sock = server.sockets[0]
        sock.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
    except Exception:
        pass

    addr = ", ".join(str(s.getsockname()) for s in server.sockets)
    print(f"Chat server listening on {addr}", flush=True)
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[server stopped]", flush=True)
