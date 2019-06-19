from Http import http_response, http_request
from Http.routes.web_routes import WebRoutes


class Thread(object):

    def __init__(self, conn):
        self.threading(conn)

    @staticmethod
    def threading(conn):
        with conn:
            # return a object w/ sent bytes by client
            # the value of bufsize should be a relatively small power of 2
            data = conn.recv(1024).decode('utf-8')

            route = WebRoutes(data)

            request = http_request.Request(data, route.method)

            response = http_response.Response(request, route)

            conn.sendall(response.get_response())
            conn.close()
