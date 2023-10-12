import pygame 
from sys import exit

pygame.init()
#Create UI size
screen = pygame.display.set_mode((600,700))
#Create UI title
pygame.display.set_caption('My game')
#FPS(Ceiling)
#FPS Cap
clock = pygame.time.Clock()


def background_Image():
  #BG image
  ground_surface =pygame.image.load('PyGame\graphics\Track.jpeg')
  imageSize_ground_Surface = (595,345)
  ground_surface = pygame.transform.scale(ground_surface,imageSize_ground_Surface)
  screen.blit(ground_surface,(2.5, 2.5))

def background_Image2():
  #BG image
  ground_surface =pygame.image.load('PyGame\graphics\Track.jpeg')
  imageSize_ground_Surface = (595,350)
  ground_surface = pygame.transform.scale(ground_surface,imageSize_ground_Surface)
  screen.blit(ground_surface,(2.5, 347.5))

def app():
  while True: 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()

    pygame.display.flip()

    pygame.display.update()
    clock.tick(60)
    background_Image()
    background_Image2()

app()