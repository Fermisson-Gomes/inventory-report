from typing import List, Dict


class SimpleReport:
    @staticmethod
    def generate(product_list: List[Dict]) -> str:
        now = datetime.datetime.now()

        manufacturing = [
            product["data_de_fabricacao"] for product in product_list
        ]

        expiration = [
            product["data_de_validade"] for product in product_list
            if product["data_de_validade"] > now.strftime("%Y-%m-%d")
        ]

        companies = [
            product["nome_da_empresa"] for product in product_list
        ]

        count_by_company = {
            f"{company}": companies.count(company)
            for company in companies
        }

        older_manufacturing = min(manufacturing)
        closest_expiration = max(expiration)
        most_products_company = max(
            count_by_company,
            key=count_by_company.get
        )

        return (
            f"Data de fabricação mais antiga: {older_manufacturing}\n"
            f"Data de validade mais próxima: {closest_expiration}\n"
            f"Empresa com mais produtos: {most_products_company}"
        )
