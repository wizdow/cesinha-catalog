class WebRoutes(object):

    ROUTES = {
        '/': 'GET',
        'index.html': 'GET',
        'fonts/icon.css': 'GET',
        'css/index.css': 'GET',
        'css/materialize.min.css': 'GET',
        'images/book-move.gif': 'GET',
        'js/jquery-3.3.1.js': 'GET',
        'js/jquery.marquee.min.js': 'GET',
        'js/materialize.min.js': 'GET',
        'audio/logoclick.mp3': 'GET',
        'images/sidenav-background.jpg': 'GET',
        'images/favicon.ico': 'GET'
    }

    def __init__(self, string):
        string = string.split(' ')

        self._path = 'index.html' if string[1].lstrip('/') == '' else string[1].lstrip('/')
        self._method = string[0]

        self.verifyPath()

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, method):
        self._method = method

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    def verifyPath(self):
        try:
            if not self.ROUTES[self._path]:
                print('File not found.')
            elif self.ROUTES[self._path] != self._method:
                print('Method not allowed!')
            else:
                print(f"{self.path} loaded with success!")
        except Exception as e:
            print(f"{e}: File {self.path} not found")

