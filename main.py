import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("geometry draw")

def draw_rectangle (height, width, x, y):

    for i in range (int(y/2), height+int(y/2)):
        for j in range (int(x/2), width+int(x/2)):
                if i==int(y/2) or j==int(x/2) or i==height-1+int(y/2) or j==width-1+int(x/2):
                    screen.set_at((i, j), pygame.Color(255, 30, 30))
                else:
                     screen.set_at((i, j), pygame.Color(30, 30, 30))


            

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_rectangle(500, 500, 0, 0)
    pygame.display.flip()

pygame.quit()