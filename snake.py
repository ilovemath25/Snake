import pygame
from src.codehh import Snake
pygame.init()
win = pygame.display.set_mode((880,600))
pygame.display.set_caption("snake")
fps = pygame.time.Clock()
run = True
shake = delay = 1
highscore = 0
in_start = True
in_game = in_retry = False
font = pygame.font.SysFont('comicsan',50,True)
snake = Snake()
win.blit(pygame.image.load('image/bg.jpg'),(0,0))
win.blit(pygame.image.load('image/bg_path.png'),(0,0))
win.blit(pygame.image.load('image/start_menu_bg.png'),(0,0))
win.blit(pygame.image.load('image/start_menu.png'),(0,0))
win.blit(font.render('Highscore : '+str(highscore),1,(255,255,255)),(355,275))
while run:
   fps.tick(30)
   if in_start:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:run = False
         if event.type == pygame.KEYDOWN:
            win.blit(pygame.image.load('image/bg.jpg'),(0,0))
            win.blit(pygame.image.load('image/bg_path.png'),(0,0))
            win.blit(pygame.image.load('image/start_menu_bg.png'),(0,0))
            win.blit(pygame.image.load('image/start_menu_active.png'),(0,0))
            win.blit(font.render('Highscore : '+str(highscore),1,(255,255,255)),(355,275))
         if event.type == pygame.KEYUP:
            in_start = False
            in_game = True
   elif in_game:
      if snake.gameover:
         if shake==3:shake=0
         elif shake!=0:shake+=1
         for event in pygame.event.get():
            if event.type == pygame.QUIT:run = False
         snake.walk(win,1,shake)
         delay+=1
         if delay==40:
            in_retry = True
            in_game = False
            if snake.score>highscore:highscore = snake.score
      elif snake.win:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:run = False
         delay+=1
         if delay==40:
            in_retry = True
            in_game = False
            if snake.score>highscore:highscore = snake.score
      else:
         snake.key()
         snake.eat()
         snake.hitwall()
         snake.walk(win,0,0)
      win.blit(font.render('Score :',1,(255,255,255)),(650,150))
      win.blit(font.render(str(snake.score),1,(255,255,255)),(650,200))
      win.blit(font.render('Highscore :',1,(255,255,255)),(650,250))
      win.blit(font.render(str(highscore),1,(255,255,255)),(650,300))
      run = snake.run
   elif in_retry:
      if delay==40:
         win.blit(pygame.image.load('image/start_menu_bg.png'),(0,0))
         win.blit(pygame.image.load('image/retry.png'),(0,0))
         win.blit(font.render('Highscore : '+str(highscore),1,(255,255,255)),(355,275))
         delay+=1
      for event in pygame.event.get():
         if event.type == pygame.QUIT:run = False
         if event.type == pygame.KEYDOWN:
            win.blit(pygame.image.load('image/retry_active.png'),(0,0))
            win.blit(font.render('Highscore : '+str(highscore),1,(255,255,255)),(355,275))
         if event.type == pygame.KEYUP:
            snake.reset()
            shake = delay = 1
            in_start = False
            in_game = True
   pygame.display.update()
pygame.quit()