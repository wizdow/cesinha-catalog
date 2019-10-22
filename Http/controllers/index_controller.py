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
        button['onclick'] = on_click
        button['class'] = class_button
        button['title'] = title

        return button

    def fill_files_in_index(self, file, type_file):
        button_view = self.button("btn btn-danger", f"edit({file['id']})", "Detalhes")
        button_delete = self.button("btn orange darken-3", f"deleted({file['id']})", "Deletar")
        button_programmed = self.button("btn blue darken-3", f"programmedMaterial({file['id']})", "Agendar")
        button_print = self.button("btn yellow darken-3", f"print({file['id']})", "Imprimir")
        button_request = self.button("btn green darken-3", f"request({file['id']})", "Solicitar")

        i_eye = self.tag_i("material-icons")
        i_eye.append("visibility")
        i_trash = self.tag_i("material-icons")
        i_trash.append("delete")
        i_programmed = self.tag_i("material-icons")
        i_programmed.append("calendar_today")
        i_print = self.tag_i("material-icons")
        i_print.append("print")
        i_request = self.tag_i("material-icons")
        i_request.append("launch")

        button_view.append(i_eye)
        button_delete.append(i_trash)
        button_programmed.append(i_programmed)
        button_print.append(i_print)
        button_request.append(i_request)

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
            column.append(button_programmed)
            column.append(button_print)
            column.append(button_request)
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
            column.append(button_programmed)
            column.append(button_print)
            column.append(button_request)
            row.append(column)

            table.append(row)

