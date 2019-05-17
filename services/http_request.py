class Request(object):

    def __init__(self, string):
        self._string = string
        self._params = []

        string.split('\r\n').pop(0)
        self._headers = self.headers_by_string(string)

        string = self.string.split(' ')

        self._route = 'index.html' if string[1].lstrip('/') == '' else string[1].lstrip('/')
        self._method = string[0]

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, params):
        self._params = params

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, string):
        self._string = string

    @property
    def route(self):
        return self._route

    @route.setter
    def route(self, route):
        self._route = route

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, method):
        self._method = method

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, headers):
        self._headers = headers

    @staticmethod
    def headers_by_string(request):
        headers = {"body": request[len(request) - 1]}

        for parameter in request:
            parameter = parameter.lower()
            if 'host: ' in parameter:
                headers["host"] = parameter.replace('host: ', '')
                break
            elif 'upgrade-insecure-requests: ' in parameter:
                headers["upgrade_insecure_requests"] = parameter.replace('upgrade-insecure-requests: ', '')
                break
            elif 'content-type: ' in parameter:
                headers["content_type"] = parameter.replace('content-type: ', '')
                break
            elif 'authority: ' in parameter:
                headers["authority"] = parameter.replace('authority: ', '')
                break
            elif 'connection: ' in parameter:
                headers["connection"] = parameter.replace('connection: ', '')
                break
            elif 'user-agent: ' in parameter:
                headers["user_agent"] = parameter.replace('user-agent: ', '')
                break
            elif 'accept: ' in parameter:
                headers["accept"] = parameter.replace('accept: ', '')
                break
            elif 'referer: ' in parameter:
                headers["referer"] = parameter.replace('referer: ', '')
                break
            elif 'origin: ' in parameter:
                headers["origin"] = parameter.replace('origin: ', '')
                break
            elif 'pragma: ' in parameter:
                headers["pragma"] = parameter.replace('pragma: ', '')
                break
            elif 'accept-encoding: ' in parameter:
                headers["accept_encoding"] = parameter.replace('accept-encoding: ', '')
                break
            elif 'accept-language: ' in parameter:
                headers["accept_language"] = parameter.replace('accept-language: ', '')
                break
            elif 'cookie: ' in parameter:
                headers["cookie"] = parameter.replace('cookie: ', '')
                break
            elif 'cache-control: ' in parameter:
                headers["cache_control"] = parameter.replace('cache-control: ', '')
                break
            else:
                continue

        return headers
