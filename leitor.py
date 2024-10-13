from metodos import *

N = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',']
n = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
V = ['π', 'e', 'A', 'B', 'C', 'D', 'E', 'F', 'X', 'Y', 'M']
O = ['√', '×' '÷', '%', 'sin', 'cos', 'tan', '!', '!', '/', 'E']
P = ['(', ')']
o = ['+', '-']
parenteseList = []
num1 = num2 = num3 = indiceNum1 = None
inicio = None

def calcular(funcao):
    i = 0
    while True:
        if funcao[i] == '(':
            print(parentese(funcao[i:]))
        i+=1

def parentese(parenteseFuncao):
    global inicio, num1, num2, indiceNum1
    i = 1
    contParentese = 0
    while True:
        # Caso o primeiro seja numero
        if parenteseFuncao[i] in N:
            print("entrou no if 2")
            if inicio is None:
                inicio = i
                indiceNum1 = i
        # Caso o caracter n seja mais um numero ou virgula deve salvar o numero e nem parentese
        elif parenteseFuncao[i] not in N or parenteseFuncao[i] == ')':
            print("entrou no else")
            if inicio is not None:
                if num1 is None:
                    num1 = parenteseFuncao[inicio:i]
                elif num2 is None:
                    num2 = parenteseFuncao[inicio:i]
                inicio = None
            # Caso o caracter seja uma potencia
            if parenteseFuncao[i] in n:
                print("7 - Detectou que é uma potencia")############################################################################################################
                if inicio is None:
                    inicio = i
                    indiceNum1 = i
                # Caso o caracter n seja mais uma potencia deve salvar a potencia
                else:
                    if inicio is not None:
                        if num1 is None:
                            num1 = parenteseFuncao[inicio:i]
                        elif num2 is None:
                            num2 = parenteseFuncao[inicio:i]
                        inicio = None
                    # Caso n seja nem potencia e nem raiz então a potencia acabou então é um numero com potencia
                    if parenteseFuncao[i + 1] != '√':
                        # Vai retornar uma array e posiciona-la aonde começou o primeiro numero
                        parenteseFuncao[indiceNum1:indiceNum1] = calcPotencia(num1, num2)
                        num1 = None
                        num2 = None
                        return parenteseFuncao
        # Se achar inicio de um novo parentese
        elif parenteseFuncao[i] == '(':
            contParentese += 1
        # Se achar final de um parentese, verifica tbm se ja n é o fechamento do parentese principal
        elif parenteseFuncao[i] == ')' and i < len(parenteseFuncao):

            contParentese -= 1
            if contParentese == 0:
                # Recursão
                parentese(parenteseFuncao[:i])


        if (i+1) < len(parenteseFuncao):
            i+=1

# Eu to considerando que a potencia é apenas os que estão em n[]