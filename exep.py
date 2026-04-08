from turtle import *
from time import sleep
import turtle 



# Bandeira Costa Rica 50xp 1

screen = turtle.Screen()
screen.title("Bandeira Costa Rica")
screen.setup(width=600, height=400)
t = Turtle()
t.speed(5)
t.hideturtle()
altura_total=200
largura_total=300
largura_faixa= altura_total / 6

def desenhar_faixa(cor,y):
    t.pu()
    t.goto(-largura_total/2,y)
    t.pd()
    t.color(cor)
    t.begin_fill()
    for _ in range(2):
        t.forward(largura_total)
        t.right(90)
        t.forward(largura_faixa)
        t.right(90)
    t.end_fill()

desenhar_faixa("#0034a3",100)
desenhar_faixa("white",100 - largura_faixa)
desenhar_faixa("#dc202c", 100-2 * largura_faixa)

desenhar_faixa("#dc202c",100-3*largura_faixa)
desenhar_faixa("white",100 - 4 * largura_faixa)
desenhar_faixa("#0030BF", 100 - 5 * largura_faixa)
t.clear()

# Bandeira Brasil 25xp

def desenhar_bandeira():
    screen.title("Bandeira do Brasil")
    t.speed(5)

    # 1. Retângulo Verde
    t.pu()
    t.goto(-200, 120)
    t.pd()
    t.color("#009440") # Verde oficial
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

    t.hideturtle()
       

desenhar_bandeira()
t.clear()

# Bandeira França 25xp

def draw_rectangle(color, width, height):
    
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# Configuração inicial

screen.title("Bandeira da França ")
turtle.speed(5) 

# Faixa Azul
t.pu()
t.goto(-150, 100)
t.pd()
draw_rectangle("#0055A4", 100, 300) 

# Faixa Branca
t.pu()
t.goto(-50, 100)
t.pd()
draw_rectangle("#FFFFFF", 100, 300)

# Faixa Vermelha
t.pu()
t.goto(50, 100)
t.pd()
draw_rectangle("#EF4135", 100, 300) 

# Esconder o cursor e manter a janela aberta
t.hideturtle()

# Bandeira Itália 25xp

def draw_rectangle(color, width, height):
    
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# Configuração inicial

screen.title("Bandeira da Itália ")
t.speed(5) 

# Faixa Azul
t.pu()
t.goto(-150, 100)
t.pd()
draw_rectangle("#009246", 100, 300) 

# Faixa Branca
t.pu()
t.goto(-50, 100)
t.pd()
draw_rectangle("#FFFFFF", 100, 300)

# Faixa Vermelha
t.pu()
t.goto(50, 100)
t.pd()
draw_rectangle("#EF4135", 100, 300) 

# Esconder o cursor e manter a janela aberta
t.hideturtle()
t.clear()
 
t.speed(0)

def main():
    

    

    # Bandeiras médias
    # Gana 50xp
    screen.title("Bandeira Gana")
    retangulo(-450, 300, 900, 200, '#ce1126')
    retangulo(-450, 100, 900, 200, '#fcd116')
    retangulo(-450, -100, 900, 200, '#006b3f')
    estrela(-100, 25, 75, 'black')
    base()

    # Cuba 50xp
    screen.title("Bandeira Cuba")
    for i in range(5):
        if (i % 2 == 0):
            color = '#002a8f'
        else:
            color = '#ffffff'
        retangulo(-450, 300-(i*120), 900, 120, color)
    triangulo(-450, 300, 600, '#cb1515')
    estrela(-350, 25, 75, '#ffffff')
    base()
    

    # Bandeiras difíceis
    # República Centro-Africana 75xp
    retangulo(-450, 300, 900, 150, '#003082')
    retangulo(-450, 150, 900, 150, '#ffffff')
    retangulo(-450, 0, 900, 150, '#289728')
    retangulo(-450, -150, 900, 150, '#ffce00')
    retangulo(-75, 300, 150, 600, '#d21034')
    estrela(-350, 240, 50, '#ffce00')
    base()

    # África do Sul 75xp
    retangulo(-450, 300, 900, 200, '#e03c31')
    retangulo(-450, 100, 900, 200, '#ffffff')
    retangulo(-450, -100, 900, 200, '#001489')
    retangulo(-450, 300, 112.5, 600, '#ffffff')
    triangulo(-337.5, 300, 600, '#ffffff')
    retangulo(-450, 60, 900, 120, '#007749')
    retangulo(-450, 300, 50, 600, '#007749')
    triangulo(-400, 300, 600, '#007749')
    triangulo(-450, 235, 470, '#ffb81c')
    triangulo(-450, 202.5, 405, '#000000')
    base()

    # Geórgia 75xp
    t.pu()
    t.goto(-65, 300)
    t.pd()
    t.color('#ff0000')
    t.begin_fill()
    for _ in range(2):
        t.fd(130)
        t.rt(90)
        t.fd(235)
        t.lt(90)
        t.fd(385)
        t.rt(90)
        t.fd(130)
        t.rt(90)
        t.fd(385)
        t.lt(90)
        t.fd(235)
        t.rt(90)
    t.end_fill()
    cruz(-278, 244, 41)
    cruz(237, 244, 41)
    cruz(-278, -121, 41)
    cruz(237, -121, 41)
    base()

    # Grécia
    for i in range(8):
        if (i % 2 == 0):
            color = '#0d5eaf'
        else:
            color = '#ffffff'
        retangulo(-450, 300-(i*66), 900, 66, color)
    color = '#0d5eaf'
    retangulo(-450, -228, 900, 72, color)
    retangulo(-450, 300, 320, 320, color)
    t.color('#ffffff')
    t.pu()
    t.goto(-323, 300)
    t.pd()
    t.begin_fill()
    for _ in range(2):
        t.fd(66)
        t.rt(90)
        t.fd(132)
        t.lt(90)
        t.fd(127)
        t.rt(90)
        t.fd(66)
        t.rt(90)
        t.fd(127)
        t.lt(90)
        t.fd(132)
        t.rt(90)
    t.end_fill()
    base()


def retangulo(x, y, fd_x, fd_y, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.fd(fd_x)
        t.rt(90)
        t.fd(fd_y)
        t.rt(90)
    t.end_fill()

def cruz(x, y, fd):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    for _ in range(2):
        t.fd(fd)
        t.rt(90)
        t.fd(fd)
        t.lt(90)
        t.fd(fd)
        t.rt(90)
        t.fd(fd)
        t.rt(90)
        t.fd(fd)
        t.lt(90)
        t.fd(fd)
        t.rt(90)
    t.end_fill()

def estrela(x, y, size, color):
    t.pu()
    t.goto(x, y)
    t.color(color)
    t.begin_fill()
    for i in range(5):
        t.fd(size)
        t.left(72)
        t.forward(size)
        t.right(144)
    t.end_fill()

def triangulo(x, y, size, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.color(color)
    t.begin_fill()
    t.rt(30)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.end_fill()
    t.setheading(0)
    
def base():
    t.pu()
    t.color('black')
    t.goto(-450, 300)
    t.pd()
    for _ in range(2):
        t.fd(900)
        t.rt(90)
        t.fd(600)
        t.rt(90)
    
    sleep(5)
    t.clear()


main()


sleep(5)
t.clear()
mainloop()