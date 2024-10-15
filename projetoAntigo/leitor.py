from metodos import *

N = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',']
n = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
V = ['π', 'e', 'A', 'B', 'C', 'D', 'E', 'F', 'X', 'Y', 'M']
O = ['√', '×' '÷', '%', 'sin', 'cos', 'tan', '!', '/', 'E']
P = ['(', ')']
o = ['+', '-']

# inicio é o index na função para o inicio de um numero
# inicio1 é o index na função para o inicio do num1
# final1 é o index do primeiro caracter após o num1
# final2 é o index do primeiro caracter após o num2
# num1 é a variavel que varia entre lista de char e float, armazena o primeiro numero encontrado, resetando apos a operação
# num2 é a variavel que varia entre lista de char e float, armazena o segundo numero encontrado, resetando apos a operação
# num3 é a variavel que armazena o resultado da operação entre num1 e num2, sempre sendo uma lista de char

inicio = inicio1 = final1 = final2 = num1 = num2 = num3 = None

def calcular(equacao):
    global inicio, inicio1, num1, num2, final1, final2, num3
    i = 0
    bloqueador = 0
    while i < len(equacao):
        # Numero
        if equacao[i] in N:
            salvarNum(equacao, N, i)
            bloqueador = 1
        # final do numero
        elif equacao[i] not in N and inicio is not None and bloqueador == 1 or i == len(equacao)-1 and bloqueador == 1:
            num1, num2, final1, final2, bloqueador = finalNumero(num1, num2, final1, final2, equacao, i)

        # Potencia
        if equacao[i] in n and bloqueador != 1:
            salvarNum(equacao, n, i)
            bloqueador = 2
        # final da potencia
        elif equacao[i] not in n and inicio is not None and bloqueador == 2 or i == len(equacao)-1 and bloqueador == 2:
            num1, num2, final1, final2, num3, bloqueador = finalPotencia(num1, num2, num3, inicio1, final1, final2, equacao, i)
        i += 1
    if i == len(equacao):
        i -= 1
        if equacao[i] not in N and inicio is not None and bloqueador == 1 or i == len(equacao) - 1 and bloqueador == 1:
            num1, num2, final1, final2, bloqueador = finalNumero(num1, num2, final1, final2, equacao, i)
        elif equacao[i] not in n and inicio is not None and bloqueador == 2 or i == len(equacao) - 1 and bloqueador == 2:
            num1, num2, final1, final2, num3, bloqueador = finalPotencia(num1, num2, num3, inicio1, final1, final2, equacao, i)
    num1 = num2 = inicio1 = final1 = final2 = None
    return equacao




# ⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹
def potencia(equacao, index):
    """"""

# π e A B C D E F X Y M
def variavel(equacao, index):
    """"""

# √
def raiz(equacao, index):
    """"""

# × ÷ % /
def operadorPrior(equacao, index):
    """"""

# + -
def operadorSimpl(equacao, index):
    """"""

# !
def fatorial(equacao, index):
    """"""

# sin cos tan
def trigonometrica(equacao, index):
    """"""

# E
def notacao(equacao, index):
    """"""

# ( )
def parentese(equacao, index):
    """"""

# N n
def salvarNum(equacao, tipo, i):
    global inicio, inicio1, num1, num2
    if equacao[i] in tipo and inicio is None:
        inicio = i
        if inicio1 is None:
            inicio1 = inicio
    # final do numero
    elif equacao[i] not in tipo and inicio is not None:
        final = i
        num = equacao[inicio:final]
        num = converterListParaNum(num)
        inicio = final = None
        return num
    elif equacao[i] in tipo and i == len(equacao)-1:
        final = i
        num = equacao[inicio:final+1]
        num = converterListParaNum(num)
        inicio = final = None
        return num

def finalNumero(num1, num2, final1, final2, equacao, i):
    if num1 is None:
        num1 = salvarNum(equacao, N, i)
        final1 = i
    else:
        num2 = salvarNum(equacao, N, i)
        final2 = i
    bloqueador = 0
    return num1, num2, final1, final2, bloqueador

def finalPotencia(num1, num2, num3, inicio1, final1, final2, equacao, i):
    if num1 is None:
        num1 = salvarNum(equacao, n, i)
        final1 = i
    else:
        num2 = salvarNum(equacao, n, i)
        final2 = i
        num3 = calcPotencia(num1, num2)
        # Remove os valores que foram operados e depois adiciona o resultado a operação
        del equacao[inicio1:final2+1]
        equacao[inicio1:inicio1] = num3
    bloqueador = 0
    return num1, num2, final1, final2, num3, bloqueador
# Eu to considerando que a potencia é apenas os que estão em n[]