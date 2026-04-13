from pygame import *
import sys

init()

running = True

clock = time.Clock()
 
f_image = image.load("fairy.png")
f_imgae = transform.scale(f_image, (100,90))
z_image = image.load("zeref.png")
z_image = transform.scale(z_image,(100,201))

fai_font = font.Font("CROWNT.TTF",25)

mixer.music.load("musicaf.mp3")
mixer.music.play(-1)


window = display.set_mode((1280, 720))

window.fill((25,25,112))
# Variaveis
x_nuvem = 0
x_nuvem2 = 900
bg_color = ((135,206,235))


while running:
    clock.tick(60)

    for ev in event.get():
        if ev.type == QUIT:
            running = False
        if ev.type == KEYDOWN:
            key_pressed = ev.key
            if key_pressed == K_SPACE:
                bg_color = (25,25,132)

    
    # Update
    dt = clock.get_time()/1000
    keys = key.get_pressed()
    
    # Teclas para movimentação
    if keys[K_d]:
        x_nuvem = x_nuvem + 100 * dt
        x_nuvem2 = x_nuvem2 + 100 * dt
    elif keys[K_a]:   
        x_nuvem = x_nuvem - 100 * dt
        x_nuvem2 = x_nuvem2 - 100 * dt

    
    
    

    # Draw
    window.fill(bg_color) # Cor de fundo
    # Casa
    draw.rect(window, (0,0,0),(0,600,1280,120)) # Chão
    draw.rect(window, (128,128,128),(1000,300,50,300) ) # Poste Luz
    draw.line(window, (128,128,128),(1000,304),(900,304),10) # Vara do poste
    draw.circle(window,(255,242,81),(900,310),15) 
    draw.rect(window, (255,250,250),(200,300,300,300)) # Casa em si
    draw.rect(window, (165,42,42), (350,450,100,150)) # Porta
    draw.rect(window, (0,0,0), (230,399,70,90)) # Janela
    draw.line(window, (229,228,226), (265, 400), (265,489), 2) # Grade janela 1 
    draw.line(window, (229,228,226), (300, 450), (230,450), 2) # Grade janela 2
    draw.polygon(window,(242,136,59),((200,300),(350,200),(500,300))) # laje
    draw.circle(window,(248,248,255),(700,60),50 )       
   
    # Desenhar Imagem (Tiradas da internet)

    window.blit(f_imgae,(300,210))
    window.blit(z_image,(600,400))

    ft_text = fai_font.render("Mundo da Magia",True,(0,0,0))
    window.blit(ft_text,(290,340))

    # Nuvem
    # Posição inicial da nuvem
    y_nuvem = 200
    y_nuvem2 = 200
    
    # Nuvem em movimento
    draw.circle(window, (164,174,179), (x_nuvem, y_nuvem), 30)
    draw.circle(window, (164,174,179), (x_nuvem+30, y_nuvem), 30)
    draw.circle(window, (164,174,179), (x_nuvem+60, y_nuvem), 30)
    draw.circle(window,(164,174,179), (x_nuvem+30, y_nuvem-30), 30)

    # Atualizar posição da nuvem
    x_nuvem = x_nuvem + 0.1
    if x_nuvem > 640: 
        x_nuvem = 0
    
    # Nuvem 2
    # Posição inicial da nuvem
    y_nuvem = 200
    y_nuvem2 = 200
    
    # Nuvem em movimento
    draw.circle(window, (164,174,179), (x_nuvem2, y_nuvem2), 30)
    draw.circle(window, (164,174,179), (x_nuvem2-30, y_nuvem2), 30)
    draw.circle(window, (164,174,179), (x_nuvem2-60, y_nuvem2), 30)
    draw.circle(window,(164,174,179), (x_nuvem2-30, y_nuvem2-30), 30)
    # Atualizar posição da nuvem 2
    x_nuvem2 = x_nuvem2 + 0.1
    if x_nuvem2 > 1280: 
        x_nuvem2 = 640


    
    
    
    display.update()