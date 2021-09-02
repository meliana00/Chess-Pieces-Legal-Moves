from itertools import count
import pygame
from pygame.locals import *
from sys import exit
import brain
import game
from game import get_mute_click_cnt, increase_mute_click_cnt

def menu():
    pygame.mixer.init()
    if get_mute_click_cnt()%2 == 0:
        bg_music = pygame.mixer.music.load('music/menu(compressed).wav')
        pygame.mixer.music.play(-1)

    def help():
        blur_bg = pygame.image.load('images/backgrounds/output-onlineimagetools.png')
        return_button = pygame.image.load('images/icons/icons8-reply-arrow-64(1).png')
        title = pygame.image.load('images/text/text-1630056929491.png')
        instructions = pygame.image.load('images/backgrounds/imageedit_1_9573724241.png')

        pygame.init()

        root = pygame.display.set_mode((730, 730))
        pygame.display.set_caption('Menu (Help)')
        
        run = True

        click = False
        while run:
            root.blit(blur_bg, (0, 0))
            root.blit(return_button, (7, 7))
            root.blit(title, (284.5, 30))
            root.blit(instructions, (91.5, 110))

            mx, my = pygame.mouse.get_pos()

            return_button_collide = pygame.Rect(7, 7, 64, 64)

            if return_button_collide.collidepoint((mx, my)):
                if click:
                    main_menu()

            click = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()

        pygame.quit()

    def credits():
        blur_bg = pygame.image.load('images/backgrounds/output-onlineimagetools.png')
        return_button = pygame.image.load('images/icons/icons8-reply-arrow-64(1).png')
        title = pygame.image.load('images/text/text-1630173959138.png')
        credits_text = pygame.image.load('images/backgrounds/imageedit_7_3188510609.png')

        pygame.init()

        root = pygame.display.set_mode((730, 730))

        pygame.display.set_caption('Menu (Credits)')

        run = True
        click = False

        while run:
            root.blit(blur_bg, (0, 0))
            root.blit(return_button, (7, 7))
            root.blit(title, (267, 30))
            root.blit(credits_text, (92, 120))

            mx, my = pygame.mouse.get_pos()

            return_button_collide = pygame.Rect(7, 7, 64, 64)

            if return_button_collide.collidepoint((mx, my)):
                if click:
                    main_menu()

            click = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                
            pygame.display.update()

        pygame.quit()

    def error_show():
        bg = pygame.image.load('images/backgrounds/output-onlineimagetools.png')
        attention = pygame.image.load('images/backgrounds/error.png')

        pygame.init()

        root = pygame.display.set_mode((730, 730))

        run = True
        click = False
        
        while run:
            root.blit(bg, (0, 0))

            mx, my = pygame.mouse.get_pos()

            ok_button_collide = pygame.Rect(333, 400, 64, 64)
            
            root.blit(attention, (113.5, 200))

            if ok_button_collide.collidepoint((mx, my)):
                if click:
                    settings()

            click = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()

        pygame.quit()

    def settings():
        blur_bg = pygame.image.load('images/backgrounds/output-onlineimagetools.png')
        return_button = pygame.image.load('images/icons/icons8-reply-arrow-64(1).png')
        grey_mode_button = pygame.image.load('images/buttons/CGB02-grey_M_btn.png')
        green_mode_button = pygame.image.load('images/buttons/CGB02-green_M_btn.png')
        title = pygame.image.load('images/text/text-1629962092292.png')
        button_one_font = pygame.image.load('images/text/text-1629963165338.png')
        button_two_font = pygame.image.load('images/text/text-1629963397570.png')
        pygame.init()

        root = pygame.display.set_mode((730, 730))

        pygame.display.set_caption('Menu (Game Mode)')
      
        run = True
        default = 0
        click = False

        while run:
            root.blit(blur_bg, (0, 0))
            root.blit(return_button, (7, 7))
            root.blit(title, (195.5, 30))

            mx, my = pygame.mouse.get_pos()

            mode_one_button_collide = pygame.Rect(237, 150, 256, 140)
            mode_two_button_collide = pygame.Rect(237, 400, 256, 140)
            return_button_collide = pygame.Rect(7, 7, 64, 64)

            if return_button_collide.collidepoint((mx, my)):
                if click:
                    main_menu()
                    
            if mode_two_button_collide.collidepoint((mx, my)):
                if click:
                    default = 1 #mode 2
                    error_show()
                
            if  mode_one_button_collide.collidepoint((mx, my)):
                if click:
                    default = 0 #mode 1

            click = False

            if default: #if mode 1 is selected
                root.blit(green_mode_button, (237, 400))
                root.blit(grey_mode_button, (237, 150))

            else:
                root.blit(green_mode_button, (237, 150))
                root.blit(grey_mode_button, (237, 400))

            root.blit(button_one_font, (274, 200))
            root.blit(button_two_font, (264, 450))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()

        pygame.quit()


    def main_menu():

        bg = pygame.image.load('images/backgrounds/1bSLcp5-chess-board-wallpaper(2).jpg')
        play_button = pygame.image.load('images/buttons/CGB02-orange_M_btn.png')
        play_font = pygame.image.load('images/text/text-1629543200641.png')
        mute_buton = pygame.image.load('images/icons/icons8-mute-64(1).png')
        settings_button = pygame.image.load('images/icons/icons8-settings-64(5).png')
        exit_button = pygame.image.load('images/icons/icons8-close-window-64.png')
        help_button = pygame.image.load('images/icons/icons8-help-64(6).png')
        credits_button = pygame.image.load('images/icons/icons8-person-female-64.png')
        github_logo = pygame.image.load('images/icons/icons8-github-40.png')
        gmail_logo = pygame.image.load('images/icons/icons8-gmail-35.png')
        github_id = pygame.image.load('images/text/text-1630172438026.png')
        gmail_id = pygame.image.load('images/text/text-1630172139331.png')
        
        pygame.init()

        root = pygame.display.set_mode((730, 730))
        pygame.display.set_caption('Chess (Main Menu)')

        click_cnt = 0
        run = True
        click = False

        while run:
            root.blit(bg, (0, 0))
            root.blit(play_button, (237, 150))
            root.blit(play_font, (296.5, 189.5))
            root.blit(mute_buton, (111, 450))
            root.blit(settings_button, (111, 545))
            root.blit(exit_button, (659, 7))
            root.blit(help_button, (555, 450))
            root.blit(credits_button, (555, 545))
            root.blit(github_logo, (0, 0))
            root.blit(gmail_logo, (3, 50))
            root.blit(github_id, (50, 15))
            root.blit(gmail_id, (50, 60))

            mx, my = pygame.mouse.get_pos()

            play_button_collide = pygame.Rect(237, 150, 256, 140)
            exit_button_collide = pygame.Rect(659, 7, 64, 64)
            credits_button_collide = pygame.Rect(555, 545, 64, 64)
            settings_button_collide = pygame.Rect(111, 545, 64, 64)
            help_button_collide = pygame.Rect(555, 450, 64, 64)
            mute_button_collide = pygame.Rect(111, 450, 64, 64)

            if mute_button_collide.collidepoint((mx, my)):
                if click:
                    # click_cnt += 1
                    increase_mute_click_cnt()
                    if get_mute_click_cnt() % 2 == 0:
                            pygame.mixer.init()
                            bg_music = pygame.mixer.music.load('music/menu(compressed).wav')
                            pygame.mixer.music.play(-1)

                    else:
                        pygame.mixer.quit()

            if exit_button_collide.collidepoint((mx, my)):
                if click:
                    pygame.quit()
                    exit()

            if play_button_collide.collidepoint((mx, my)):
                if click:
                    pygame.mixer.quit()
                    game.chess()

            if credits_button_collide.collidepoint((mx, my)):
                if click:
                    credits()

            if settings_button_collide.collidepoint((mx, my)):
                if click:
                    settings()

            if help_button_collide.collidepoint((mx, my)):
                if click:
                    help()

            click = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()

        pygame.quit()

    main_menu()

menu()
