import threading
import schedule
from Database.models import Produto, Movimentacao


class Estoque:
    def __init__(self):
        self.produtos = {}

    def carregar_produtos(self):
        for produto in Produto.select():
            self.produtos[produto.nome] = produto.quantidade

    def consultar_estoque(self, nome):
        return self.produtos.get(nome, 0)

    def adicionar_produto(self, nome, tipo, quantidade):
        produto = Produto.get_or_none(nome=nome)
        if produto is None:
            produto = Produto.create(nome=nome, quantidade=quantidade)
            self.produtos[nome] = quantidade
        else:
            produto.quantidade += quantidade
            produto.save()
            self.produtos[nome] += quantidade

        Movimentacao.create(produto=produto, tipo=tipo, quantidade=quantidade)

    def registrar_venda(self, nome, quantidade):
        with threading.Lock():
            estoque_atual = self.consultar_estoque(nome)
            if quantidade <= estoque_atual:
                self.adicionar_produto(nome, 'Venda', -quantidade)
                return True
            else:
                return False

    def registrar_compra(self, nome, quantidade):
        with threading.Lock():
            self.adicionar_produto(nome, 'Compra', quantidade)

    def registrar_devolucao(self, nome, quantidade):
        with threading.Lock():
            self.adicionar_produto(nome, 'Devolução', quantidade)

    def ajustar_estoque(self, nome, quantidade):
        with threading.Lock():
            self.adicionar_produto(nome, 'Ajuste', quantidade)

    def alerta_estoque_baixo(self, limite_minimo=5):
        alertas = []
        for nome, quantidade in self.produtos.items():
            if quantidade < limite_minimo:
                mensagem = f"Produto {nome} em estoque baixo: {quantidade} unidades."
                alertas.append(mensagem)
        return alertas

    # solução sugerida pelo ChatGPT
    schedule.every(1).hour.do(alerta_estoque_baixo)
