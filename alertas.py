import db
import schedule
import time


def alerta_estoque_baixo():
    produtos = db.Produto.select().where(db.Produto.quantidade <= 5)
    if produtos.count() > 0:
        print('Alerta de estoque baixo:')
        for produto in produtos:
            print(f'{produto.nome} - quantidade em estoque: {produto.quantidade}')
    else:
        print('Não há produtos com estoque baixo')


# solução sugerida pelo ChatGPT
# Agendar a execução da função verificar_estoque a cada 1 hora
schedule.every(1).hour.do(alerta_estoque_baixo)

# Loop principal do programa
while True:
    schedule.run_pending()
    time.sleep(60)
