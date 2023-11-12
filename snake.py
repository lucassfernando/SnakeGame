import pygame
import random



pygame.init()

resolucao = (500, 500)
screen = pygame.display.set_mode(resolucao)
dark_mode = (0, 0, 0)
screen.fill(dark_mode)

class Snake:
    cor = (255, 255, 255)
    tamanho = (10, 10)

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)

        self.corpo = [(100, 100), (90, 100), (80, 100)]

    def blit(self, screen):
        for posicao in self.corpo:
            screen.blit(self.textura, posicao)


class Frutinha():
    cor  = (255, 0, 0)
    tamanho = (10, 10)

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)
        self.posicao = (random.randint(0, 49) * 10, random.randint(0, 49) * 10)

    def blit(self, screen):
        screen.blit(self.textura, self.posicao)

frutinha = Frutinha()
snake = Snake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    frutinha.blit(screen)
    snake.blit(screen)
    pygame.display.update()



    