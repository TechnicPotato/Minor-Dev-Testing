import socket

# Globals
HOST = ''
PORT = 9001

# Main Thread
if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    # Threadlocks and waits for a connection
    s.listen()
    conn, addr = s.accept()
    print("Connected to: {client}".format(conn))
    while True:
        # Recieve 1024 bytes, can change parameters to allow more
        data = conn.recv(1024)
        # Cannot recieve any data.
        if data == 0:
            break
        data.decode("utf-8")
        print(data)
        conn.sendall(b"Message Recieved!")
    conn.close()
    