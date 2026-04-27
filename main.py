# Configuração da tela
import turtle 

screen = turtle.Screen()
screen.title("Jogo da velha - Turtle")
screen.setup(width=600, height=600)
screen.setworldcoordinates(0,0,3,3) 
#Olha 
# Desenhar Tabuleiro
t= turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(5)

def draw_grid():
    # Linhas Verticais
    for i in range(1,3):
        t.pu()
        t.goto(i,0)
        t.pd()
        t.goto(i,3)
    # Linhas Horizontais
    for i in range(1,3):
        t.pu()
        t.goto(0,i)
        t.pd()
        t.goto(3,i)
draw_grid()

# Lógica do jogo
board= [[' ' for _ in range(3)]for _ in range(3)]
turn= 'X'
game_over = False
def draw_x(x,y):
    t.pu()
    t.goto(x+0.2, y+0.2)
    t.pd()
    t.goto(x+0.8, y+0.8)
    t.pu()
    t.goto(x+0.2, y+0.8)
    t.pd()
    t.goto(x+0.8, y+0.2)

def draw_o(x,y):
    t.pu()
    t.goto(x+0.5, y+0.1)
    t.pd()
    t.circle(0.4, steps=100)

def check_winner():
    # Lógica simplificada de verificação
    for i in range(3):
        if board[i][0] == board[i][1]== board[i][2] != '': return board[i][0]
        if board[0][i] == board[1][i]== board[2][i] != '': return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] != '': return board[0][0]            
        if board[0][2] == board[1][1] == board[2][0] != '': return board[0][2]
    return None

def click(x,y):
    global turn, game_over
    if game_over:  
        return
    # Converter coordenadas do clipe para índice da lista
    row = int(y)
    col = int(x)

    if 0 <= row < 3 and 0 <= col <3 and board[row][col] == '':
        board[row][col] = turn
        if turn == 'X':
            draw_x(col,row)
            turn = 'O'
        else:
            draw_o(col,row)
            turn = 'X'
        winner = check_winner()
        if winner:
            print(f"Jogador {winner} venceu!")
            game_over = True
        elif all(all(cell != '' for cell in linha) for row in board):
            print("Empate!")
            game_over = True


screen.onscreenclick(click)
turtle.mainloop()
