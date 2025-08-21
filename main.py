import pygame

SCREEN_SIZE=1000

pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("geometry fail")

class BaseShape :
    speedX = 1
    speedY = 1
    x = 2
    y = 2
    size = 50
    def process_physics(self):
        if self.x > SCREEN_SIZE - self.size//2 or self.x < self.size//2:
            self.speedX *= -1
        if self.y > SCREEN_SIZE - self.size//2 or self.y < self.size//2:
            self.speedY *= -1
        self.x+=self.speedX
        self.y+=self.speedY

    def draw(self):
        pass
    def __init__(self, x, y, size, speedX, speedY):
        self.x=x
        self.y=y
        self.size=size
        self.speedX=speedX
        self.speedY=speedY

class Circle(BaseShape):
    def draw(self):
        for i in range (self.x - self.size, self.size+self.x):
            for j in range (self.y - self.size, self.size+self.y):
                if ((i-self.x)**2 + (j-self.y)**2 <= self.size**2):
                    screen.set_at((i, j), pygame.Color(255, 255, 255))

class Square(BaseShape):
    def draw(self):
        x = self.x - self.size // 2
        y = self.y - self.size // 2
        for i in range(x, x + self.size):
            for j in range(y, y + self.size):
                if j == y or i == x or i == x + self.size - 1 or j == y + self.size - 1:
                    screen.set_at((i, j), pygame.Color(60, 33, 33))
                else:
                    screen.set_at((i, j), pygame.Color(255, 255, 255))

shapes: list[BaseShape] = [
    Circle (100, 100, 21, 2, 1),
    Square (100, 100, 40, 4, 2),
    Circle (100, 130, 10, -2, 1)
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(pygame.Color(0, 0, 0))

    for i in shapes:
        i.process_physics()
        i.draw()

    pygame.display.flip()

pygame.quit()
