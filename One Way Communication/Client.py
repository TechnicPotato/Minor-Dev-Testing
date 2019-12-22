import socket

# These can be shifted later to allow command line arguments.
# These are the statically defined IPs to connect to.
HOST = "10.0.0.44"
# Hopefully a free port, allow changes
PORT = 9001

def initial_setup(host, port, socket):
    """Attempts to connect to the server.
    
    Keyword arguments:
    host -- host to connect to.
    port -- port on the host to connect to.
    socket -- empty socket to pass in.

    """
    # Connect to the actual server.
    try:
        socket.connect((host, port))
    except Exception as e:
        print(e)

def send_msg(str, socket):
    """Sends a message on a socket"""
    if socket.sendall(str) != None:
        print("Message failed to send!")


# Defining the main loop
if __name__ == "__main__":
    # Begin an initial setup
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    initial_setup(host=HOST, port=PORT, socket=s)
    send_msg(b"test", socket=s)
    