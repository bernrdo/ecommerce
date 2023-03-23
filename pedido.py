import threading


class Pedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade


class GerenciadorPedidos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = threading.Lock()

    def verificar_disponibilidade(self, pedido):
        with self.lock:
            return self.estoque.remover_produto(pedido.produto, pedido.quantidade)

    def processar_pedido(self, pedido):
        if self.verificar_disponibilidade(pedido):
            print(f'Pedido processado: {pedido.quantidade} unidades do produto {pedido.produto}')
        else:
            print(f'Pedido não pode ser processado: estoque insuficiente para o produto {pedido.produto}')
