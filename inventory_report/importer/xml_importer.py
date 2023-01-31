from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(path):
        try:
            with open(path) as file:
                return list(xmltodict.parse(file.read())['dataset']['record'])
        except Exception:
            raise ValueError("Arquivo inválido")
