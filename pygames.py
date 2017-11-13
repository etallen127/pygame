import pygame

pygame.init()

# dimensions
screenWidth = 1200
screenHeight = 1000

# video settings
screen = pygame.display.set_mode((screenWidth,screenHeight))
finished = False

# player Info 
playerWidth = 50
playerHeight = 75
playerX = (1/2) * screenWidth - (1/2) * playerWidth
playerY = (1/2) * screenHeight - (1/2) * playerHeight 

# Player Images 
playerImage = pygame.image.load("dogforward.png")
playerImage = pygame.transform.scale(playerImage, (playerWidth,playerHeight))
playerImage = playerImage.convert_alpha()
playerImageLeft = pygame.transform.rotate(playerImage, (-90))

# Background Images
background1 = pygame.image.load("background1.png")
background1 = pygame.transform.scale(background1, (screenWidth,screenHeight))
screen.blit(background1,(0,0))

frame = pygame.time.Clock()

while finished == False:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      finished = True

  pressed_keys = pygame.key.get_pressed() 
  # active keys
  Space_Bar = pressed_keys[pygame.K_SPACE] # interact
  Tab_Key = pressed_keys[pygame.K_TAB] # skills
  skill1 = pressed_keys[pygame.K_1] # skill 1
  skill2 = pressed_keys[pygame.K_2] # skill 2
  skill3 = pressed_keys[pygame.K_3] # skill 3
  skill4 = pressed_keys[pygame.K_4] # skill 4
  skill5 = pressed_keys[pygame.K_5] # skill 5

  # movement keys
  left = pressed_keys[pygame.K_a]
  down = pressed_keys[pygame.K_s]
  right = pressed_keys[pygame.K_d]
  up = pressed_keys[pygame.K_w]

  if left != 0:
    playerX -= 50
    playerImage =  pygame.image.load("dogleft.png")
    playerImage = playerImage.convert_alpha()
    playerWidth = 65
    playerHeight = 40
    playerImage = pygame.transform.scale(playerImage, (playerWidth,playerHeight))
    
  elif right != 0:
    playerX += 50
    playerImage =  pygame.image.load("dogright.png")
    playerImage = playerImage.convert_alpha()
    playerWidth = 65
    playerHeight = 40
    playerImage = pygame.transform.scale(playerImage, (playerWidth,playerHeight))

  elif up == 1:
    playerY -= 50
    playerImage =  pygame.image.load("dogforward.png")
    playerImage = playerImage.convert_alpha()
    playerWidth = 50
    playerHeight = 75
    playerImage = pygame.transform.scale(playerImage, (playerWidth,playerHeight))
  
  elif down == 1: 
    playerY += 50
    playerImage =  pygame.image.load("dogdown.png")
    playerImage = playerImage.convert_alpha()
    playerWidth = 50
    playerHeight = 75
    playerImage = pygame.transform.scale(playerImage, (playerWidth,playerHeight))

  if playerX + 100 > screenWidth:
    playerX = 100
  elif playerX < 100:
    playerX = screenWidth - 100

  if playerY + 100 > screenHeight:
    playerY = 100
  elif playerY < 100:
    playerY = screenHeight - 100

 
  screen.blit(background1,(0,0))
  screen.blit(playerImage,(playerX, playerY))
  pygame.display.flip()
  frame.tick(120)