import threading
import produto


class Estoque:
    def __init__(self):
        self.produtos = {}
        self.lock = threading.Lock()

    def adicionar_produto(self, nome, quantidade):
        with self.lock:
            if nome in self.produtos:
                self.produtos[nome].quantidade += quantidade
            else:
                self.produtos[nome] = produto.Produto(nome, quantidade)

    def remover_produto(self, nome, quantidade):
        with self.lock:
            if nome in self.produtos and self.produtos[nome].quantidade >= quantidade:
                self.produtos[nome].quantidade -= quantidade
                return True
            else:
                return False

    def ajustar_estoque(self, nome, quantidade):
        with self.lock:
            if nome in self.produtos:
                self.produtos[nome].quantidade = quantidade

    def consultar_estoque(self, nome):
        with self.lock:
            if nome in self.produtos:
                return self.produtos[nome].quantidade
            else:
                return 0

    def alerta_estoque_baixo(self, nome):
        with self.lock:
            if nome in self.produtos and self.produtos[nome].quantidade <= 10:
                print(f'ALERTA: estoque baixo para o produto {nome}!')
