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
        return self._request

    @request.setter
    def request(self, request):
        self._request = request

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
                mime_type = mimetypes.guess_type('anyway.json')[0]
            elif self.route.attr['function'] == 'delete':
                mime_type = mimetypes.guess_type('anyway.json')[0]
            elif self.route.attr['function'] == 'create':
                mime_type = mimetypes.guess_type('anyway.json')[0]
            elif self.route.attr['function'] == 'update':
                mime_type = mimetypes.guess_type('anyway.json')[0]
            else:
                mime_type = mimetypes.guess_type(self.route.attr['path'])[0]

            headers += 'Content-Type: ' + str(mime_type) + '\r\n\r\n'
        except Exception as e:
            headers = 'HTTP/1.1 404 Not Found\r\n\r\n'
            self._body(f"Error 404: File not found\r\n{e}\r\n")

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
            elif self.route.attr['function'] == 'edit':
                id_file = self.route.attr['params'][0]
                file_json = open('repository/sql.json', 'rb')
                body = self.edit(id_file, file_json.read())
                file_json.close()
            elif self.route.attr['function'] == 'create':
                body = self.create(json.loads(self.request.params), 'repository/sql.json')
            elif self.route.attr['function'] == 'delete':
                id_file = self.route.attr['params'][0]
                body = self.delete(id_file, 'repository/sql.json')
            elif self.route.attr['function'] == 'update':
                id_file = self.route.attr['params'][0]
                file_json = open('repository/sql.json', 'rb')
                body = self.update(id_file, file_json.read(), json.loads(self.request.params))
                file_json.close()
            else:
                file = open(self.route.attr['path'], 'rb')
                body = file.read()
                file.close()

        except Exception as e:
            return f"Error 404: File not found\r\n{e}\r\n".encode('utf-8')

        return body

    def update(self, id_file, file_json, data):
        response = {
            "data": "",
            "status": 500,
            "message": "File not found."
        }

        files = json.loads(file_json)
        new_files = []

        for file in files:
            if file['id'] == int(id_file):
                data = {
                    "id": file['id'],
                    "type": data['type'],
                    "assigned": data['assigned'],
                    "course": data['course'],
                    "title": data['title'],
                    "price": data['price']
                }
                print(data)
                new_files.append(data)
                response = {
                    "data": file,
                    "status": 200,
                    "message": "File found successfully."
                }
            else:
                new_files.append(file)

        self.write_json(new_files, 'repository/sql.json')

        return json.dumps(response).encode('utf-8')

    @staticmethod
    def edit(id_file, file_json):
        response = {
            "data": "",
            "status": 500,
            "message": "File not found."
        }
        files = json.loads(file_json)

        for file in files:
            if file['id'] == int(id_file):
                response = {
                    "data": file,
                    "status": 200,
                    "message": "File found successfully."
                }
                break

        return json.dumps(response).encode('utf-8')

    def delete(self, id_file, path_json):
        response = {
            "data": "",
            "status": 500,
            "message": "File not found."
        }

        file_json = open(path_json, 'rb')
        files = file_json.read()
        files = json.loads(files)
        file_json.close()

        new_files = []

        for file in files:
            if file['id'] == int(id_file):
                response = {
                    "data": file,
                    "status": 200,
                    "message": "Xerox deleted successfully."
                }
            else:
                new_files.append(file)

        self.write_json(new_files, path_json)

        return json.dumps(response).encode('utf-8')

    def create(self, data, path_json):
        response = {
            "data": "",
            "status": 200,
            "message": "File created successfully!"
        }

        file_json = open(path_json, 'rb')
        files = file_json.read()
        files = json.loads(files)
        file_json.close()

        data = {
            "id": files[-1]['id'] + 1,
            "type": data['type'],
            "assigned": data['assigned'],
            "course": data['course'],
            "title": data['title'],
            "price": data['price']
        }

        files.append(data)

        self.write_json(files, path_json)

        response['data'] = data

        return json.dumps(response).encode('utf-8')

    @staticmethod
    def write_json(list_json, path_json):
        with open(path_json, 'w') as f:
            f.write('[\n')
            for file in list_json:
                f.write('\t{\n')
                f.write('\t\t"id": %s,\n' % file['id'])
                f.write('\t\t"type": %s,\n' % file['type'])
                f.write('\t\t"assigned": "%s",\n' % file['assigned'])
                f.write('\t\t"course": "%s",\n' % file['course'])
                f.write('\t\t"title": "%s",\n' % file['title'])
                f.write('\t\t"price": "%s"\n' % file['price'])
                f.write('\t}\n') if file['id'] == list_json[-1]['id'] else f.write('\t},\n')
            f.write(']\n')
            f.close()

    @staticmethod
    def get_body_with_json(file_json, response):
        html = IndexController(response, 'html.parser')
        files = json.loads(file_json)

        for file in files:
            html.fill_files_in_index(file, file['type'])

        return html.html.encode('utf-8')

    def get_response(self):
        return self.headers.encode('utf-8') + self.body
