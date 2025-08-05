import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Geoulia")


def draw_rectan(x, y, height, width):
    x = x - width // 2
    y = y - height // 2
    for i in range(x, x + width):
        for j in range(y, y + height):
            if j == y or i == x or i == x + width - 1 or j == y + height - 1:
                screen.set_at((i, j), pygame.Color(60, 33, 33))
            else:
                screen.set_at((i, j), pygame.Color(255, 255, 255))


speedX = 1
speedY = 2


def process_physics(positionX, positionY, height, width):
    global speedX, speedY
    if positionX > 1000 - width//2 or positionX < width//2:
        speedX *= -1
    if positionY > 1000 - height//2 or positionY < height//2:
        speedY *= -1


positionX = 250
positionY = 250

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(pygame.Color(0, 0, 0))

    draw_rectan(positionX, positionY, 100, 100)
    process_physics(positionX, positionY, 100, 100)
    positionX += speedX
    positionY += speedY

    pygame.display.flip()

pygame.quit()
