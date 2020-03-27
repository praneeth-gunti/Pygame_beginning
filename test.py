import pygame

x = 100
y = 300
width = 10
height = 20
vel = 5
run = True
win_height = 500
win_width = 500
jump = False
jumpHeight = 10
trace = False

pygame.init()
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Wanna Play")

while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    n = pygame.key.get_pressed()
    if n[pygame.K_RIGHT] and x < win_width - width - vel:
        x += vel
    if n[pygame.K_LEFT] and x > vel:
        x -= vel
    if not jump:
        if n[pygame.K_UP] and y > vel:
            y -= vel
        if n[pygame.K_DOWN] and y < win_height - height - vel:
            y += vel
        if n[pygame.K_SPACE]:
            jump = True
    else:

        if jumpHeight >= -10:
            rev = 1
            if jumpHeight < 0:
                rev = -1
            y -= (jumpHeight ** 2) * 0.5 * rev
            jumpHeight -= 1
        else:
            jump = False
            jumpHeight = 10
    if not trace:
        win.fill((0, 0, 0))
    if n[pygame.K_t]:
        trace = not trace
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
pygame.quit()