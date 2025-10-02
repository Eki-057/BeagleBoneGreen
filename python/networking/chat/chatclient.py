#!/usr/bin/env python3
 
import asyncio, sys
from socket import IPPROTO_TCP, TCP_NODELAY
 
SERVER_HOST = "10.3.20.101"   # <-- set to your server IP
SERVER_PORT = 5000
 
PROMPT = "> "
 
 
async def recv_task(reader: asyncio.StreamReader):
    """Continuously print server messages the instant they arrive."""
    try:
        while True:
            line = await reader.readline()
            if not line:
                print("\n[server closed]", flush=True)
                break
 
            # redraw-friendly print
            sys.stdout.write("\r")
            sys.stdout.flush()
            print(line.decode("utf-8", "ignore").rstrip("\n"), flush=True)
            sys.stdout.write(PROMPT)
            sys.stdout.flush()
    except Exception:
        pass
 
 
def format_message(msg: str) -> str:
    """
    Format a message for sending to the server.
    - @user message   → /msg user message
    - all: message    → /all message
    - /quit           → /quit
    - default         → /all message
    """
    if not msg:
        return ""
 
    if msg.startswith("@"):
        try:
            target, message = msg.split(" ", 1)
            target = target[1:]  # ta bort '@'
            return f"/msg {target} {message}"
        except ValueError:
            print("[usage] @username message")
            return ""
 
    elif msg.startswith("all:"):
        message = msg[4:].strip()
        return f"/all {message}"
 
    elif msg == "/quit":
        return "/quit"
 
    else:
        return f"/all {msg}"
 
 
async def input_task(writer: asyncio.StreamWriter):
    """Read user input and send immediately."""
    try:
        while True:
            msg = await asyncio.to_thread(input, PROMPT)
            formatted = format_message(msg)
 
            if not formatted:
                continue
 
            writer.write((formatted + "\n").encode("utf-8", "ignore"))
            await writer.drain()
 
            if formatted == "/quit":
                break
 
    except (EOFError, KeyboardInterrupt):
        try:
            writer.write(b"/quit\n")
            await writer.drain()
        except:
            pass
 
 
async def main():
    username = (await asyncio.to_thread(lambda: input("Choose a username: ").strip())) or "user"
 
    reader, writer = await asyncio.open_connection(SERVER_HOST, SERVER_PORT)
 
    # Lower latency
    try:
        sock = writer.get_extra_info("socket")
        if sock is not None:
            sock.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
    except Exception:
        pass
 
    # Expect ENTER_USERNAME and send our name
    banner = await reader.readline()
    if b"ENTER_USERNAME" not in banner:
        print("[unexpected server response]")
 
    writer.write((username + "\n").encode("utf-8", "ignore"))
    await writer.drain()
 
    print(f"Welcome, {username}! Type messages to chat. Use /quit to exit.", flush=True)
 
    # Run recv + input concurrently
    tasks = [
        asyncio.create_task(recv_task(reader)),
        asyncio.create_task(input_task(writer)),
    ]
 
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
 
    for t in pending:
        t.cancel()
 
    try:
        writer.close()
        await writer.wait_closed()
    except:
        pass
 
 
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[client stopped]", flush=True)
