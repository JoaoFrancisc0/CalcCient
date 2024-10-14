import math

# Os metodos precisam retornar os valores em formato de array com cada caractere separado
N = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
n = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']

def converterListParaNum(num):
    if num[0] in n:
        # Criar um dicionário para mapeamento
        mapeamento = {n[i]: N[i] for i in range(len(N))}
        # Converter superíndices para dígitos normais usando o dicionário
        num = [mapeamento.get(char, char) for char in num]
    # Juntar os elementos em uma única string
    num = ''.join(num)
    # Substituir a vírgula por um ponto
    num = num.replace(',', '.')
    # Converter a string para float
    num = float(num)
    return num

def converterNumParaList(num):
    # Converter o número para string
    num_str = str(num)
    # Criar a lista que irá armazenar os caracteres
    array = []
    for char in num_str:
        if char in N:
            # Encontrar o índice do dígito e pegar o índice correspondente
            index = N.index(char)
            array.append(N[index])
        elif char == '.':
            # Substituir o ponto por vírgula
            array.append(',')
    return array

def calcPotencia(num1, num2):
    num1 = math.pow(num1, num2)
    num = converterNumParaList(num1)
    return num
