import flet as ft
from botoes import switch_case
from ui import tela

equacao = []
resultado = A = B = C = D = E = F = X = Y = M = None
shift = alpha = store = False
equacao_ref = ft.Ref[ft.Text]()
resultado_ref = ft.Ref[ft.Text]()

# Função que será chamada ao clicar no botão
def button_click(value):
    global equacao, resultado, shift, alpha, store, A, B, C, D, E, F, X, Y, M
    equacao, resultado, shift, alpha, store, A, B, C, D, E, F, X, Y, M = switch_case(equacao, resultado, value, shift, alpha, store, A, B, C, D, E, F, X, Y, M)
    tela(equacao, resultado, shift, alpha)

def main(page: ft.Page):
    # Defina o tamanho da janela
    page.window_width = 500  # Largura da janela
    page.window_height = 400  # Altura da janela
    global equacao, resultado, shift, alpha
    equacaoTela = ft.Text("")
    resultadoTela = ft.Text("")
    shift_text = ft.Text("S") if shift else ft.Text("")
    alpha_text = ft.Text("A") if alpha else ft.Text("")
    page.title = "Calc App"

    page.add(
        ft.Row(
            controls=[
                ft.ElevatedButton(text="SHIFT", on_click=lambda e: button_click(1)),
                ft.ElevatedButton(text="ALPHA", on_click=lambda e: button_click(2)),
                ft.ElevatedButton(text="REPLAY", on_click=lambda e: button_click(3)),
                ft.ElevatedButton(text="MODE", on_click=lambda e: button_click(4)),
                ft.ElevatedButton(text="ON", on_click=lambda e: button_click(5)),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="ab/c", on_click=lambda e: button_click(10)),
                ft.ElevatedButton(text="√", on_click=lambda e: button_click(11)),
                ft.ElevatedButton(text="x²", on_click=lambda e: button_click(12)),
                ft.ElevatedButton(text="^", on_click=lambda e: button_click(13)),
                ft.ElevatedButton(text="log", on_click=lambda e: button_click(14)),
                ft.ElevatedButton(text="ln", on_click=lambda e: button_click(15)),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="(-)", on_click=lambda e: button_click(16)),
                ft.ElevatedButton(text=".,,,", on_click=lambda e: button_click(17)),
                ft.ElevatedButton(text="hyp", on_click=lambda e: button_click(18)),
                ft.ElevatedButton(text="sin", on_click=lambda e: button_click(19)),
                ft.ElevatedButton(text="cos", on_click=lambda e: button_click(20)),
                ft.ElevatedButton(text="tan", on_click=lambda e: button_click(21)),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="RCL", on_click=lambda e: button_click(22)),
                ft.ElevatedButton(text="ENG", on_click=lambda e: button_click(23)),
                ft.ElevatedButton(text="(", on_click=lambda e: button_click(24)),
                ft.ElevatedButton(text=")", on_click=lambda e: button_click(25)),
                ft.ElevatedButton(text=",", on_click=lambda e: button_click(26)),
                ft.ElevatedButton(text="M+", on_click=lambda e: button_click(27)),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="7", on_click=lambda e: button_click(28)),
                ft.ElevatedButton(text="8", on_click=lambda e: button_click(29)),
                ft.ElevatedButton(text="9", on_click=lambda e: button_click(30)),
                ft.ElevatedButton(text="DEL", on_click=lambda e: button_click(31)),
                ft.ElevatedButton(text="AC", on_click=lambda e: button_click(32)),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="4", on_click=lambda e: button_click(33)),
                ft.ElevatedButton(text="5", on_click=lambda e: button_click(34)),
                ft.ElevatedButton(text="6", on_click=lambda e: button_click(35)),
                ft.ElevatedButton(text="×", on_click=lambda e: button_click(36)),
                ft.ElevatedButton(text="÷", on_click=lambda e: button_click(37)),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="1", on_click=lambda e: button_click(38)),
                ft.ElevatedButton(text="2", on_click=lambda e: button_click(39)),
                ft.ElevatedButton(text="3", on_click=lambda e: button_click(40)),
                ft.ElevatedButton(text="+", on_click=lambda e: button_click(41)),
                ft.ElevatedButton(text="-", on_click=lambda e: button_click(42)),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="0", on_click=lambda e: button_click(43)),
                ft.ElevatedButton(text=".", on_click=lambda e: button_click(44)),
                ft.ElevatedButton(text="EXP", on_click=lambda e: button_click(45)),
                ft.ElevatedButton(text="Ans", on_click=lambda e: button_click(46)),
                ft.ElevatedButton(text="=", on_click=lambda e: button_click(47)),
            ]
        ),
    )

ft.app(main)
