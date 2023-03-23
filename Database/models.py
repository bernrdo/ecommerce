from peewee import *

db = SqliteDatabase('estoque.db')


class Produto(Model):
    nome = CharField()
    quantidade = IntegerField()

    class Meta:
        database = db


class Movimentacao(Model):
    produto = ForeignKeyField(Produto, backref='movimentacoes')
    tipo = CharField()  # Venda, Compra, Devolução, Ajuste
    quantidade = IntegerField()

    class Meta:
        database = db
