from pathlib import Path
from scrapy.exporters import JsonItemExporter


class PerIDJSONExportPipeline(object):
    def open_spider(self, spider):
        Path(f'results/{spider.name}').mkdir(
            parents=True,
            exist_ok=True
        )

        self.exporters = {}


    def close_spider(self, spider):
        for exporter in self.exporters.values():
            exporter.finish_exporting()


    def _do_exporting(self, item, spider_name):
        id_ = item['id']
        if id_ not in self.exporters:
            file_path = f'results/{spider_name}/{id_}.json'
            file_handler = open(file_path, 'wb')

            exporter = JsonItemExporter(file_handler)
            exporter.start_exporting()

            self.exporters[id_] = exporter

        return self.exporters[id_]


    def process_item(self, item, spider):
        exporter = self._do_exporting(item, spider.name)
        exporter.export_item(item)

        return item
