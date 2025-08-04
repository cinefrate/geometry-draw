import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("geometry draw")

def draw_rectangle (height, width, x, y):

    for i in range (y-int(height/2), y+int(height/2)):
        for j in range (x-int(width/2), x+int(width/2)):
                if i==y-int(height/2) or j==x-int(width/2) or i==y+int(height/2)-1 or j==x+int(width/2)-1:
                    screen.set_at((j, i), pygame.Color(255, 30, 30))
                else:
                     screen.set_at((j, i), pygame.Color(30, 30, 30))


            

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_rectangle(100, 100, 50,  50)
    pygame.display.flip()

pygame.quit()