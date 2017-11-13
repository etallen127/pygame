import pygame

pygame.init()
screen = pygame.display.set_mode((900,700))

finished = False

while finished == False:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      finished = True

  rect_one = pygame.Rect(50,50, 30,50) # x,y,width,height
  rect_one_color = (255,255,30)

  pygame.draw.rect(screen, rect_one_color, rect_one)
  pygame.display.flip()
