from sys import argv
import socket

BUFFER_SIZE = 1024

def main(arguments):
    host = argv[1]
    port = int(argv[2])
    message = "*" if len(argv) is not 4 or len(argv) is 3 else argv[3]

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print "Connection established: {}:{}".format(host, port)

    print "Sent: {}".format(message)
    s.send(message)
    # data = s.recv(BUFFER_SIZE) # echo
    s.close()
    print "Connection closed."
    # print "Received:", data # echo

if __name__ == "__main__":
    if len(argv) < 3 or len(argv) > 4 :
        print "python tcp_sender.py <host> <port> [message]"
        exit(1)
    else: main(argv)
