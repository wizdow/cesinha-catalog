class Response:
    request = ''
    header = ''
    body = ''

    def __init__(self, request):
        self.request = request.request if request else 'index.html'
        self.get_header()
        self.get_body()

    def set_request(self, request):
        self.request = request

    def set_body(self, body):
        self.body = body

    def set_header(self, header):
        self.header = header

    def get_header(self):

        if self.header:
            return self.header

        try:
            header = 'HTTP/1.1 200 OK\n'

            if self.request.endswith(".html"):
                mime_type = 'text/html'
            elif self.request.endswith(".mp3"):
                mime_type = 'audio/' + self.request.rpartition(".")[-1]
            elif self.request.endswith(".js"):
                mime_type = '​​​application/javascript'
            elif self.request.endswith(".json"):
                mime_type = '​​​application/json'
            elif self.request.endswith(".css"):
                mime_type = '​​​text/css'
            else:
                mime_type = 'image/' + self.request.rpartition(".")[-1]

            header += 'Content-Type: ' + str(mime_type) + '\n\n'
            self.set_header(header)

        except Exception as e:
            self.set_header('HTTP/1.1 404 Not Found\n\n')
            self.set_body(str('Error 404: File not found\n').encode('utf-8'))

        return self.header

    def get_body(self):

        if self.body:
            return self.body

        try:
            file = open(self.request, 'rb')
            self.body = file.read()
            file.close()
        except Exception as e:
            self.set_body(str('Error 404: File not found\n').encode('utf-8'))

        return self.body

    def get_response(self):
        return self.header.encode('utf-8') + self.body
