from calculadora import calcular

N = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
cont = 0

def switch_case(equacao, resultado, case, shift, alpha, store, A, B, C, D, E, F, X, Y, M):
    case = int(case)
    match case:
        # SHIFT
        case 1:
            shift = True
            alpha = False
            return equacao, resultado, shift, alpha, False, A, B, C, D, E, F, X, Y, M
        # ALPHA
        case 2:
            alpha = True
            shift = False
            return equacao, resultado, shift, alpha, False, A, B, C, D, E, F, X, Y, M
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
            if not shift:
                equacao.append('^')
                equacao.append('(')
                equacao.append('-')
                equacao.append('1')
                equacao.append(')')

            if shift:
                equacao.append('!')
        # nCr   # nPr
        case 7:
            return "Executando o case 1"
        # Pol() # Rec(  #:
        case 8:
            return "Executando o case 2"
        # X³    # ³√
        case 9:
            if not shift:
                equacao.append('^')
                equacao.append('3')
            if shift:
                equacao.append('3')
                equacao.append('√')
        # ab/c  # d/c
        case 10:
            if not shift:
                if resultado == None:
                    equacao.append('/')
                else:
                    ""
                    # Chamar alguma função para converter o resultado para decimal
        # √
        case 11:
            equacao.append('√')
        # X²
        case 12:
            equacao.append('^')
            equacao.append('2')
        # ^     #^x√
        case 13:
            if not shift:
                equacao.append('^')
            if shift:
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
                equacao.append('sin')
                equacao.append('^')
                equacao.append('(')
                equacao.append('-')
                equacao.append('1')
                equacao.append(')')
            elif store:
                D = resultado
        # cos   # cos-¹ # E
        case 20:
            if not store and not shift:
                equacao.append('cos')
            elif shift:
                equacao.append('cos')
                equacao.append('^')
                equacao.append('(')
                equacao.append('-')
                equacao.append('1')
                equacao.append(')')
            elif store:
                E = resultado
        # tan   # tan-¹ # F
        case 21:
            if not store and not shift:
                equacao.append('tan')
            elif shift:
                equacao.append('tan')
                equacao.append('^')
                equacao.append('(')
                equacao.append('-')
                equacao.append('1')
                equacao.append(')')
            elif store:
                F = resultado
        # RCL   # STO
        case 22:
            if not shift:
                ''
            if shift:
                store = True
                return equacao, resultado, False, False, False, A, B, C, D, E, F, X, Y, M
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
            equacao.append('7')
        # 8
        case 29:
            equacao.append('8')
        # 9
        case 30:
            equacao.append('9')
        # DEL   # INS
        case 31:
            return "Executando o case 1"
        # AC    # DT[CL]OFF
        case 32:
            return "Executando o case 2"
        # 4
        case 33:
            equacao.append('4')
        # 5
        case 34:
            equacao.append('5')
        # 6
        case 35:
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
                equacao.append('1')
            if shift:
                ''
        # 2     # [S-VAR]
        case 39:
            if not shift:
                equacao.append('2')
            if shift:
                ''
        # 3
        case 40:
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
                equacao = []
            if shift:
                equacao.append('%')
#          equacao, resultado, shift, alpha, store, A, B, C, D, E, F, X, Y, M
    return equacao, resultado, False, False, False, A, B, C, D, E, F, X, Y, M