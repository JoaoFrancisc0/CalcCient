from leitor import calcular

N = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
n = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
cont = 0

def switch_case(funcao, resultado, case, shift, alpha, store, A, B, C, D, E, F, X, Y, M):
    global cont
    case = int(case)
    match case:
        # SHIFT
        case 1:
            shift = True
            alpha = False
            return funcao, shift, alpha, False, A, B, C, D, E, F, X, Y, M
        # ALPHA
        case 2:
            alpha = True
            shift = False
            return funcao, shift, alpha, False, A, B, C, D, E, F, X, Y, M
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
                funcao.append('³')
            if shift:
                funcao.append('³')
                funcao.append('√')
        # ab/c  # d/c
        case 10:
            if not shift:
                if resultado == None:
                    funcao.append('/')
                else:
                    ""
                    # Chamar alguma função para converter o resultado para decimal
            if shift:
                funcao.append('³')
                funcao.append('√')
        # √
        case 11:
            funcao.append('√')
        # X²
        case 12:
            funcao.append('²')
        # ^     #^x√
        case 13:
            if not shift:
                funcao.append('^')
            if shift:
                cont = 1
                while True:
                    if funcao[-cont] in N:
                        posicao = N.index(funcao[-cont])
                        funcao.pop(-cont)
                        funcao.append(n[posicao])
                        cont = cont + 1
                    else:
                        break
                funcao.append('√')
        # log   # 10^x
        case 14:
            if not shift:
                funcao.append('log')
            if shift:
                funcao.append('10')
                funcao.append('^')
        # ln    # e^x   # e
        case 15:
            if not shift and not alpha:
                funcao.append('ln')
            elif shift:
                funcao.append('e')
                funcao.append('^')
            elif alpha:
                funcao.append('e')
        # (-)           # A
        case 16:
            if not store:
                funcao.append('-')
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
                funcao.append('sin')
            elif shift:
                ''
            elif store:
                D = resultado
        # cos   # cos-¹ # E
        case 20:
            if not store and not shift:
                funcao.append('cos')
            elif shift:
                ''
            elif store:
                E = resultado
        # tan   # tan-¹ # F
        case 21:
            if not store and not shift:
                funcao.append('tan')
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
                return funcao, False, False, store, A, B, C, D, E, F, X, Y, M
        # ENG   # <--
        case 23:
            return "Executando o case 1"
        # (
        case 24:
            funcao.append('(')
        # )             # X
        case 25:
            if not store:
                funcao.append(')')
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
                if funcao[cont-1] == '^':
                    funcao.pop()
                    funcao.append('⁷')
                elif funcao[cont-1] in n:
                    funcao.append('⁷')
            else:
                 funcao.append('7')
        # 8
        case 29:
            if cont != 0:
                if funcao[cont-1] == '^':
                    funcao.pop()
                    funcao.append('⁸')
                elif funcao[cont-1] in n:
                    funcao.append('⁸')
            else:
                funcao.append('8')
        # 9
        case 30:
            if cont != 0:
                if funcao[cont-1] == '^':
                    funcao.pop()
                    funcao.append('⁹')
                elif funcao[cont-1] in n:
                    funcao.append('⁹')
            else:
                funcao.append('9')
        # DEL   # INS
        case 31:
            return "Executando o case 1"
        # AC    # DT[CL]OFF
        case 32:
            return "Executando o case 2"
        # 4
        case 33:
            if cont != 0:
                if funcao[cont-1] == '^':
                    funcao.pop()
                    funcao.append('⁴')
                elif funcao[cont-1] in n:
                    funcao.append('⁴')
            else:
                funcao.append('4')
        # 5
        case 34:
            if cont != 0:
                if funcao[cont-1] == '^':
                    funcao.pop()
                    funcao.append('⁵')
                elif funcao[cont-1] in n:
                    funcao.append('⁵')
            else:
                funcao.append('5')
        # 6
        case 35:
            if cont != 0:
                if funcao[cont-1] == '^':
                    funcao.pop()
                    funcao.append('⁶')
                elif funcao[cont-1] in n:
                    funcao.append('⁶')
            else:
                funcao.append('6')
        # ×
        case 36:
            funcao.append('×')
        # ÷
        case 37:
            funcao.append('÷')
        # 1     # [S-SUM]
        case 38:
            if not shift:
                if cont != 0:
                    if funcao[cont-1] == '^':
                        funcao.pop()
                        funcao.append('¹')
                    elif funcao[cont-1] in n:
                        funcao.append('¹')
                else:
                    funcao.append('1')
            if shift:
                ''
        # 2     # [S-VAR]
        case 39:
            if not shift:
                if cont != 0:
                    if funcao[cont-1] == '^':
                        funcao.pop()
                        funcao.append('²')
                    elif funcao[cont-1] in n:
                        funcao.append('²')
                else:
                    funcao.append('2')
            if shift:
                ''
        # 3
        case 40:
            if cont != 0:
                if funcao[cont-1] == '^':
                    funcao.pop()
                    funcao.append('³')
                elif funcao[cont-1] in n:
                    funcao.append('³')
            else:
                funcao.append('3')
        # +
        case 41:
            funcao.append('+')
        # -
        case 42:
            funcao.append('-')
        # 0     # Rnd
        case 43:
            if not shift:
                if cont != 0:
                    if funcao[cont-1] == '^':
                        funcao.pop()
                        funcao.append('⁰')
                    elif funcao[cont-1] in n:
                        funcao.append('⁰')
                else:
                    funcao.append('0')
            if shift:
                ''
        # .     # Ran#
        case 44:
            if not shift:
                funcao.append(',')
            if shift:
                ''
        # EXP   # π
        case 45:
            if not shift:
                funcao.append('E')
            if shift:
                funcao.append('π')
        # Ans   # DRG>
        case 46:
            if not shift:
                ''
            if shift:
                ''
        # =     # %
        case 47:
            if not shift:
                resultado = calcular(funcao)
                cont = 0
            if shift:
                funcao.append('%')
    cont += 1
#          resultado, shift, alpha, store, A, B, C, D, E, F, X, Y, M
    return resultado, False, False, False, A, B, C, D, E, F, X, Y, M