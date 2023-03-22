import db


def consultar_id(nome):
    produto = db.Produto.get(nome=nome)
    print(f'ID do produto: {produto.id}')


def consultar_estoque(id_produto):
    produto = db.Produto.get(id=id_produto)
    print(f'Produto: {produto.nome}\nQuantidade em estoque: {produto.quantidade}\nPreço: R$ {produto.preco}')
