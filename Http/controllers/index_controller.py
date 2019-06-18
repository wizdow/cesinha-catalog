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

    def tag_i(self, class_tag):
        i = self.html.new_tag("i")
        i['class'] = class_tag
        i['aria-hidden'] = "true"

        return i

    def button(self, class_button, on_click, title):
        button = self.html.new_tag("a")
        button['on-click'] = on_click
        button['class'] = class_button
        button['title'] = title

        return button

    def fill_files_in_index(self, file, type_file):
        button_view = self.button("btn orange darken-3", f"edit({file['id']})", "Detalhes")
        button_delete = self.button("btn btn-danger", f"deleted({file['id']})", "Deletar")

        i_eye = self.tag_i("material-icons")
        i_eye.append("visibility")
        i_trash = self.tag_i("material-icons")
        i_trash.append("delete")

        button_view.append(i_eye)
        button_delete.append(i_trash)

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

            column = self.html.new_tag("td")
            column.append(button_view)
            column.append(button_delete)
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

            column = self.html.new_tag("td")
            column.append(button_view)
            column.append(button_delete)
            row.append(column)

            table.append(row)

