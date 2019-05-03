import json
import mimetypes


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
            mime_type = mimetypes.guess_type(self.request)[0]

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
        body_not_free = """<tbody>\n"""
        body_free = """<tbody>\n"""
        classrooms = json.loads(file_json)
        html = html.decode()

        for classroom in classrooms:
            if classroom['isUsed']:
                body_not_free += f"""<tr>
                              <th scope="row">{classroom['name']}</th>
                              <td>{classroom['teacher']}</td>
                              <td>{classroom['class']}</td>
                            </tr>
                            """
            else:
                body_free += f"""<tr>
                              <th scope="row">{classroom['name']}</th>
                              <td> -- </td>
                              <td> -- </td>
                            </tr>
                            """
        body_not_free += "</tbody>"
        body_free += "</tbody>"
        str_replace_not_free = '<!--                  <tbody id="api_simulated_not_free">-->'
        str_replace_free = '<!--                  <tbody id="api_simulated_free">-->'

        html = str(html).replace(str_replace_not_free, body_not_free)
        body = str(html).replace(str_replace_free, body_free)

        return body.encode('utf-8')

    def get_response(self):
        return self.header.encode('utf-8') + self.body
