import json
import mimetypes
from bs4 import BeautifulSoup

class Response(object):

    def __init__(self, request):
        self._request = request.route if request else 'index.html'
        self._headers = self.create_headers()
        self._body = self.create_body()

    @property
    def request(self):
        return self._request

    @request.setter
    def request(self, request):
        self._request = request

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
            mime_type = mimetypes.guess_type(self.request)[0]

            headers += 'Content-Type: ' + str(mime_type) + '\r\n\r\n'

        except Exception as e:
            headers = 'HTTP/1.1 404 Not Found\r\n\r\n'
            self.body('Error 404: File not found\r\n')

        return headers

    def create_body(self):

        if hasattr(self, '_body'):
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

        except Exception as e:
            return 'Error 404: File not found\r\n'.encode('utf-8')

        return body

    @staticmethod
    def get_body_with_json(file_json, response):

        html = BeautifulSoup(response, 'html.parser')
        classrooms = json.loads(file_json)

        for classroom in classrooms:
            if classroom['isUsed']:
                table = html.find(id="books")
                row = html.new_tag("tr")

                column = html.new_tag("th", scope="row")
                column.append(classroom['name'])
                row.append(column)

                column = html.new_tag("td")
                column.append(classroom['teacher'])
                row.append(column)

                column = html.new_tag("td")
                column.append(classroom['class'])
                row.append(column)

                table.append(row)
            else:
                continue

        # body_free = """<tbody>\n"""
        # classrooms = json.loads(file_json)
        # html = html.decode()

        # for classroom in classrooms:
        #     if classroom['isUsed']:
        #         continue
        #     else:
        #         body_free += f"""<tr>
        #                       <th scope="row">{classroom['name']}</th>
        #                       <td> -- </td>
        #                       <td> -- </td>
        #                     </tr>
        #                     """
        # body_free += "</tbody>"
        # str_replace_free = '<!--                  <tbody id="api_simulated_free">-->'

        # body = str(html).replace(str_replace_free, body_free)

        return html.encode('utf-8')

    def get_response(self):
        return self.headers.encode('utf-8') + self.body
