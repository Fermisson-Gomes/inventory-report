from inventory_report.inventory.product import Product


def test_cria_produto():
    created_product = Product(
        1,
        "Nicotine Polacrilex",
        "Target Corporation",
        "2021-02-18",
        "2023-09-17",
        1551,
        "instrucao 1"
    )

    assert created_product.id == 1
    assert created_product.nome_do_produto == "Nicotine Polacrilex"
    assert created_product.nome_da_empresa == "Target Corporation"
    assert created_product.data_de_fabricacao == "2021-02-18"
    assert created_product.data_de_validade == "2023-09-17"
    assert created_product.numero_de_serie == 1551
    assert created_product.instrucoes_de_armazenamento == "instrucao 1"
