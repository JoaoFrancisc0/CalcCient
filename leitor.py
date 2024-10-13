from metodos import *

N = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',']
n = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
V = ['π', 'e', 'A', 'B', 'C', 'D', 'E', 'F', 'X', 'Y', 'M']
O = ['√', '×' '÷', '%', 'sin', 'cos', 'tan', '!', '/', 'E']
P = ['(', ')']
o = ['+', '-']
inicio = inicio1 = final1 = final2 = num1 = num2 = num3 = None

def calcular(funcao):
    global inicio, inicio1, num1, num2, final1, final2, num3
    i = 0
    bloqueador = 0
    while i < len(funcao):
        # Numero
        if funcao[i] in N:
            salvarNum(funcao, N, i)
            bloqueador = 1
        # final do numero
        elif funcao[i] not in N and inicio is not None and bloqueador == 1 or i == len(funcao)-1 and bloqueador == 1:
            num1, num2, final1, final2, bloqueador = finalNumero(num1, num2, final1, final2, funcao, i)

        # Potencia
        if funcao[i] in n and bloqueador != 1:
            salvarNum(funcao, n, i)
            bloqueador = 2
        # final da potencia
        elif funcao[i] not in n and inicio is not None and bloqueador == 2 or i == len(funcao)-1 and bloqueador == 2:
            num1, num2, final1, final2, num3, bloqueador = finalPotencia(num1, num2, num3, inicio1, final1, final2, funcao, i)
        i += 1
    if i == len(funcao):
        i -= 1
        if funcao[i] not in N and inicio is not None and bloqueador == 1 or i == len(funcao) - 1 and bloqueador == 1:
            num1, num2, final1, final2, bloqueador = finalNumero(num1, num2, final1, final2, funcao, i)
        elif funcao[i] not in n and inicio is not None and bloqueador == 2 or i == len(funcao) - 1 and bloqueador == 2:
            num1, num2, final1, final2, num3, bloqueador = finalPotencia(num1, num2, num3, inicio1, final1, final2, funcao, i)
    num1 = num2 = inicio1 = final1 = final2 = None
    return funcao




# ⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹
def potencia(funcao, index):
    """"""

# π e A B C D E F X Y M
def variavel(funcao, index):
    """"""

# √
def raiz(funcao, index):
    """"""

# × ÷ % /
def operadorPrior(funcao, index):
    """"""

# + -
def operadorSimpl(funcao, index):
    """"""

# !
def fatorial(funcao, index):
    """"""

# sin cos tan
def trigonometrica(funcao, index):
    """"""

# E
def notacao(funcao, index):
    """"""

# ( )
def parentese(funcao, index):
    """"""

# N n
def salvarNum(funcao, tipo, i):
    global inicio, inicio1, num1, num2
    if funcao[i] in tipo and inicio is None:
        inicio = i
        if inicio1 is None:
            inicio1 = inicio
    # final do numero
    elif funcao[i] not in tipo and inicio is not None:
        final = i
        num = funcao[inicio:final]
        num = converterListParaNum(num)
        inicio = final = None
        return num
    elif funcao[i] in tipo and i == len(funcao)-1:
        final = i
        num = funcao[inicio:final+1]
        num = converterListParaNum(num)
        inicio = final = None
        return num

def finalNumero(num1, num2, final1, final2, funcao, i):
    if num1 is None:
        num1 = salvarNum(funcao, N, i)
        final1 = i
    else:
        num2 = salvarNum(funcao, N, i)
        final2 = i
    bloqueador = 0
    return num1, num2, final1, final2, bloqueador

def finalPotencia(num1, num2, num3, inicio1, final1, final2, funcao, i):
    if num1 is None:
        num1 = salvarNum(funcao, n, i)
        final1 = i
    else:
        num2 = salvarNum(funcao, n, i)
        final2 = i
        num3 = calcPotencia(num1, num2)
        # Remove os valores que foram operados e depois adiciona o resultado a operação
        del funcao[inicio1:final2+1]
        funcao[inicio1:inicio1] = num3
    bloqueador = 0
    return num1, num2, final1, final2, num3, bloqueador
# Eu to considerando que a potencia é apenas os que estão em n[]