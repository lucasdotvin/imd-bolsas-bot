import os
from jinja2 import Template


class TemplateHandler(object):
    def __init__(self, template_name):
        super(TemplateHandler, self).__init__()

        self.name = template_name
        self._get_template_file_path()


    def _get_template_file_path(self):
        file_name = f'{self.name}.html.jinja'
        file_path = os.path.join('templates', file_name)

        self._file_path = file_path


    def render(self, data):
        with open(self._file_path, 'rb') as file_handler:
            file_content = file_handler.read()
            file_content = file_content.decode('utf-8')

        template = Template(file_content)
        return template.render(data)
