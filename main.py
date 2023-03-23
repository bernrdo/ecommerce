import threading
import estoque
import pedido

# exemplo de uso
estoque = estoque.Estoque()
estoque.adicionar_produto('produto1', 100)
estoque.adicionar_produto('produto2', 50)

gerenciador_pedidos = pedido.GerenciadorPedidos(estoque)

# criação de threads para processar pedidos
t1 = threading.Thread(target=gerenciador_pedidos.processar_pedido, args=(pedido.Pedido('produto1', 50),))
t2 = threading.Thread(target=gerenciador_pedidos.processar_pedido, args=(pedido.Pedido('produto2', 60),))
t3 = threading.Thread(target=gerenciador_pedidos.processar_pedido, args=(pedido.Pedido('produto1', 60),))

t1.start()
t2.start()
t3.start()

# aguarda a finalização das threads
t1.join()
t2.join()
t3.join()

# exibe o estoque atualizado
print('Estoque atualizado:')
print(f'produto1: {estoque.consultar_estoque("produto1")}')
print(f'produto2: {estoque.consultar_estoque("produto2")}')
