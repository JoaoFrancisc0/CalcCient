import sympy as sp

def calcular_trigonometria(funcao, y):
    # Converte o valor de y para um símbolo radiano
    radianos = sp.Rational(y)  # Pode ser decimal ou fração exata

    # Dicionário para mapear entrada textual para função sympy correspondente
    funcoes = {
        'sen': sp.sin,
        'cos': sp.cos,
        'tan': sp.tan
    }

    # Verifica se a função existe no dicionário
    if funcao not in funcoes:
        return "Função inválida. Use 'sen', 'cos' ou 'tan'."

    # Calcula a função escolhida com o valor de radianos fornecido
    resultado = funcoes[funcao](radianos)
    return resultado.simplify()

# Exemplos de uso
print(calcular_trigonometria('sen', sp.pi / 2))  # Resultado: 1
print(calcular_trigonometria('cos', 0))          # Resultado: 1
print(calcular_trigonometria('tan', sp.pi / 4))  # Resultado: 1
