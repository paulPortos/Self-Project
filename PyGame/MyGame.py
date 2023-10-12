import pygame 
from sys import exit

score = 0
pygame.init()
#Create UI size
screen = pygame.display.set_mode((600,400))
#Create UI title
pygame.display.set_caption('My game')
#FPS(Ceiling)
#FPS Cap
clock = pygame.time.Clock()

#Set background image
def background_Image():
  ground_surface =pygame.image.load('PyGame\graphics\Track.jpeg')
  imageSize_ground_Surface = (595,395)
  ground_surface = pygame.transform.scale(ground_surface,imageSize_ground_Surface)
  r = ground_surface.get_rect()
  r.center = screen.get_rect().center
  #Where to align the image
  screen.blit(ground_surface, r)

def car_Image():
  #Car image
  car = pygame.image.load('PyGame\graphics\car.png')
  imageSize_Car = (90,90)
  car = pygame.transform.scale(car, imageSize_Car)
  s = car.get_rect()
  s.center = screen.get_rect().center
  #Where to align the image
  screen.blit(car, s)

def coin_Image():
  #Car image
    coin = pygame.image.load('PyGame\graphics\obstacle.png')
    imageSize_coin = (70,60)
    coin = pygame.transform.scale(coin, imageSize_coin)
    screen.blit(coin,(230,20))

def score_Text():
  text1_font = pygame.font.Font(None, 30)
  text1_surface = text1_font.render('Car Car Game', False, 'Green')
  screen.blit(text1_surface,(230,15))

def app():
  while True: 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()

    pygame.display.flip()

    pygame.display.update()
    clock.tick(60)

def main():
  background_Image()
  car_Image()
  score_Text()
  coin_Image()
  app()

main()