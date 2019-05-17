import socket
import threading
import threaded

HOST = socket.gethostbyname(socket.gethostname())
PORT = 4000

# "with" look like "try-finally"
# socket(ADDRESS_FAMILY, SOCKET_TYPE)
# ADRESS_FAMILY -> AF_NET (default):        IPV4
#               -> AF_INET6:                IPV6
# SOCKET_TYPE   -> SOCK_STREAM (default):   TCP  
#               -> SOCK_DGRAM:              UDP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp:
    # used for defining the communication end point (socket), associating the socket with a address
    # bind(ADDRESS_FAMILY(AF_NET), Port)
    # socket.gethostname() returns the hostname's machine

    print(f'Try to connect: {HOST}:{PORT}')

    tcp.bind((HOST, PORT))

    # define the number of pending connections the queue will hold
    # listen(BACKLOG)
    # socket.SOMAXCONN is the maximum backlog value that the "socket.listen" can allow by system
    tcp.listen(socket.SOMAXCONN)
    while True:
        # if input("Write 'exit' or 'quit' for close server...\n") == 'exit' or 'quit':
        #     print('\033[1;30;41m Good bye! \033[m')
        #     break

        # return a new socket representing the connection, and the address of the client
        (conn, addr) = tcp.accept()

        threading.Thread(target=threaded.Thread, args=(conn,)).start()
tcp.close()
