import json


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
            if self.request == 'index.html':
                file_json = open('API_simulated.json', 'rb')
                html = open(self.request, 'rb')
                body = self.get_body_with_json(file_json.read(), html.read())
                file_json.close()
                html.close()
            else:
                file = open(self.request, 'rb')
                body = file.read()
                file.close()

            self.body = body
        except Exception as e:
            self.set_body(str('Error 404: File not found\n').encode('utf-8'))

        return self.body

    def get_body_with_json(self, file_json, html):
        body = """<tbody>\n"""
        classrooms = json.loads(file_json)
        html = html.decode()

        for classroom in classrooms:
            if classroom['isUsed']:
                body += f"""<tr>
                              <th scope="row">{classroom['name']}</th>
                              <td>{classroom['teacher']}</td>
                              <td>{classroom['class']}</td>
                            </tr>
                            """
            else:
                body += f"""<tr>
                              <th scope="row">{classroom['name']}</th>
                              <td> -- </td>
                              <td> -- </td>
                            </tr>
                            """
        body += "</tbody>"
        str_replace = """<tbody id="api_simulated">

                  </tbody>"""
        body = str(html).replace(str_replace, body)

        return body.encode('utf-8')

    def get_response(self):
        return self.header.encode('utf-8') + self.body
