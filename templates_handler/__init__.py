import os

from jinja2 import Environment, FileSystemLoader

import configs


class TemplateHandler(object):
    def __init__(self, template_name):
        super(TemplateHandler, self).__init__()

        self.name = template_name
        self._env = self._get_enviroment()


    def _get_enviroment(self):
        templates_folder_path = os.getenv('TEMPLATES_FOLDER_PATH')
        templates_folder_path = templates_folder_path.replace(
            '/',
            os.sep
        )

        loader = FileSystemLoader(templates_folder_path)
        return Environment(
            autoescape=True,
            loader=loader
        )


    def render(self, data):
        file_name = self.name + '.html.jinja'
        template = self._env.get_template(file_name)
        return template.render(data)
