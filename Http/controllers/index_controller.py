from bs4 import BeautifulSoup


class IndexController(object):

    def __init__(self, response, link):
        self._html = BeautifulSoup(response, link)

    @property
    def html(self):
        return self._html

    @html.setter
    def html(self, html):
        self._html = html

    def fill_files_in_index(self, file, type_file):
        if type_file == 0:
            table = self.html.find(id="books")
            row = self.html.new_tag("tr")

            column = self.html.new_tag("th")
            column.append(file['course'])
            row.append(column)

            column = self.html.new_tag("td")
            column.append(file['assigned'])
            row.append(column)

            column = self.html.new_tag("td")
            column.append(file['title'])
            row.append(column)

            column = self.html.new_tag("td")
            column.append("R$" + file['price'])
            row.append(column)

            table.append(row)
        else:
            table = self.html.find(id="exames")
            row = self.html.new_tag("tr")

            column = self.html.new_tag("th")
            column.append(file['course'])
            row.append(column)

            column = self.html.new_tag("td")
            column.append(file['assigned'])
            row.append(column)

            column = self.html.new_tag("td")
            column.append(file['title'])
            row.append(column)

            column = self.html.new_tag("td")
            column.append("R$" + file['price'])
            row.append(column)

            table.append(row)

