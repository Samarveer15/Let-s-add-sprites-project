import pygame

pygame.init()

window_size = (640, 480)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("My first game screen")

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

rect1 = pygame.Rect(100, 100, 50, 50)
rect2 = pygame.Rect(300, 200, 50, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        rect1.x -= .5
    if keys[pygame.K_RIGHT]:
        rect1.x += .5
    if keys[pygame.K_UP]:
        rect1.y -= .5
    if keys[pygame.K_DOWN]:
        rect1.y += .5
    
    screen.fill(white)

    pygame.draw.rect(screen, blue, rect1)
    pygame.draw.rect(screen, red, rect2)

    pygame.display.flip()

pygame.quit()
