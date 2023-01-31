from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        id=1,
        nome_do_produto="Test product",
        nome_da_empresa="Test company",
        data_de_fabricacao="2020-10-20",
        data_de_validade="2021-10-20",
        numero_de_serie=12345,
        instrucoes_de_armazenamento="Instructions"
    )

    assert str(product.__repr__()) == f"O produto {product.nome_do_produto}\
 fabricado em {product.data_de_fabricacao} por\
 {product.nome_da_empresa} com validade até\
 {product.data_de_validade} precisa ser armazenado\
 {product.instrucoes_de_armazenamento}."
