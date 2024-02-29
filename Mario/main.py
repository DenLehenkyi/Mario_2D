from Visualization import *
from Player import Player
from Goomba import Goomba
from Menu import *
from Coin import Coin
import ctypes

pygame.init()
screen = pygame.display.set_mode((W, H))

imported_from_cpp = ctypes.CDLL("./kursova.dll")

clock = pygame.time.Clock()
player = Player()
goombas = []
coins = []
delay = 2000
decrease_base = 1.01
last_spawn_time = pygame.time.get_ticks()
FPS = 60


def start_game():
    global score, last_spawn_time, goombas
    score = 0
    last_spawn_time = pygame.time.get_ticks()
    player.respawn()
    goombas.clear()
    coins.clear()
    sky_x = 0
    main_sound.play(loops=-1)


def update_game():
    global score, last_spawn_time, sky_x, coins_count

    screen.blit(sky, (0, 0))
    sky_x -= 2
    if sky_x == -800:
        sky_x = 0

    ground_x = -(player.rect.x % ground_W)
    screen.blit(ground, (ground_x, H - ground_H))
    screen.blit(ground, (ground_x + ground_W, H - ground_H))

    score_text = font_large.render(str(score), True, (255, 255, 255))
    score_rect = score_text.get_rect()
    screen.blit(scoreinfo, (500, 30))

    coin_text = font_large.render(str(coins_count), True, (255, 255, 255))
    coin_rect = coin_text.get_rect()
    screen.blit(coin_info, (100, 30))
    coin_rect.midbottom = (170, 120)

    screen.blit(coin_text, coin_rect)

    if player.is_out:
        score_rect.midbottom = (W // 2, H // 2)
        screen.blit(retry_text, (200, H // 2))
    else:
        player.update()
        player.draw(screen)

        now = pygame.time.get_ticks()
        elapsed = now - last_spawn_time

        if elapsed > delay:
            last_spawn_time = now
            goombas.append(Goomba())
            coins.append(Coin())

        for goomba in list(goombas):
            if goomba.is_out:
                goombas.remove(goomba)
            else:
                goomba.update()
                goomba.draw(screen)
                if not player.is_dead and not goomba.is_dead and player.rect.colliderect(goomba.rect):
                    if player.rect.bottom - player.y_speed < goomba.rect.top:
                        goomba.kill(goomba_dead)
                        mario_kill.play()
                        score = imported_from_cpp.CalculateScore(score)
                        score_text = font_large.render('100', True, (255, 255, 255))
                        score_rect = score_text.get_rect()
                        score_rect.midbottom = goomba.rect.midbottom
                    # screen.blit(score_text, score_rect)
                    else:
                        main_sound.stop()
                        player.kill(mario)
                        mario_dead.play()

        for coin in list(coins):
            if coin.is_out:
                coins.remove(coin)
            else:
                coin.update()
                coin.draw(screen)
                if player.rect.colliderect(coin.rect):
                    coin_sound.play()
                    coins.remove(coin)
                    coins_count = imported_from_cpp.CalculateMoney(coins_count)

                if player.is_dead:
                    coins_count = 0

        score_rect.midbottom = (590, 120)



    screen.blit(score_text, score_rect)
running = True
menu = Menu()
menu.append_option("Play game", start_game)
menu.append_option("Settings", quit)
menu.append_option("Quit", quit)

game_active = False

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_1:
                menu.switch(-1)
            elif e.key == pygame.K_2:
                menu.switch(1)
            elif e.key == pygame.K_3:
                if menu.current_option_index == 0:
                    menu.select()
                    game_active = True
                elif menu.current_option_index == 1:
                    # Обробка налаштувань
                    pass
                elif menu.current_option_index == 2:
                    running = False

            elif e.key == pygame.K_SPACE or e.key == pygame.K_UP or e.key == pygame.K_w:
                if game_active:
                    if player.is_out:
                        start_game()
                        main_sound.play()
                    else:
                        player.jump()

    screen.fill((0, 0, 0))
    screen.blit(mario, (0, 0))
    if game_active:
        update_game()
    else:
        menu.draw_menu(screen, 270, 200, 75)

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()