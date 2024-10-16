from sympy import *
from botoes import switch_case
from calculadora import calcular_raiz
from ui import tela

def raiz_while(equacao, indice):
    resultado = A = B = C = D = E = F = X = Y = M = None
    shift = alpha = store = False
    expressao = []
    while True:
        input_char = input("Indice da raiz: ")
        expressao, resultado, shift, alpha, store, A, B, C, D, E, F, X, Y, M = switch_case(expressao, resultado, input_char, shift, alpha, store, A, B, C, D, E, F, X, Y, M)
        equacaoComRaiz = equacao.copy()
        print(equacaoComRaiz)
        equacaoComRaiz.append(indice)
        print(equacaoComRaiz)
        if indice != '':
            equacaoComRaiz += '√'
        equacaoComRaiz += expressao
        if indice == '':
            equacaoComRaiz.append('√')
        equacaoComRaizString = ''.join(str(char) for char in equacaoComRaiz)
        tela(equacaoComRaizString, resultado, shift, alpha)
        if ')' in expressao:
            expressao = ''.join(str(char) for char in expressao)
            expressao = expressao.replace('(', '').replace(')', '')
            return expressao

equacao = ['5','+']
indice = ''
raiz_while(equacao, indice)