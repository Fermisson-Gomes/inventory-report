from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        with open(path) as file:
            if "csv" in path:
                data = csv.DictReader(file, delimiter=",", quotechar='"')
            else:
                raise ValueError("Arquivo inválido")

            return list(data)
