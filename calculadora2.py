import tkinter as tk
import webbrowser

tema_claro = {
    "bg": "#ffeaf4",
    "display_bg": "#ffffff",
    "display_fg": "#333333",
    "btn_bg": "#ffffff",
    "btn_fg": "#555555",
    "op_bg": "#ffb3d9",
    "op_fg": "#ffffff",
}

tema_escuro = {
    "bg": "#1f1f2e",
    "display_bg": "#2c2c3a",
    "display_fg": "#ffffff",
    "btn_bg": "#3b3b4f",
    "btn_fg": "#dedede",
    "op_bg": "#ff2fa3",
    "op_fg": "#ffffff",
}

tema_atual = tema_claro  


def clicar(valor):
    if tela.get() == "0":
        tela.delete(0, tk.END)
    tela.insert(tk.END, valor)


def limpar():
    tela.delete(0, tk.END)
    tela.insert(0, "0")


def deletar():
    atual = tela.get()
    if len(atual) > 1:
        tela.delete(len(atual) - 1, tk.END)
    else:
        tela.delete(0, tk.END)
        tela.insert(0, "0")


def calcular():
    expressao = tela.get()
    if expressao.replace(" ", "") == "2+2":
        webbrowser.open("https://www.youtube.com/watch?v=-KTWKUctFq4")
        tela.delete(0, tk.END)
        tela.insert(0, "4")
        return
    
    if expressao.replace(" ", "") == "67":
        webbrowser.open("https://youtu.be/L7ejl_Hj3A8?si=8vT0CGCl4vJGk7sc")
        tela.delete(0, tk.END)
        tela.insert(0, "676767676767")
        return
    
    try:
        resultado = str(eval(tela.get()))
        tela.delete(0, tk.END)
        tela.insert(0, resultado)
    except:
        tela.delete(0, tk.END)
        tela.insert(0, "Erro")


def trocar_tema():
    global tema_atual
    tema_atual = tema_escuro if tema_atual == tema_claro else tema_claro
    aplicar_tema()


def aplicar_tema():
    janela.configure(bg=tema_atual["bg"])
    tela.configure(bg=tema_atual["display_bg"],
                   fg=tema_atual["display_fg"])

    for btn in botoes_normais:

        btn.configure(bg=tema_atual["btn_bg"],
                      fg=tema_atual["btn_fg"],
                      activebackground=tema_atual["btn_bg"])

    for btn in botoes_operadores:
        btn.configure(bg=tema_atual["op_bg"],
                      fg=tema_atual["op_fg"],
                      activebackground=tema_atual["op_bg"])

    botao_tema.configure(bg=tema_atual["op_bg"],
                         fg=tema_atual["op_fg"])


janela = tk.Tk()
janela.title("Calculadora Mel")
janela.geometry("360x520")
janela.resizable(False, False)

# Display
tela = tk.Entry(janela, font=("Arial", 36),
                border=0, justify="right")
tela.insert(0, "0")
tela.place(x=20, y=20, width=320, height=80)

# Botão de tema
botao_tema = tk.Button(janela, text="🌙", font=("Arial", 14),
                       relief="flat", command=trocar_tema)
botao_tema.place(x=290, y=110, width=40, height=40)

# Botões da calculadora
botoes = [
    ("clr", limpar), ("DEL", deletar), ("%", lambda: clicar("%")), ("/", lambda: clicar("/")),
    ("7", lambda: clicar("7")), ("8", lambda: clicar("8")), ("9", lambda: clicar("9")), ("*", lambda: clicar("*")),
    ("4", lambda: clicar("4")), ("5", lambda: clicar("5")), ("6", lambda: clicar("6")), ("-", lambda: clicar("-")),
    ("1", lambda: clicar("1")), ("2", lambda: clicar("2")), ("3", lambda: clicar("3")), ("+", lambda: clicar("+")),
    (".", lambda: clicar(".")), ("0", lambda: clicar("0")), ("=", calcular)
]

botoes_normais = []
botoes_operadores = []

x = 20
y = 170

for texto, comando in botoes:
    if texto == "=":
        btn = tk.Button(janela, text=texto, font=("Arial", 20),
                        relief="flat", command=comando)
        btn.place(x=x, y=y, width=152, height=60)
        botoes_operadores.append(btn)
        continue

    btn = tk.Button(janela, text=texto, font=("Arial", 18),
                    relief="flat", command=comando)

    btn.place(x=x, y=y, width=70, height=60)

    # operador = cor diferente
    if texto in ["clr", "DEL", "%", "/", "*", "-", "+"]:
        botoes_operadores.append(btn)
    else:
        botoes_normais.append(btn)

    x += 80
    if x > 270:
        x = 20
        y += 70

aplicar_tema()

janela.mainloop()
