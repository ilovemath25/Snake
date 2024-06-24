import pygame
import random
class Snake:
   def __init__(self):
      self.head = [pygame.image.load('image/snake/head.png')]
      self.body = [pygame.image.load('image/snake/body.png'),pygame.image.load('image/snake/tail.png')]
      self.hit = [pygame.image.load('image/snake/hit1.png'),pygame.image.load('image/snake/hit2.png')]
      self.x = 50+4*50
      self.y = 25+5*50
      self.snake_body = [[self.x-(i*6.25),float(self.y),'right','right',False] for i in range(0,14,1)]
      self.xa = 50+8*50
      self.ya = 25+5*50
      self.eatrange = [range(self.xa,self.xa+50),range(self.ya,self.ya+50)]
      self.vel = 6.25
      self.run = True
      self.gameover = self.win = False
      self.state = 'right'
      self.before = self.state
      self.isturn = False
      self.iswalk = False
      self.score = 0
      self.eatcount = 0
      self.temp = [0,0,0,0]
   def reset(self):
      self.head = [pygame.image.load('image/snake/head.png')]
      self.body = [pygame.image.load('image/snake/body.png'),pygame.image.load('image/snake/tail.png')]
      self.hit = [pygame.image.load('image/snake/hit1.png'),pygame.image.load('image/snake/hit2.png')]
      self.x = 50+4*50
      self.y = 25+5*50
      self.snake_body = [[self.x-(i*6.25),float(self.y),'right','right',False] for i in range(0,14,1)]
      self.xa = 50+8*50
      self.ya = 25+5*50
      self.vel = 6.25
      self.run = True
      self.gameover = self.win = False
      self.state = 'right'
      self.before = self.state
      self.isturn = False
      self.iswalk = False
      self.score = 0
      self.eatcount = 0
      self.temp = [0,0,0,0]
   def eat(self):
      eatrange = [range(self.xa,self.xa+50),range(self.ya,self.ya+50)]
      if(self.x+25 in eatrange[0])and(self.y+25 in eatrange[1]):
         self.xa=50+(random.randint(0,10))*50
         self.ya=25+(random.randint(0,10))*50
         snake_cord = [[i[0],i[1]] for i in self.snake_body]
         while [self.xa,self.ya] in snake_cord:
            self.xa=50+(random.randint(0,10))*50
            self.ya=25+(random.randint(0,10))*50
         self.eatcount=1
         self.score+=1
      if(self.score==121):self.win = True
   def hitwall(self):
      if self.x < 50 or self.x>550:self.gameover = True
      if self.y < 25 or self.y>525:self.gameover = True
      for body in self.snake_body[14:]:
         if(int(self.x) in range(int(body[0])-30,int(body[0])+30))and(int(self.y) in range(int(body[1])-30,int(body[1])+30)):
            self.temp = [int(body[0])-25,int(body[1])-25,50,50]
            self.gameover = True
            break
      if self.gameover:self.head = self.hit
   def walk(self,win,hit,shake):
      win.blit(pygame.image.load('image/bg.jpg'),(0,0))
      if shake:win.blit(pygame.image.load('image/bg_path.png'),(((-1)**shake)*2,((-1)**shake)*3))
      else:win.blit(pygame.image.load('image/bg_path.png'),(0,0))
      win.blit(pygame.image.load('image/title_and_score.png'),(0,0))
      win.blit(pygame.image.load('image/apple.png'),(self.xa,self.ya))
      if hit>0:self.iswalk=False
      if self.iswalk:
         if self.isturn:
            if self.before=='up':self.y-=self.vel
            elif self.before=='down':self.y+=self.vel
            elif self.before=='left':self.x-=self.vel
            elif self.before=='right':self.x+=self.vel
         else:
            if self.state=='up':self.y-=self.vel
            elif self.state=='down':self.y+=self.vel
            elif self.state=='left':self.x-=self.vel
            elif self.state=='right':self.x+=self.vel
         if self.eatcount:
            self.snake_body.insert(0, [self.x,self.y,self.state,self.before,self.isturn])
            if self.eatcount>9:self.eatcount=0
            else:self.eatcount+=1
         else:
            self.snake_body.insert(0, [self.x,self.y,self.state,self.before,self.isturn])
            self.snake_body.pop()
      for i in self.snake_body:
         if self.snake_body.index(i)==len(self.snake_body)-1:body_or_tail = 1
         else:body_or_tail = 0
         if i[4]:
            if i[0]%50==25 and i[1]%50==25:
               i[3]=i[2]
               i[4]=False
            else:
               if i[3]=='up':win.blit(pygame.transform.rotate(self.body[body_or_tail],90),(i[0],i[1]))
               elif i[3]=='down':win.blit(pygame.transform.rotate(self.body[body_or_tail],270),(i[0],i[1]))
               elif i[3]=='left':win.blit(pygame.transform.rotate(self.body[body_or_tail],180),(i[0],i[1]))
               elif i[3]=='right':win.blit(pygame.transform.rotate(self.body[body_or_tail],0),(i[0],i[1]))
         else:
            if i[3]=='up':win.blit(pygame.transform.rotate(self.body[body_or_tail],90),(i[0],i[1]))
            elif i[3]=='down':win.blit(pygame.transform.rotate(self.body[body_or_tail],270),(i[0],i[1]))
            elif i[3]=='left':win.blit(pygame.transform.rotate(self.body[body_or_tail],180),(i[0],i[1]))
            elif i[3]=='right':win.blit(pygame.transform.rotate(self.body[body_or_tail],0),(i[0],i[1]))
      if self.isturn:
         if self.y%50==25 and self.x%50==0:
            self.before=self.state
            if self.state=='up':win.blit(pygame.transform.rotate(self.head[hit],90),(self.x,self.y))
            elif self.state=='down':win.blit(pygame.transform.rotate(self.head[hit],270),(self.x,self.y))
            elif self.state=='left':win.blit(pygame.transform.rotate(self.head[hit],180),(self.x,self.y))
            elif self.state=='right':win.blit(pygame.transform.rotate(self.head[hit],0),(self.x,self.y))
            self.isturn=False
         else:
            if self.before=='up':win.blit(pygame.transform.rotate(self.head[hit],90),(self.x,self.y))
            elif self.before=='down':win.blit(pygame.transform.rotate(self.head[hit],270),(self.x,self.y))
            elif self.before=='left':win.blit(pygame.transform.rotate(self.head[hit],180),(self.x,self.y))
            elif self.before=='right':win.blit(pygame.transform.rotate(self.head[hit],0),(self.x,self.y))
      else:
         if self.before=='up':win.blit(pygame.transform.rotate(self.head[hit],90),(self.x,self.y))
         elif self.before=='down':win.blit(pygame.transform.rotate(self.head[hit],270),(self.x,self.y))
         elif self.before=='left':win.blit(pygame.transform.rotate(self.head[hit],180),(self.x,self.y))
         elif self.before=='right':win.blit(pygame.transform.rotate(self.head[hit],0),(self.x,self.y))
   def key(self):
      for event in pygame.event.get():
         if event.type == pygame.QUIT:self.run = False
         elif event.type == pygame.KEYDOWN:
            if((event.key == pygame.K_LEFT)or(event.key == pygame.K_a))and((self.state!='right'))and(not(self.isturn)):
               self.isturn = self.iswalk = True
               self.before = self.state
               self.state = 'left'
            elif((event.key == pygame.K_RIGHT)or(event.key == pygame.K_d))and((self.state!='left'))and(not(self.isturn)):
               self.isturn = self.iswalk = True
               self.before = self.state
               self.state = 'right'         
            elif((event.key == pygame.K_UP)or(event.key == pygame.K_w))and((self.state!='down'))and(not(self.isturn)):
               self.isturn = self.iswalk = True
               self.before = self.state
               self.state = 'up'         
            elif((event.key == pygame.K_DOWN)or(event.key == pygame.K_s))and((self.state!='up'))and(not(self.isturn)):
               self.isturn = self.iswalk = True
               self.before = self.state
               self.state = 'down'         