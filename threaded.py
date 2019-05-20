from controllers.http import http_request, http_response


class Thread(object):

    def __init__(self, conn):
        self.threading(conn)

    @staticmethod
    def threading(conn):
        with conn:
            # return a object w/ sent bytes by client
            # the value of bufsize should be a relatively small power of 2
            data = conn.recv(1024).decode('utf-8')

            request = http_request.Request(data)

            response = http_response.Response(request)

            conn.sendall(response.get_response())
            conn.close()
