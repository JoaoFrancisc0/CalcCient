from ui import tela
from botoes import switch_case
equacao = []
resultado = A = B = C = D = E = F = X = Y = M = None
shift = alpha = store = False

while True:
    tela(equacao, resultado, shift, alpha)
    entrada = input("Escolha um botão: ")
    equacao, resultado, shift, alpha, store, A, B, C, D, E, F, X, Y, M = switch_case(equacao, resultado, entrada, shift, alpha, store, A, B, C, D, E, F, X, Y, M)