# Com Pygame
import pygame
import random
import sys

# --- Configurações Básicas ---
pygame.init()
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Adivinhação")
fonte = pygame.font.SysFont("Arial", 32)
BRANCO, PRETO, AZUL = (255,255,255), (0,0,0), (50,150,255)

class Jogo:
    def __init__(self):
        self.reiniciar()
        self.modo = None # 'USER' ou 'COMP'

    def reiniciar(self):
        self.alvo = random.randint(1, 100)
        self.tentativas, self.input_texto = 0, ""
        self.feedback, self.fim_de_jogo = "", False

    def desenhar_texto(self, texto, y, cor=PRETO):
        img = fonte.render(texto, True, cor)
        tela.blit(img, img.get_rect(center=(LARGURA//2, y)))

    def loop_principal(self):
        while True:
            tela.fill(BRANCO)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); sys.exit()
                
                # Seleção de modo
                if not self.modo and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1: self.modo = 'USER'
                    if event.key == pygame.K_2: self.modo = 'COMP'
                
                # Entrada do usuário (simplificado)
                elif self.modo == 'USER' and not self.fim_de_jogo and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and self.input_texto:
                        chute = int(self.input_texto)
                        self.tentativas += 1
                        if chute > self.alvo: self.feedback = "Muito alto"
                        elif chute < self.alvo: self.feedback = "Muito baixo"
                        else: self.feedback = "Acertou!"; self.fim_de_jogo = True
                        self.input_texto = ""
                    elif event.unicode.isdigit(): self.input_texto += event.unicode
                    elif event.key == pygame.K_BACKSPACE: self.input_texto = self.input_texto[:-1]

            # Renderização (simplificado)
            if not self.modo:
                self.desenhar_texto("[1] Modo Usuário | [2] Modo PC", 300)
            else:
                self.desenhar_texto(f"Alvo: {self.alvo} (DEBUG)", 100)
                self.desenhar_texto(f"Palpite: {self.input_texto}", 250, AZUL)
                self.desenhar_texto(f"Feedback: {self.feedback}", 350)
                if self.fim_de_jogo: self.desenhar_texto("Pressione R para reiniciar", 450)

            if pygame.key.get_pressed()[pygame.K_r]: self.__init__()
            pygame.display.flip()

if __name__ == "__main__": Jogo().loop_principal()
