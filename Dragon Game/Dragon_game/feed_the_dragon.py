import pygame
import random
pygame.init()

#set display surface
#constants class
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400 
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Feed the Dragon")

#set FPS and Clock
FPS = 60
clock = pygame.time.Clock()

#set game values
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 10
COIN_STARTING_VELOCITY = 5
COIN_ACCELERATION = .5
BUFFER_DISTANCE = 100

#set colors
GREEN = (0,255,0)
DARK_GREEN = (10,50,10)
WHITE = (255,255,255)
BLACK = (0,0,0)
SCORE = 0

#Set font
font = pygame.font.SysFont('calibri',32)

# Actor Class
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY


#Text Class
#set text
score_text = font.render("Score: " + str(SCORE), True, GREEN, DARK_GREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10,10)

title_text = font.render("Feed the Dragon!", True, GREEN)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.y = 10

lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARK_GREEN)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH-10, 10)

game_over_text = font.render("GAMEOVER", True, GREEN, DARK_GREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to play again.", True, GREEN, DARK_GREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 32)

#Sound Class
#set sounds and music
coin_sound = pygame.mixer.Sound("coin_sound.wav")
miss_sound = pygame.mixer.Sound("miss_sound.wav")
miss_sound.set_volume(.1)
pygame.mixer.music.load("ftd.background_music.wav")

#Dragon Class
#set images
player_image = pygame.image.load("dragon_right.png")
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = WINDOW_HEIGHT//2

#Coin clas (add a another object)
coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)

#Director Class
pygame.mixer.music.play(-1)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #May divde this up into keyboard and director class
    #check to see if the user wants to move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.top > 64:
        player_rect.y -= PLAYER_VELOCITY
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += PLAYER_VELOCITY

    #may divde into different class (Sound class, Action Class, Coin Class, Actor Class)  Write an if statement is director 
    #update using methods
    #move the coin
    if coin_rect.x <0:
        #player missed coin
        player_lives -=1    
        miss_sound.play() 
        coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.y = random.randint (64, WINDOW_HEIGHT - 32)
    else:
        #move the coin
        coin_rect.x -= coin_velocity

    #Collsions class
    #check for collisions
    if player_rect.colliderect(coin_rect):
        SCORE += 10
        coin_sound.play()
        coin_velocity += COIN_ACCELERATION
        coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.y = random.randint (64, WINDOW_HEIGHT - 32)

    #Score Class
    #Update the score area
    score_text = font.render("Score: " + str(SCORE), True, GREEN, DARK_GREEN)
    lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARK_GREEN)
    if player_lives ==0:
        display_surface.blit(game_over_text,game_over_rect)
        display_surface.blit(continue_text,continue_rect)
        pygame.display.update()

        #director class
        #pause game until player presses a key to reset game
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    SCORE = 0
                    player_lives = PLAYER_STARTING_LIVES
                    player_rect.y = WINDOW_HEIGHT//2
                    coin_velocity = COIN_STARTING_VELOCITY
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    #Hud Class
    #fill the display
    display_surface.fill(BLACK)
    display_surface.blit(score_text,score_rect)
    display_surface.blit(title_text,title_rect)
    display_surface.blit(lives_text,lives_rect)
    pygame.draw.line(display_surface, WHITE, (0,64), (WINDOW_WIDTH, 64), 2)
    #coin_rect.y = random.randint (64, WINDOW_HEIGHT - 32)

    #blit assests
    display_surface.blit(player_image,player_rect)
    display_surface.blit(coin_image,coin_rect)
    
    #Director Class
    #update display
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

