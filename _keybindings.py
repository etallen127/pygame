import pygame

pygame.init()

""" This page is for defining key and their functions in mygame"""
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

def player_movement(pressed_keys):

if left == 1:
    playerX -= 5
    # playerImage =  pygame.image.load("playerLeft.jpg")
elif right == 1:
     playerX += 5
     # playerImage =  pygame.image.load("playerRight.jpg")
elif up == 1:
    playerY -= 5
    # playerImage =  pygame.image.load("playerUp.jpg")
elif down == 1: 
    playerY += 5
    # playerImage =  pygame.image.load("playerDown.jpg")