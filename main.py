import pygame, sys
from pygame.locals import QUIT, K_LEFT, K_RIGHT, KEYDOWN,K_UP, K_SPACE, K_1
distance = 0
l = 0
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Replit platformar')
clock = pygame.time.Clock()
y = 0
test_font_distance = pygame.font.Font(None, 40)
test_font_winner = pygame.font.Font(None, 40)
test_font_game = pygame.font.Font(None, 80)

winner = test_font_winner.render("You win!", True, 'Black')

sky_surface = pygame.Surface((800, 400))
sky_surface.fill('lightblue')
land_surface = pygame.Surface((200, 50))
land_surface.fill('green')
land_rec = land_surface.get_rect(midbottom=(0, 300))
l1 = pygame.Surface((200, 50))
l1.fill('green')
l1_rec = l1.get_rect(midbottom=(400, 300))
l2 = pygame.Surface((200, 50))
l2.fill('red')
l2_rec = l2.get_rect(midbottom=(200, 300))
l3 = pygame.Surface((200, 50))
l3.fill('green')
l3_rec = l3.get_rect(midbottom=(500, 250))
l4 = pygame.Surface((1100, 50))
l4.fill('red')
l4_rec = l4.get_rect(midbottom=(955, 300))
l5 = pygame.Surface((200, 50))
l5.fill('green')
l5_rec = l5.get_rect(midbottom=(500, 200))
l7 = pygame.Surface((10, 200))
l7.fill('purple')
l7_rec = l7.get_rect(midbottom=(500, 150))

player = pygame.image.load('graphics/player.png').convert_alpha()
gameover = pygame.image.load('graphics/gameover.png').convert_alpha()
player_rec = player.get_rect(midbottom=(40, 200))
spike = pygame.image.load('graphics/spike.png').convert_alpha()
spike_rec = spike.get_rect(midbottom=(500, 200))
spike1 = pygame.image.load('graphics/spike.png').convert_alpha()
spike1_rec = spike.get_rect(midbottom=(500, 150))
sign = pygame.image.load('graphics/sign.png').convert_alpha()
sign_rec = sign.get_rect(midbottom=(190, 320))
sign1 = pygame.image.load('graphics/sign.png').convert_alpha()
sign1_rec = sign.get_rect(midbottom=(500, 320))


if_game_is_still_going = 'yes'
while True:
    distance_surface = test_font_distance.render(f"{distance}m", True, 'Black')
    for event in pygame.event.get():
      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   

  
    if event.type == pygame.KEYDOWN:
        keys = pygame.key.get_pressed()
       
        if keys[pygame.K_UP]:
          if player_rec.colliderect(land_rec):
              player_rec.y -= 100
          if player_rec.colliderect(l1_rec):
              player_rec.y -= 100
          if player_rec.colliderect(l3_rec):
              player_rec.y -= 100
          if player_rec.colliderect(l5_rec):
              player_rec.y -= 100
        if keys[pygame.K_RIGHT]:
            distance += 1
            sign_rec.x -= 5
            land_rec.x -= 5
            l1_rec.x -= 5
            l2_rec.x -= 5
            if distance >= 20:
              l4_rec.x -= 5
            if distance >= 20:
              sign1_rec.x -= 5
            if distance >= 58:
              l3_rec.x -= 5
            if distance >= 55:
              spike_rec.x -= 5
            if distance >= 123:
              l5_rec.x -= 5
            if distance >= 115:
              spike1_rec.x -= 5
            if distance >= 142:
              l7_rec.x -= 5
          
        if keys[pygame.K_LEFT]:
            distance -= 1
            sign_rec.x += 5
            land_rec.x += 5
            l1_rec.x += 5
            l2_rec.x += 5
            if distance >= 20:
              l4_rec.x += 5
            if distance >= 20:
              sign1_rec.x += 5
            if distance >= 58:
              l3_rec.x += 5
            if distance >= 55:
              spike_rec.x += 5
            if distance >= 123:
              l5_rec.x += 5
            if distance >= 115:
              spike1_rec.x += 5
            if distance >= 142:
              l7_rec.x += 5
        if event.key == pygame.K_SPACE:
            print(player_rec.y)

        
    if player_rec.y >= 250:
      if_game_is_still_going = 'gameover'
    if player_rec.colliderect(l2_rec):
      if_game_is_still_going = 'gameover'
    if player_rec.colliderect(spike_rec):
      if_game_is_still_going = 'gameover'
    if player_rec.colliderect(spike1_rec):
      if_game_is_still_going = 'gameover'
    if player_rec.colliderect(l4_rec):
      if_game_is_still_going = 'gameover'
    if player_rec.colliderect(l7_rec):
      if_game_is_still_going = 'win'
    if not player_rec.colliderect(land_rec):
        if not player_rec.colliderect(l1_rec):
          if not player_rec.colliderect(l3_rec):
            if not player_rec.colliderect(l5_rec):
               player_rec.y += 1.9
    if if_game_is_still_going == 'gameover':
        #print("gameover")
        sky_surface.fill('light blue')
       
        screen.blit(gameover,(0,0))
    if if_game_is_still_going == 'yes':
        
        screen.blit(sky_surface, (0, 0))
        screen.blit(distance_surface, (0, 0))
        screen.blit(land_surface, (land_rec))
        if distance >= 20:
          screen.blit(sign1,(sign1_rec))
        if distance >= 142:
          screen.blit(l7,(l7_rec))
        screen.blit(l1, (l1_rec))
        screen.blit(sign,(sign_rec))
        screen.blit(l2, (l2_rec))
       
        if distance >= 58:
           screen.blit(l3, (l3_rec))
        if distance >= 123:
           screen.blit(l5, (l5_rec))
        if distance >= 55:
           screen.blit(spike, (spike_rec))
        if distance >= 20:
           screen.blit(l4, (l4_rec))
        if distance >= 115:
           screen.blit(spike1,(spike1_rec))
        screen.blit(player, (player_rec))
      
    else:
        screen.blit(sky_surface, (0, 0))
    pygame.display.update()
    clock.tick(60)
