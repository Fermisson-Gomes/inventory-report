from collections import Counter
import datetime


class SimpleReport:
    @staticmethod
    def generate(products):
        my_date = datetime.datetime.now()
        oldest_creation_date = min(
            product["data_de_fabricacao"] for product in products
            )
        closest_expiration_date = min(
            product["data_de_validade"] for product in products
            if product["data_de_validade"] > my_date.strftime("%Y-%m-%d")
            )
        company_with_most_products = Counter(
            product["nome_da_empresa"] for product in products
            ).most_common()[0][0]
        return (
            f"Data de fabricação mais antiga: {oldest_creation_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_most_products}"
        )
