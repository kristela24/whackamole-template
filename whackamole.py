import pygame
import random
from constants import *

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        #mole start
        mole_x = 0
        mole_y = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                #mole-mouse movement
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    mole_rect = mole_image.get_rect(topleft=(mole_x, mole_y))

                    if mole_rect.collidepoint(mouse_x, mouse_y):
                        # Move mole to random square
                        mole_x = random.randrange(0, 20) * 32
                        mole_y = random.randrange(0, 16) * 32

        #screen
            screen.fill("light blue")
            for x in range(0, 641, 32):  # 640 + 1 to include right edge
                pygame.draw.line(screen, "dark green", (x, 0), (x, 512))
            for y in range(0, 513, 32):  # 512 + 1 to include bottom edge
                pygame.draw.line(screen, "white", (0, y), (640, y))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
#update