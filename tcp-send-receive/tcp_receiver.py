from sys import argv
import socket

BUFFER_SIZE = 20  # Normally 1024, but we want fast response

def main(host, port):
    port = int(argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    conn, addr = s.accept()
    print "Connection address: {}:{}".format(host, port)
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        print "Received: {}".format(data)
        # conn.send(data)  # echo
    conn.close()
    print "Connection closed."

if __name__ == "__main__":
    if len(argv) != 3:
        print "python tcp_receiver.py <host> <port>"
        exit(1)
    else: main(argv[1], argv[2])
