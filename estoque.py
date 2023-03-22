import db


def cadastrar_produto(nome, quantidade, preco):
    db.Produto.create(nome=nome, quantidade=quantidade, preco=preco)
    print('Produto cadastrado com sucesso')


def registrar_venda(id_produto, quantidade):
    produto = db.Produto.get(id=id_produto)
    if produto.quantidade >= quantidade:
        produto.quantidade -= quantidade
        produto.save()
        print('Pedido realizado com sucesso')
    else:
        print('Não há estoque suficiente para realizar o pedido')


def registrar_compra(id_produto, quantidade):
    produto = db.Produto.get(id=id_produto)
    produto.quantidade += quantidade
    produto.save()
    print('Compra registrada com sucesso')


def registrar_devolucao(id_produto, quantidade):
    produto = db.Produto.get(id=id_produto)
    produto.quantidade += quantidade
    produto.save()
    print('Devolução registrada com sucesso')


def ajustar_estoque(id_produto, quantidade):
    produto = db.Produto.get(id=id_produto)
    produto.quantidade = quantidade
    produto.save()
    print('Estoque ajustado com sucesso')
