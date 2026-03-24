from turtle import *
from time import sleep

t = Turtle()

t.speed(5)

def main():
    # Bandeiras fáceis
    # Holanda/Países Baixos 25xp
    retangulo(-450, 300, 900, 200, '#ae1c28')
    retangulo(-450, 100, 900, 200, '#ffffff')
    retangulo(-450, -100, 900, 200, '#21468b')
    base()

    # França 25xp
    retangulo(-450, 300, 300, 600, '#0055A4')
    retangulo(-150, 300, 300, 600, '#ffffff')
    retangulo(150, 300, 300, 600, '#ce2b37')
    base()

    # Bandeiras médias
    # Gana 50xp
    retangulo(-450, 300, 900, 200, '#ce1126')
    retangulo(-450, 100, 900, 200, '#fcd116')
    retangulo(-450, -100, 900, 200, '#006b3f')
    estrela(-100, 25, 75, 'black')
    base()

    # Cuba 50xp
    for i in range(5):
        if (i % 2 == 0):
            color = '#002a8f'
        else:
            color = '#ffffff'
        retangulo(-450, 300-(i*120), 900, 120, color)
    triangulo(-450, 300, 600, '#cb1515')
    estrela(-350, 25, 75, '#ffffff')
    base()
    
  
    # Bandeira Costa Rica 50xp 

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

    # Reino Unido
    t.pu()
    t.goto(-65, 300)
    t.pd()
    t.color('#ff0000')
    t.begin_fill()
    def  des_ret(t, x, y, largura, altura, cor):
        t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(cor)
    t.begin_fill()
    for _ in range(2):
        t.forward(largura)
        t.right(90)
        t.forward(altura)
        t.right(90)
    t.end_fill()
    def des_linha_vert(t, x1, y1, x2, y2, largura, cor):
    
           t.pu()
           t.goto(x1, y1)
           t.pd()
           t.pensize(largura)
           t.color(cor)
           t.goto(x2, y2)

    

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
mainloop()


