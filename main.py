import estoque
import Database.models as initdb
import schedule

if __name__ == '__main__':
    # Criando a database
    initdb.db.create_tables([initdb.Produto, initdb.Movimentacao])

    # Criando o objeto Estoque
    estoque = estoque.Estoque()

    # Carregando produtos
    estoque.carregar_produtos()

    # Cadastrando produtos
    estoque.adicionar_produto('Caneca', 'Compra', 50)
    estoque.adicionar_produto('Batedeira', 'Compra', 10)
    estoque.adicionar_produto('Prato', 'Compra', 30)
    estoque.carregar_produtos()
    print(estoque.consultar_estoque('Prato'))

    # Verificando se existe produtos com estoque baixo
    while True:
        schedule.run_pending()
