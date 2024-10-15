from leitor import calcular

N = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
n = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
cont = 0

def switch_case(equacao, resultado, case, shift, alpha, store, A, B, C, D, E, F, X, Y, M):
    global cont
    case = int(case)
    match case:
        # SHIFT
        case 1:
            shift = True
            alpha = False
            return equacao, shift, alpha, False, A, B, C, D, E, F, X, Y, M
        # ALPHA
        case 2:
            alpha = True
            shift = False
            return equacao, shift, alpha, False, A, B, C, D, E, F, X, Y, M
        # REPLAY
        case 3:
            return "Executando o case 1"
        # MODE  # CLR
        case 4:
            return "Executando o case 2"
        # ON
        case 5:
            return "Executando o case 1"
        # X-¹   # X!
        case 6:
            return "Executando o case 2"
        # nCr   # nPr
        case 7:
            return "Executando o case 1"
        # Pol() # Rec(  #:
        case 8:
            return "Executando o case 2"
        # X³    # ³√
        case 9:
            if not shift:
                equacao.append('³')
            if shift:
                equacao.append('³')
                equacao.append('√')
        # ab/c  # d/c
        case 10:
            if not shift:
                if resultado == None:
                    equacao.append('/')
                else:
                    ""
                    # Chamar alguma função para converter o resultado para decimal
            if shift:
                equacao.append('³')
                equacao.append('√')
        # √
        case 11:
            equacao.append('√')
        # X²
        case 12:
            equacao.append('²')
        # ^     #^x√
        case 13:
            if not shift:
                equacao.append('^')
            if shift:
                cont = 1
                while True:
                    if equacao[-cont] in N:
                        posicao = N.index(equacao[-cont])
                        equacao.pop(-cont)
                        equacao.append(n[posicao])
                        cont = cont + 1
                    else:
                        break
                equacao.append('√')
        # log   # 10^x
        case 14:
            if not shift:
                equacao.append('log')
            if shift:
                equacao.append('10')
                equacao.append('^')
        # ln    # e^x   # e
        case 15:
            if not shift and not alpha:
                equacao.append('ln')
            elif shift:
                equacao.append('e')
                equacao.append('^')
            elif alpha:
                equacao.append('e')
        # (-)           # A
        case 16:
            if not store:
                equacao.append('-')
            else:
                A = resultado
        # º, ,, # <--   # B
        case 17:
            if not store and not shift:
                ''
            elif shift:
                ''
            elif store:
                B = resultado
        # hyp           # C
        case 18:
            if not store:
                ''
            elif store:
                C = resultado
        # sin   # sin-¹ # D
        case 19:
            if not store and not shift:
                equacao.append('sin')
            elif shift:
                ''
            elif store:
                D = resultado
        # cos   # cos-¹ # E
        case 20:
            if not store and not shift:
                equacao.append('cos')
            elif shift:
                ''
            elif store:
                E = resultado
        # tan   # tan-¹ # F
        case 21:
            if not store and not shift:
                equacao.append('tan')
            elif shift:
                ''
            elif store:
                F = resultado
        # RCL   # STO
        case 22:
            if not shift:
                ''
            if shift:
                store = True
                return equacao, False, False, store, A, B, C, D, E, F, X, Y, M
        # ENG   # <--
        case 23:
            return "Executando o case 1"
        # (
        case 24:
            equacao.append('(')
        # )             # X
        case 25:
            if not store:
                equacao.append(')')
            elif store:
                X = resultado
        # ,     # ;     # Y
        case 26:
            if not store and not shift:
                ''
            elif shift:
                ''
            elif store:
                Y = resultado
        # M+    # M-    # M
        case 27:
            if not store and not shift:
                ''
            elif shift:
                ''
            elif store:
                M = resultado
        # 7
        case 28:
            if cont != 0:
                if equacao[cont-1] == '^':
                    equacao.pop()
                    equacao.append('⁷')
                elif equacao[cont-1] in n:
                    equacao.append('⁷')
                else:
                    equacao.append('7')
            else:
                 equacao.append('7')
        # 8
        case 29:
            if cont != 0:
                if equacao[cont-1] == '^':
                    equacao.pop()
                    equacao.append('⁸')
                elif equacao[cont-1] in n:
                    equacao.append('⁸')
                else:
                    equacao.append('8')
            else:
                equacao.append('8')
        # 9
        case 30:
            if cont != 0:
                if equacao[cont-1] == '^':
                    equacao.pop()
                    equacao.append('⁹')
                elif equacao[cont-1] in n:
                    equacao.append('⁹')
                else:
                    equacao.append('9')
            else:
                equacao.append('9')
        # DEL   # INS
        case 31:
            return "Executando o case 1"
        # AC    # DT[CL]OFF
        case 32:
            return "Executando o case 2"
        # 4
        case 33:
            if cont != 0:
                if equacao[cont-1] == '^':
                    equacao.pop()
                    equacao.append('⁴')
                elif equacao[cont-1] in n:
                    equacao.append('⁴')
                else:
                    equacao.append('4')
            else:
                equacao.append('4')
        # 5
        case 34:
            if cont != 0:
                if equacao[cont-1] == '^':
                    equacao.pop()
                    equacao.append('⁵')
                elif equacao[cont-1] in n:
                    equacao.append('⁵')
                else:
                    equacao.append('5')
            else:
                equacao.append('5')
        # 6
        case 35:
            if cont != 0:
                if equacao[cont-1] == '^':
                    equacao.pop()
                    equacao.append('⁶')
                elif equacao[cont-1] in n:
                    equacao.append('⁶')
                else:
                    equacao.append('6')
            else:
                equacao.append('6')
        # ×
        case 36:
            equacao.append('×')
        # ÷
        case 37:
            equacao.append('÷')
        # 1     # [S-SUM]
        case 38:
            if not shift:
                if cont != 0:
                    if equacao[cont-1] == '^':
                        equacao.pop()
                        equacao.append('¹')
                    elif equacao[cont-1] in n:
                        equacao.append('¹')
                    else:
                        equacao.append('1')
                else:
                    equacao.append('1')
            if shift:
                ''
        # 2     # [S-VAR]
        case 39:
            if not shift:
                if cont != 0:
                    if equacao[cont-1] == '^':
                        equacao.pop()
                        equacao.append('²')
                    elif equacao[cont-1] in n:
                        equacao.append('²')
                    else:
                        equacao.append('2')
                else:
                    equacao.append('2')
            if shift:
                ''
        # 3
        case 40:
            if cont != 0:
                if equacao[cont-1] == '^':
                    equacao.pop()
                    equacao.append('³')
                elif equacao[cont-1] in n:
                    equacao.append('³')
                else:
                    equacao.append('3')
            else:
                equacao.append('3')
        # +
        case 41:
            equacao.append('+')
        # -
        case 42:
            equacao.append('-')
        # 0     # Rnd
        case 43:
            if not shift:
                if cont != 0:
                    if equacao[cont-1] == '^':
                        equacao.pop()
                        equacao.append('⁰')
                    elif equacao[cont-1] in n:
                        equacao.append('⁰')
                    else:
                        equacao.append('0')
                else:
                    equacao.append('0')
            if shift:
                ''
        # .     # Ran#
        case 44:
            if not shift:
                equacao.append(',')
            if shift:
                ''
        # EXP   # π
        case 45:
            if not shift:
                equacao.append('E')
            if shift:
                equacao.append('π')
        # Ans   # DRG>
        case 46:
            if not shift:
                ''
            if shift:
                ''
        # =     # %
        case 47:
            if not shift:
                resultado = calcular(equacao)
                cont = 0
            if shift:
                equacao.append('%')
    cont += 1
#          resultado, shift, alpha, store, A, B, C, D, E, F, X, Y, M
    return resultado, False, False, False, A, B, C, D, E, F, X, Y, M