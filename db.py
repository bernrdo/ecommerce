from peewee import *

db = SqliteDatabase('estoque.db')


class Produto(Model):
    id = AutoField()
    nome = CharField()
    quantidade = IntegerField()
    preco = FloatField()

    class Meta:
        database = db


db.create_tables([Produto])
