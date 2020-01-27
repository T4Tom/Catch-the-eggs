import pygame, random, time
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

transparent = (0, 0, 0, 0)
caught = 0

font = pygame.font.SysFont(None, 90)
text = font.render('GAME OVER', True, (255, 0, 0))
textRect = text.get_rect()
textRect.center = (400, 300)

font2 = pygame.font.SysFont(None, 55)




basketImg = pygame.image.load('basket.png')
basketImg = pygame.transform.scale(basketImg, (100, 100))

backgroundImg = pygame.image.load('background.jpg')
backgroundImg = pygame.transform.scale(backgroundImg, (800, 600))

eggImg = pygame.image.load('egg.png')
eggImg = pygame.transform.scale(eggImg, (60, 80))
crackedEggImg = pygame.image.load('crackedegg.png')
crackedEggImg = pygame.transform.scale(crackedEggImg, (80, 80))



def game_loop():
  done = False

  basketx = 350
  baskety = 400

  random1 = random.randint(1, 740)
  eggx = random1
  eggy = -100
  caught = 0


  while not done:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        exit()
      if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and basketx + 100 < 800:
      basketx += 5
    if pressed[pygame.K_LEFT] and basketx > 0:
      basketx -= 5

    text2 = font2.render('Caught: {0}'.format(caught), True, (0, 0, 0))
    textRect2 = text2.get_rect()
    textRect2.center = (100, 50)
    
    eggy += 3


    screen.blit(backgroundImg, (0, 0))
    screen.blit(eggImg, (eggx, eggy))
    screen.blit(basketImg, (basketx, baskety))
    screen.blit(text2, textRect2)

    if eggy >= 400 and eggx > basketx and eggx + 60 < basketx + 100:
      random2 = random.randint(1, 740)
      eggx = random2
      eggy = -100
      caught += 1
    elif eggy >= 420:
      if eggx < basketx or eggx + 60 > basketx + 100:
        screen.blit(text, textRect)
        screen.blit(crackedEggImg, (eggx, eggy))
        pygame.display.flip()
        time.sleep(5)
        game_loop()

      
    pygame.display.flip()
    clock.tick(60)

game_loop()