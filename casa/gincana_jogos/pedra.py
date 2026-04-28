# Jogo de Pedra, Papel, Tesoura

import random

def jogar():
    pontos = 0
    
    while True:
        opcoes = ["pedra", "papel", "tesoura"]
        computador = random.choice(opcoes)
        
        jogador = input("\nEscolha pedra, papel ou tesoura: ").lower()
        
        if jogador not in opcoes:
            print("Escolha inválida!")
            continue

        print(f"Computador escolheu: {computador}")

        # Lógica de vitória/derrota/empate
        if jogador == computador:
            print("Empate!")
        elif (jogador == "pedra" and computador == "tesoura") or \
             (jogador == "tesoura" and computador == "papel") or \
             (jogador == "papel" and computador == "pedra"):
            print("Você venceu!")
            pontos += 1
        else:
            print("Você perdeu!")

        print(f"Sua pontuação: {pontos}")

        # Reiniciar o jogo
        denovo = input("Deseja jogar novamente? (s/n): ").lower()
        if denovo != 's':
            print(f"\nJogo encerrado. Pontuação final: {pontos}")
            break

jogar()
