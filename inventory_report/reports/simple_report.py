from collections import Counter


class SimpleReport:
    def generate(products):
        oldest_manufacturing_date = min(
            product["data_de_fabricacao"] for product in products
        )
        closest_expiration_date = min(
            product["data_de_validade"] for product in products
        )
        company_with_most_products = Counter(
            product["nome_da_empresa"] for product in products
        ).most_common(1)[0][0]
        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_most_products}"
        )
