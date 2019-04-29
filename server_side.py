import socket

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

    print('Try to connect: ' + HOST)

    tcp.bind((HOST, PORT))

    # define the number of pending connections the queue will hold
    # listen(BACKLOG)
    # socket.SOMAXCONN is the maximum backlog value that the "socket.listen" can allow by system
    tcp.listen(socket.SOMAXCONN)
    while True:
        # return a new socket representing the connection, and the address of the client
        (conn, addr) = tcp.accept()

        with conn:
            # return a object w/ sent bytes by client
            # the value of bufsize should be a relatively small power of 2
            data = conn.recv(2048).decode('utf-8')

            # Split to detect the methods and request
            stringSplit = data.split(' ')

            http_method = stringSplit[0]
            http_request = 'index.html' if stringSplit[1].lstrip('/') == '' else stringSplit[1].lstrip('/')

            try:
                file = open(http_request, 'rb')
                file_response = file.read()
                file.close()

                header_response = 'HTTP/1.1 200 OK\n'

                if(http_request.endswith(".html")):
                    mime_type = 'text/html'
                elif(http_request.endswith(".mp3")):
                    mime_type = 'audio/' + http_request.rpartition(".")[-1]
                elif(http_request.endswith(".js")):
                    mime_type = '​​​application/javascript'
                elif(http_request.endswith(".json")):
                    mime_type = '​​​application/json'
                elif(http_request.endswith(".css")):
                    mime_type = '​​​text/css'            
                else:
                    mime_type = 'image/' + http_request.rpartition(".")[-1]

                header_response += 'Content-Type: ' + str(mime_type) + '\n\n'

            except Exception as e:
                header = 'HTTP/1.1 404 Not Found\n\n'
                response = str('Error 404: File not found\n').encode('utf-8')

            response = header_response.encode('utf-8') + file_response

            conn.sendall(response)
            conn.close()
        
    tcp.close()
