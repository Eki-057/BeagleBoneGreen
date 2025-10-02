# Basic TCP example

This pair of scripts demonstrates the absolute minimum needed for two
BeagleBone Green boards (or a BBG and a laptop) to communicate over TCP.
The server listens for an incoming connection, prints anything the client
sends, and echoes messages back to the sender.

## Files

- `server.py` – Listens on port 5000, greets the client, and echoes received
  messages.  Each connection is handled in a background thread so you can
  interact with multiple clients during a single run.
- `client.py` – Connects to the server, prints the greeting, and sends a
  sample message.

## Usage

1. Edit the `HOST` constant in `client.py` so it matches the server's IP
   address.  The default assumes the server is located at `10.0.0.100`.
2. On the server BeagleBone Green, run:

   ```bash
   cd ~/BeagleBoneGreen/python/networking/basic_tcp
   python3 server.py
   ```

   Leave this terminal open.
3. On the client BeagleBone Green (or another machine on the same network),
   run:

   ```bash
   cd ~/BeagleBoneGreen/python/networking/basic_tcp
   python3 client.py
   ```

   You should see the greeting message and the server should log the
   connection details.

Feel free to modify the scripts to send additional data or to integrate them
into other projects.
