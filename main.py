import estoque
import consulta


if __name__ == '__main__':
    estoque.cadastrar_produto('Tinta', 10, 20.0)
    consulta.consultar_id('Tinta')
    estoque.registrar_venda(1, 25)
