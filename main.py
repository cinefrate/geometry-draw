import pygame

pygame.init()
HEIGHT = 500
WIDTH = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geoulia")


def draw_rectan(x, y, length):
    x = x - length // 2
    y = y - length // 2
    for i in range(x, x + length):
        for j in range(y, y + length):
            if j == y or i == x or i == x + length - 1 or j == y + length - 1:
                screen.set_at((i, j), pygame.Color(60, 33, 33))
            else:
                screen.set_at((i, j), pygame.Color(255, 255, 255))


speedX = 1
speedY = 2


def process_physics(positionX, positionY, HEIGHT, WIDTH):
    global speedX, speedY
    if positionX > WIDTH - 50 or positionX < 50:
        speedX *= -1
    if positionY > HEIGHT - 50 or positionY < 50:
        speedY *= -1


positionX = 250
positionY = 250

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(pygame.Color(0, 0, 0))

    draw_rectan(positionX, positionY, 100)
    process_physics(positionX, positionY, HEIGHT, WIDTH)
    positionX += speedX
    positionY += speedY

    pygame.display.flip()

pygame.quit()
