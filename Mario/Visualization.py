import pygame

W = 800
H = 600
pygame.font.init()
pygame.mixer.init()

pygame.display.set_caption("Mario Game")
font_path = 'mario_font.ttf'
font_large = pygame.font.Font(font_path, 48)
font_small = pygame.font.Font(font_path, 24)

ground = pygame.image.load("images/ground.png")
ground_H = ground.get_height()
ground_W = ground.get_width()
ground = pygame.transform.scale(ground, (1608, 150))

goomba_skin = pygame.image.load("images/goomba.png")
goomba_skin = pygame.transform.scale(goomba_skin, (80, 80))

goomba_dead = pygame.image.load("images/goomba_dead.png")
goomba_dead = pygame.transform.scale(goomba_dead, (80, 80))

mario_width = 40
mario_height = 40
mario = pygame.image.load("Mario_Anims/mario_right/mright1.png")
mario = pygame.transform.scale(mario, (mario_width, mario_height))

sky = pygame.image.load("images/sky.png")
sky = pygame.transform.scale(sky, (W, H))
game_over = False

retry_text = font_large.render('PRESS ANY KEY', True, (255, 255, 255))
retry_rect = retry_text.get_rect()

main_sound = pygame.mixer.Sound("sound/Mario_Theme.ogg")
mario_dead = pygame.mixer.Sound("sound/mariodie.wav")
mario_kill = pygame.mixer.Sound("sound/kill.wav")

coin = pygame.image.load("images/coin.png")
coin = pygame.transform.scale(coin, (80, 80))

coin_sound = pygame.mixer.Sound("sound/collect_money.mp3")

score = 0
scoreinfo = font_large.render('Score', True, 'White')
sky_x = 0
coins_count = 0
coin_info = font_large.render("Coins", True, 'White')
money = font_large.render("100 ", True, 'White')
