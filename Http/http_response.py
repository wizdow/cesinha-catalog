import json
import mimetypes
from Http.controllers.index_controller import IndexController


class Response(object):

    def __init__(self, request, route):
        self._request = request
        self._route = route
        self._headers = self.create_headers()
        self._body = self.create_body()

    @property
    def request(self):
        return self._route

    @request.setter
    def request(self, request):
        self._route = request

    @property
    def route(self):
        return self._route

    @route.setter
    def route(self, route):
        self._route = route

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, body):
        self._body = body.encode('utf-8')

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, headers):
        self._headers = headers

    def create_headers(self):

        if hasattr(self, '_headers'):
            return self.headers

        try:
            headers = 'HTTP/1.1 200 OK\r\n'

            if self.route.attr['function'] == 'edit':
                mime_type = mimetypes.guess_type('.html')[0]
            elif self.route.attr['function'] == 'delete':
                mime_type = mimetypes.guess_type('.html')[0]
            elif self.route.attr['function'] == 'create':
                mime_type = mimetypes.guess_type('.html')[0]
            else:
                mime_type = mimetypes.guess_type(self.route.attr['function'])[0]

            headers += 'Content-Type: ' + str(mime_type) + '\r\n\r\n'

        except Exception:
            headers = 'HTTP/1.1 404 Not Found\r\n\r\n'
            self._body('Error 404: File not found\r\n')

        return headers

    def create_body(self):

        if hasattr(self, '_body'):
            return self.body

        try:
            if self.route.attr['path'] == 'index.html':
                file_json = open('repository/sql.json', 'rb')
                html = open(self.route.attr['path'], 'rb')
                body = self.get_body_with_json(file_json.read(), html.read())
                file_json.close()
                html.close()
            else:
                file = open(self.route.attr['path'], 'rb')
                body = file.read()
                file.close()

        except Exception:
            return 'Error 404: File not found\r\n'.encode('utf-8')

        return body

    @staticmethod
    def get_body_with_json(file_json, response):

        html = IndexController(response, 'html.parser')
        files = json.loads(file_json)

        for file in files:
            html.fill_files_in_index(file, file['type'])

        return html.html.encode('utf-8')

    def get_response(self):
        return self.headers.encode('utf-8') + self.body
