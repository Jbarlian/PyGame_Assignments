import pygame


def subok():
    pygame.init()
    height = int(input("Pick Height: "))
    width = int(input("Pick Width: "))
    screen = pygame.display.set_mode((width, height))
    done = False
    is_blue = True
    x = 30
    y = 30

    clock = pygame.time.Clock()

    while not done:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                         done = True
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                         is_blue = not is_blue

            pressed = pygame.key.get_pressed()
            if y > 2:
                if pressed[pygame.K_UP]: y -= 5
            if y < (height-62):
                if pressed[pygame.K_DOWN]: y += 5
            if x > 2:
                if pressed[pygame.K_LEFT]: x -= 5
            if x < (width-62):
                if pressed[pygame.K_RIGHT]: x += 5

            screen.fill((0, 0, 0))
            if is_blue: color = (0, 128, 255)
            else: color = (255, 100, 0)
            pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

            pygame.display.flip()
            clock.tick(60)
subok()




