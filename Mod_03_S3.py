'''Semana 03'''

def exibir_cardapio():
    cardapio = """
    *******************Cardápio*******************
    ----------------------------------------------
    | Código |        Descrição        |  Valor  |
    |   100  |     Cachorro Quente     |   9,00  |
    |   101  |  Cachorro Quente Duplo  |  11,00  |
    |   102  |           X-Egg         |  12,00  |
    |   103  |         X-Salada        |  12,00  |
    |   104  |          X-Bacon        |  14,00  |
    |   105  |           X-Tudo        |  17,00  |
    |   200  |    Refrigerente Lata    |   5,00  |
    |   201  |         Chá Gelado      |   4,00  |
    ----------------------------------------------
    """
    print(cardapio)


def calcular_total_pedido(codigo):
    if codigo == 100:
        print('Você pediu um Cachorro Quente no valor de 9,00')
        return 9.00
    elif codigo == 101:
        print('Você pediu um Cachorro Quente Duplo no valor de 11,00')
        return 11.00
    elif codigo == 102:
        print('Você pediu um X-Egg no valor de 12,00')
        return 12.00
    elif codigo == 103:
        print('Você pediu um X-Salada no valor de 12,00')
        return 12.00
    elif codigo == 104:
        print('Você pediu um X-Bacon no valor de 14,00')
        return 14.00
    elif codigo == 105:
        print('Você pediu um X-Tudo no valor de 17,00')
        return 17.00
    elif codigo == 200:
        print('Você pediu um refrigerante Lata no valor de 5,00')
        return 5.00
    elif codigo == 201:
        print('Você pediu um Chá Gelado no valor de 4,00')
        return 4.00
    else:
        print('Opção inválida')
        return 0.00


def fazer_pedido():
    total = 0.0

    exibir_cardapio()

    while True:
        codigo = int(input('Entre com o código desejado: '))

        valor_pedido = calcular_total_pedido(codigo)
        total += valor_pedido

        print('Deseja pedir mais alguma coisa?')
        print('1 - Sim')
        print('2 - Não')
        pedir_mais = int(input())

        if pedir_mais == 2:
            break

    print(f'O total a ser pago é: {total:.2f} R$')


if __name__ == '__main__':
    fazer_pedido()