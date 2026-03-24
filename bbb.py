from turtle import *
from time import sleep
import turtle

# ========== CONFIGURAÇÃO GLOBAL ========== 
screen = turtle.Screen()
screen.setup(width=800, height=600)
t = turtle.Turtle()
t.hideturtle()

# ========== BANDEIRA COSTA RICA (50xp) ========== 
def bandeira_costa_rica():
    
    screen.title("Bandeira Costa Rica")
    screen.bgcolor("white")
    t.speed(5)
    
    altura_total = 200
    largura_total = 300
    largura_faixa = altura_total / 6
    
    def desenhar_faixa(cor, y):
        t.pu()
        t.goto(-largura_total/2, y)
        t.pd()
        t.color(cor)
        t.begin_fill()
        for _ in range(2):
            t.forward(largura_total)
            t.right(90)
            t.forward(largura_faixa)
            t.right(90)
        t.end_fill()
    
    # Desenhar as faixas na ordem correta
    desenhar_faixa("#0034a3", 100)
    desenhar_faixa("white", 100 - largura_faixa)
    desenhar_faixa("#dc202c", 100 - 2 * largura_faixa)
    desenhar_faixa("#dc202c", 100 - 3 * largura_faixa)
    desenhar_faixa("white", 100 - 4 * largura_faixa)
    desenhar_faixa("#0030BF", 100 - 5 * largura_faixa)
    
    sleep(3)

# ========== BANDEIRA BRASIL (25xp) ========== 
def bandeira_brasil():
    
    screen.clear()
    screen.title("Bandeira do Brasil")
    screen.bgcolor("white")
    t.speed(5)
    
    # 1. Retângulo Verde
    t.pu()
    t.goto(-200, 120)
    t.pd()
    t.color("#009440")  # Verde oficial
    t.begin_fill()
    for _ in range(2):
        t.forward(400)
        t.right(90)
        t.forward(240)
        t.right(90)
    t.end_fill()
    
    # 2. Losango Amarelo
    t.pu()
    t.goto(0, 100)
    t.pd()
    t.color("#ffcb00")
    t.begin_fill()
    t.goto(180, 0)
    t.goto(0, -100)
    t.goto(-180, 0)
    t.goto(0, 100)
    t.end_fill()
    
    # 3. Círculo Azul
    t.pu()
    t.goto(0, -70)
    t.setheading(0)
    t.pd()
    t.color("#002776")
    t.begin_fill()
    t.circle(70)
    t.end_fill()
    
    sleep(3)

# ========== BANDEIRA HOLANDA (25xp) ========== 
def bandeira_holanda():
    """Desenha a bandeira da Holanda com três faixas horizontais"""
    screen.clear()
    screen.title("Bandeira Holanda")
    screen.bgcolor("white")
    t.speed(5)
    
    cores = ["#AE1C28", "white", "#21468B"]  # Vermelho, Branco, Azul
    largura = 300
    altura = 100
    
    for i, cor in enumerate(cores):
        t.pu()
        t.goto(-largura/2, 150 - (i * altura))
        t.pd()
        t.color(cor)
        t.begin_fill()
        for _ in range(2):
            t.forward(largura)
            t.right(90)
            t.forward(altura)
            t.right(90)
        t.end_fill()
    
    sleep(3)

# ========== BANDEIRA EMIRADOS ÁRABES (50xp) ========== 
def bandeira_emirados():
    """Desenha a bandeira dos Emirados Árabes Unidos"""
    screen.clear()
    screen.title("Bandeira dos Emirados Árabes Unidos")
    screen.bgcolor("white")
    t.speed(5)
    
    def draw_retangulo(cor, x, y, width, height):
        t.pu()
        t.goto(x, y)
        t.pd()
        t.color(cor)
        t.begin_fill()
        for _ in range(2):
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)
        t.end_fill()
    
    # Dimensões
    altura = 200
    largura = 400
    strip_largura = largura * 0.75
    red_largura = largura * 0.25
    strip_altura = altura / 3
    
    # 1. Faixa Vertical Vermelha
    draw_retangulo("#FF0000", -largura/2, -altura/2, red_largura, altura)
    
    # 2. Faixa Horizontal Verde
    draw_retangulo("#00732F", -largura/2 + red_largura, altura/2 - strip_altura, strip_largura, strip_altura)
    
    # 3. Faixa Horizontal Branca
    draw_retangulo("#FFFFFF", -largura/2 + red_largura, -strip_altura/2, strip_largura, strip_altura)
    
    # 4. Faixa Horizontal Preta
    draw_retangulo("#000000", -largura/2 + red_largura, -altura/2, strip_largura, strip_altura)
    
    sleep(3)

# ========== BANDEIRA PAQUISTÃO (50xp) ========== 
def bandeira_paquistao():
    """Desenha a bandeira do Paquistão com lua crescente e estrela"""
    screen.clear()
    screen.title("Bandeira do Paquistão")
    screen.bgcolor("white")
    t.speed(3)
    
    # Configurações iniciais
    largura = 600
    altura = 400
    
    # Desenhar o retângulo verde
    t.pu()
    t.goto(-largura/2, altura/2)
    t.pd()
    t.color("#004037")  # Verde escuro
    t.begin_fill()
    for _ in range(2):
        t.forward(largura)
        t.right(90)
        t.forward(altura)
        t.right(90)
    t.end_fill()
    
    # Desenhar a faixa branca
    t.pu()
    t.goto(-largura/2, altura/2)
    t.pd()
    t.color("white")
    t.begin_fill()
    for _ in range(2):
        t.forward(largura/4)  # 1/4 da largura
        t.right(90)
        t.forward(altura)
        t.right(90)
    t.end_fill()
    
    # Desenhar a Lua Crescente (Crescent)
    t.pu()
    t.goto(50, 60)
    t.pd()
    t.color("white")
    t.begin_fill()
    t.circle(70)
    t.end_fill()
    
    # Desenhar o círculo para "apagar" a lua (fazer o efeito crescente)
    t.pu()
    t.goto(75, 75)
    t.color("#004037")  # Cor de fundo verde
    t.begin_fill()
    t.circle(70)
    t.end_fill()
    
    # Desenhar a Estrela
    t.pu()
    t.goto(100, 30)
    t.pd()
    t.color("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(50)
        t.right(144)
    t.end_fill()
    
    sleep(3)

# ========== BANDEIRA TURQUIA (50xp) ========== 
def bandeira_turquia():
    """Desenha a bandeira da Turquia com lua e estrela"""
    screen.clear()
    screen.title("Bandeira da Turquia")
    screen.bgcolor("white")
    t.speed(3)
    
    # Configurações iniciais
    largura = 600
    altura = 400
    screen.setup(largura, altura)
    screen.bgcolor("red")  # Fundo Vermelho
    
    # Desenhar a Lua Crescente
    t.pu()
    t.goto(-100, -80)
    t.pd()
    t.color("white")
    t.begin_fill()
    t.circle(80)  # Círculo externo
    t.end_fill()
    
    t.pu()
    t.goto(-70, -60)
    t.pd()
    t.color("red")
    t.begin_fill()
    t.circle(60)  # Círculo interno para fazer a lua
    t.end_fill()
    
    # Desenhar a Estrela
    t.pu()
    t.goto(50, 0)
    t.pd()
    t.color("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(80)
        t.right(144)
    t.end_fill()
    
    sleep(3)

# ========== BANDEIRA NORUEGA (50xp) ========== 
def bandeira_noruega():
    """Desenha a bandeira da Noruega com cruz"""
    screen.clear()
    screen.title("Bandeira da Noruega")
    screen.bgcolor("white")
    t.speed(5)
    
    def draw_retangulo_norway(cor, largura, altura):
        t.begin_fill()
        t.color(cor)
        for _ in range(2):
            t.forward(largura)
            t.right(90)
            t.forward(altura)
            t.right(90)
        t.end_fill()
    
    # Dimensões
    largura = 220
    altura = 160
    
    # 1. Fundo Vermelho
    t.pu()
    t.goto(-110, 80)
    t.pd()
    draw_retangulo_norway("#BA0C2F", largura, altura)  # Vermelho Norueguês
    
    # 2. Cruz Branca (Horizontal e Vertical)
    
    # Horizontal Branca
    t.pu()
    t.goto(-110, 20)
    t.pd()
    draw_retangulo_norway("white", largura, 40)
    
    # Vertical Branca
    t.pu()
    t.goto(-30, 80)
    t.pd()
    draw_retangulo_norway("white", 40, altura)
    
    # 3. Cruz Azul (Horizontal e Vertical)
    
    # Horizontal Azul
    t.pu()
    t.goto(-110, 10)
    t.pd()
    draw_retangulo_norway("#00205B", largura, 20)  # Azul Norueguês
    
    # Vertical Azul
    t.pu()
    t.goto(-20, 80)
    t.pd()
    draw_retangulo_norway("#00205B", 20, altura)
    
    sleep(3)

# ========== BANDEIRA ISLÂNDIA (50xp) ========== 
def bandeira_islandia():
    """Desenha a bandeira da Islândia com cruzes"""
    screen.clear()
    screen.title("Bandeira da Islândia")
    screen.bgcolor("white")
    t.speed(3)
    
    def draw_retangulo_iceland(cor, largura, altura, x, y):
        t.pu()
        t.goto(x, y)
        t.pd()
        t.color(cor)
        t.begin_fill()
        for _ in range(2):
            t.forward(largura)
            t.right(90)
            t.forward(altura)
            t.right(90)
        t.end_fill()
    
    # Fundo Azul
    draw_retangulo_iceland("#0048E0", 600, 400, -300, 200)
    
    # Cruz Branca
    draw_retangulo_iceland("white", 600, 100, -300, 50)
    draw_retangulo_iceland("white", 100, 400, -100, 200)
    
    # Cruz Vermelha
    draw_retangulo_iceland("#D72828", 600, 50, -300, 25)
    draw_retangulo_iceland("#D72828", 50, 400, -75, 200)
    
    sleep(3)

# ========== BANDEIRA ÁFRICA DO SUL (75xp) ========== 
def bandeira_africa_do_sul():
    """Desenha a bandeira da África do Sul"""
    screen.clear()
    screen.title("Bandeira da África do Sul")
    screen.bgcolor("white")
    t.speed(5)
    
    def desenhar_retangulo_safrica(cor, x, y, largura, altura):
        t.pu()
        t.goto(x, y)
        t.pd()
        t.color(cor)
        t.begin_fill()
        for _ in range(2):
            t.forward(largura)
            t.left(90)
            t.forward(altura)
            t.left(90)
        t.end_fill()
    
    def desenhar_poligono_safrica(cor, pontos):
        t.pu()
        t.goto(pontos[0])
        t.pd()
        t.color(cor)
        t.begin_fill()
        for ponto in pontos[1:]:
            t.goto(ponto)
        t.goto(pontos[0])
        t.end_fill()
    
    # Cores aproximadas (RGB/Hex)
    VERMELHO = "#E23D28"
    AZUL = "#002395"
    VERDE = "#007749"
    AMARELO = "#FFB81C"
    PRETO = "#000000"
    BRANCO = "#FFFFFF"
    
    # 1. Fundo/Base (Vermelho em cima, Azul embaixo)
    desenhar_retangulo_safrica(VERMELHO, -300, 0, 600, 200)
    desenhar_retangulo_safrica(AZUL, -300, -200, 600, 200)
    
    # 2. Faixa Branca (Base para o Y verde)
    pontos_branco = [(-300, 200), (-300, -200), (0, 0), (600, 0), (600, 60), (60, 60), (-240, 260)]
    
    # 3. Faixa Verde (Formato em Y)
    desenhar_poligono_safrica(VERDE, [(-300, 100), (0, 0), (600, 0), (600, -60), (0, -60), (-300, -260), (-300, -180), (-80, 0), (-300, 180)])
    
    # 4. Triângulo Preto e bordas Amarelas
    desenhar_poligono_safrica(AMARELO, [(-300, 120), (-160, 0), (-300, -120)])
    desenhar_poligono_safrica(PRETO, [(-300, 100), (-180, 0), (-300, -100)])
    
    sleep(3)

# ========== BANDEIRA COREIA DO NORTE (75xp) ========== 
def bandeira_coreia_do_norte():
    """Desenha a bandeira da Coreia do Norte"""
    screen.clear()
    screen.title("Bandeira da Coreia do Norte")
    screen.bgcolor("white")
    t.speed(3)
    
    def desenhar_retangulo_nkorea(cor, largura, altura):
        t.begin_fill()
        t.fillcolor(cor)
        for _ in range(2):
            t.forward(largura)
            t.right(90)
            t.forward(altura)
            t.right(90)
        t.end_fill()
    
    def desenhar_estrela_nkorea(cor, tamanho):
        t.begin_fill()
        t.fillcolor(cor)
        for _ in range(5):
            t.forward(tamanho)
            t.right(144)
        t.end_fill()
    
    # Cores
    vermelho = "#ED1C27"
    azul = "#024FA2"
    branco = "#FFFFFF"
    
    # Dimensões (proporção aproximada)
    largura = 300
    altura = 200
    
    # Desenhar faixa azul superior
    t.pu()
    t.goto(-150, 100)
    t.pd()
    desenhar_retangulo_nkorea(azul, largura, altura/3)
    
    # Desenhar faixas brancas
    t.pu()
    t.goto(-150, 100 - altura/3)
    t.pd()
    desenhar_retangulo_nkorea(branco, largura, 10)
    
    t.pu()
    t.goto(-150, -100 + altura/3 + 10)
    t.pd()
    desenhar_retangulo_nkorea(branco, largura, 10)
    
    # Desenhar faixas vermelhas
    t.pu()
    t.goto(-150, 100 - altura/3 - 10)
    t.pd()
    desenhar_retangulo_nkorea(vermelho, largura, altura/3 - 10)
    
    t.pu()
    t.goto(-150, -100 + altura/3)
    t.pd()
    desenhar_retangulo_nkorea(vermelho, largura, altura/3 - 10)
    
    # Desenhar círculo branco
    t.pu()
    t.goto(0, -40)
    t.pd()
    t.color(branco)
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    
    # Desenhar estrela vermelha
    t.pu()
    t.goto(-25, 5)
    t.pd()
    t.color(vermelho)
    desenhar_estrela_nkorea(vermelho, 50)
    
    sleep(3)

# ========== BANDEIRA CANADÁ (200xp - Desafio) ==========
def bandeira_canada():

    screen.clear()
    screen.title("Bandeira do Canadá")
    screen.bgcolor("white")
    t.speed(3)
    
    def draw_rectangle_canada(cor, largura, altura):
        t.begin_fill()
        t.fillcolor(cor)
        for _ in range(2):
            t.forward(largura)
            t.right(90)
            t.forward(altura)
            t.right(90)
        t.end_fill()
    
    # Desenhar faixas vermelhas e branca
    draw_rectangle_canada("red", 100, 300)
    t.forward(100)
    draw_rectangle_canada("white", 200, 300)
    t.forward(200)
    draw_rectangle_canada("red", 100, 300)
    
    # Desenhar folha
    t.pu()
    t.goto(0, 0)
    t.pd()
    t.color("red")
    t.begin_fill()
    t.speed(3)
    t.left(90)
    
    # Desenho da folha 
    t.forward(100)
    
    # Lado esquerdo
    t.right(120)
    t.forward(30)
    t.left(120)
    t.forward(30)
    t.right(120)
    t.forward(30)
    t.left(120)
    t.forward(30)
    t.right(120)
    t.forward(30)
    
    # Topo
    t.left(150)
    t.forward(40)
    t.right(150)
    t.forward(40)
    
    # Lado direito
    t.left(120)
    t.forward(30)
    t.right(120)
    t.forward(30)
    t.left(120)
    t.forward(30)
    t.right(120)
    t.forward(30)
    t.left(120)
    t.forward(30)
    
    t.right(120)
    t.forward(100)
    
    # Base/Caule
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    
    t.end_fill()
    
    sleep(3)

mainloop()