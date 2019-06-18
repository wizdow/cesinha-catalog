class WebRoutes(object):
    ROUTES = {
        '/': 'GET',
        'index.html': 'GET',
        'fonts': {
            'icon.css': 'GET',
        },
        'css': {
            'index.css': 'GET',
            'materialize.min.css': 'GET',
        },
        'js': {
            'jquery-3.3.1.js': 'GET',
            'jquery.marquee.min.js': 'GET',
            'materialize.min.js': 'GET',
            'index.js': 'GET',
        },
        'audio': {
            'logoclick.mp3': 'GET'
        },
        'images': {
            'sidenav-background.jpg': 'GET',
            'favicon.ico': 'GET',
            'book-move.gif': 'GET',
        },
        'xerox': {
            'edit': {
                'id': True,
                'method': 'GET',
                'mime_type': '.html'
            },
            'create': {
                'id': False,
                'method': 'POST',
            },
            'delete': {
                'id': True,
                'method': 'DELETE',
            },
        }
    }

    def __init__(self, string):
        string = string.split(' ')

        self._path = 'index.html' if string[1].lstrip('/') == '' else string[1].lstrip('/')
        self._method = string[0]

        self._path = self._path.split('/')

        if self._path[0] != 'index.html' and self._path[0] != 'favicon.ico':
            self._controller = self._path[0]
            self._function = self._path[1]
            self._params = self._path[2:]
        else:
            self._controller = ''
            self._function = ''
            self._params = ''

        self._attr = {
            'path': '/'.join(self._path),
            'controller': self._controller,
            'function': self._function,
            'params': self._params
        }

        self.verify_path()

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, method):
        self._method = method

    @property
    def attr(self):
        return self._attr

    @attr.setter
    def attr(self, attr):
        self._attr = attr

    def verify_path(self):
        try:
            if self._path == 'index.html':
                print(f"{self._path} loaded with success!")
            elif self.ROUTES[self._controller]:
                if self.ROUTES[self._controller][self._function]:
                    if self.ROUTES[self._controller][self._function] == 'GET':
                        print(f"{self._path} loaded with success!")
                    else:
                        if self.ROUTES[self._controller][self._function]['method'] == self._method:
                            print(f"{self._path} loaded with success!")
                        else:
                            print(f"For {self._path} Method {self._method} not allowed!")
                else:
                    print(f"Method not allowed in {self._controller}")
            else:
                print("Route not allowed!")

        except Exception as e:
            print(f"{e}: File {self._path} not found")
