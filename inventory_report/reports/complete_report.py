from inventory_report.reports.simple_report import SimpleReport


class CompleteReport:
    @classmethod
    def generate(self, list):
        simple_report = SimpleReport.generate(list)
        qty_by_company = self.count_products_by_company(list)
        return simple_report + qty_by_company

    @classmethod
    def count_products_by_company(self, products):
        count = {}
        for product in products:
            nome_da_empresa = product["nome_da_empresa"]
            if nome_da_empresa in count:
                count[nome_da_empresa] += 1
            else:
                count[nome_da_empresa] = 1

        return self.strf_qty(count.items())

    @staticmethod
    def strf_qty(qty):
        string = "\nProdutos estocados por empresa:\n"

        for company, product in qty:
            string += f"- {company}: {product}\n"

        return string
