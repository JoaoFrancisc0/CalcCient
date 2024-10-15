from sympy import *

# Dicionário de substituições
substituicoes = {
    'π': '3.141592653', 'e': '2.718281828',
    '×': '*', '÷': '/', 'E': '*10**',
    '%': '/100', '!': '*factorial'
}

# Função para substituir caracteres em uma string
def substituir_caracteres(expressao, substituicoes):
    for char, substituto in substituicoes.items():
        expressao = expressao.replace(char, substituto)
    return expressao

def calcular(expressao):
    expressao = ''.join(expressao)
    expressao = substituir_caracteres(expressao, substituicoes)
    expressao = sympify(expressao)
    r = symbols('r')
    expressao = Eq(expressao, r)
    solution = solve(expressao, r)
    solution = [sol.evalf() for sol in solution]
    return solution
