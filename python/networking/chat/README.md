# Async chat example

The chat example builds a small multi-user TCP chat room using Python's
`asyncio` library.  It is a richer demonstration than the basic TCP scripts
and includes niceties such as usernames, command handling, and immediate
message delivery.

## Files

- `chatserver.py` – Runs the asynchronous chat server.  It listens on port
  5000, keeps track of connected users, and broadcasts messages to everyone in
  the room.
- `chatclient.py` – Terminal-based chat client.  It connects to the server,
  prompts for a username, and displays incoming messages in real time.

## Usage

1. On the BeagleBone Green that will host the chat server, run:

   ```bash
   cd ~/BeagleBoneGreen/python/networking/chat
   python3 chatserver.py
   ```

2. On each client BeagleBone Green (or other computer on the LAN), update the
   `SERVER_HOST` constant in `chatclient.py` if needed, then run:

   ```bash
   cd ~/BeagleBoneGreen/python/networking/chat
   python3 chatclient.py
   ```

3. Follow the prompts to pick a username.  Type messages and press
   <kbd>Enter</kbd> to chat.  Use `/list` to view connected users and `/quit` to
   exit.

The scripts default to port `5000`, but you can change `PORT` in the server
and client to match your network requirements.
