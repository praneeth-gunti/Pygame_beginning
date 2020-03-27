import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("first game")

x = 50
y = 50
width = 40
height = 60
vel = 10
run = True

isJump = False
jumpCount = 10

while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    n = pygame.key.get_pressed()

    if n[pygame.K_LEFT] and x > vel:
        x -= vel
    if n[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
    if not isJump:
        if n[pygame.K_UP] and y > vel:
            y -= vel
        if n[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel
        if n[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()