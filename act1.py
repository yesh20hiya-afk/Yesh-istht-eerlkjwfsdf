import pygame

pygame.init()
screen = pygame.display.set_mode((400,500))
pygame.display.set_caption("Yesh")

background_image = pygame.transform.scale(pygame.image.load("Yesh.jpg").convert(),(400,500))
y1 = pygame.transform.scale(pygame.image.load("Gemini.jpeg").convert_alpha(),(200,200))
y1_ret = y1.get_rect(center=(200,220))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(background_image,(0,0))
    screen.blit(y1,y1_ret)
pygame.display.flip()

