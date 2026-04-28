# Jogo da Forca

import random

print("--- JOGO DA FORCA ---")
print("--- Tema: Oceano ---")
def jogo_forca():
    palavras = ["pacifico", "indico", "mar", "marisco", "tubarao", "coral", "onda", "peixe", "golfinho", "baleia"]
    palavra = random.choice(palavras)
    letras_descobertas = set()
    tentativas = 6

    while tentativas > 0:
        display_palavra = " ".join([letra if letra in letras_descobertas else "_" for letra in palavra])
        print(f"\nPalavra: {display_palavra}")
        print(f"Tentativas restantes: {tentativas}")

        chute = input("Digite uma letra: ").lower()
        
        if chute in letras_descobertas:
            print("Você já tentou essa letra!")
            

        if chute in palavra:
            letras_descobertas.add(chute)
            print("Boa! Você acertou uma letra.")
        else:
            tentativas -= 1
            print("Ops! Letra errada.")

        if all(letra in letras_descobertas for letra in palavra):
            print(f"Parabéns! Você descobriu a palavra: {palavra}")
        chute1 = input("Digite a palavra completa (ou Enter para pular): ").lower()
        if chute1 == palavra:
            print(f"Parabéns! Você descobriu a palavra: {palavra}")
            return
            
    else:
        print(f"Game Over! A palavra era: {palavra}")
jogo_forca()