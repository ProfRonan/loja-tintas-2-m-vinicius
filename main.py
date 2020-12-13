"""Arquivo principal que será interpretado pelo interpretador."""
import math


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI

    print('Área a ser pintada em metros quadrados:')
    a = float(input('> '))

    quant_litros_latas = a / 6
    latas = quant_litros_latas / 18
    latas = math.ceil(latas)
    preco_latas = latas * 80

    print(f'O valor gasto comprando apenas latas é de R$ {preco_latas:.2f}.')
    print(f'Serão necessárias {latas} latas.')

    quant_litros_galao = a / 6
    galao = quant_litros_galao / 3.6
    galao = math.ceil(galao)
    preco_galao = galao * 25

    print(f'O valor gasto comprando apenas latas é de R$ {preco_galao:.2f}.')
    print(f'Serão necessárias {galao} latas.')

    #O valor gasto comprando de forma que gere a menor quantidade de desperdício é de R$ [valor com duas casas decimais].Serão necessárias [quantidade] latas e [quantidade] galões.


if __name__ == '__main__':
    main()
