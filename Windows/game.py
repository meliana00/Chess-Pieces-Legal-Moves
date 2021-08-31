import images
import pygame
from pygame.locals import *
from sys import exit
import itertools
import brain
import menu 

mute = False
click_cnt = 0
def get_mute_click_cnt():
    return click_cnt

def increase_mute_click_cnt():
    global click_cnt
    click_cnt += 1

def chess():
    pygame.mixer.init()
    if get_mute_click_cnt()%2 == 0:
        soundtrack = pygame.mixer.music.load('music/SYML - I Wanted to Leave.wav')
        pygame.mixer.music.play(-1)

    def show_possible(piece, position):
        alpha_num_map = {v:k for k,v in enumerate('ABCDEFGH', start=1)}
        
        def pixel_to_cell(pos):
            pixel_x = pos[0]
            pixel_y = pos[1]

            cell_x = str(int(pixel_x/84) + 1)
            cell_y =  str(list(alpha_num_map.keys())[list(alpha_num_map.values()).index(8 - (pixel_y/84))])

            return cell_y+cell_x

        def cell_to_pixel(pos):
            x = int(pos[1])
            y = alpha_num_map[pos[0]]

            pixel_x = (x-1)*84
            pixel_y = (8-y)*84

            return [pixel_x, pixel_y]
        
        def pixel_rect(move_list):
            res = []
            for i in move_list:
                res.append(cell_to_pixel(i))

            return res

        move_list = [str(i) for i in brain.possible_moves(piece, pixel_to_cell(position)) if i != 'INVALID']
        pixel_rect_list = pixel_rect(move_list)
        
        return pixel_rect_list

    def set_pos(bg, color, piece, board):
        return_icon = pygame.image.load('images/icons/icons8-reply-arrow-50(3).png')

        def subs(l):
            res = []
            
            res = list(itertools.combinations_with_replacement(l, 2))
                    
            return res

        nums = []

        for i in range(8):
            nums.append(i*84)

        cells = subs(nums)
        reverse = subs(nums[::-1])

        cells = list(set(cells+reverse))

        trigger = pygame.image.load('images/icons/icons8-border-all-84.png')

        pygame.init()

        root = pygame.display.set_mode((730, 730))
        pygame.display.set_caption('Set Position')

        run = True

        square_collide = []
        positions = square_collide

        for i in range(len(cells)):
            square_collide.append(list(cells[i]))

        for j in range(len(square_collide)):
            positions[j].extend([84, 84])

        while run:
            root.blit(color, (0, 0))
            root.blit(bg, (0, 0))
            root.blit(return_icon, (677, 261))

            mx, my = pygame.mouse.get_pos()
            
            return_collide = pygame.Rect(677, 261, 50, 50)

            if return_collide.collidepoint((mx, my)):
                if click:
                    return #used to be game()

            for i in positions:
                if pygame.Rect(tuple(i)).collidepoint((mx, my)):
                    root.blit(trigger, (i))
                    
                    if click:
                        game(board, piece, (i))

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



    def piece_choose(board_default=0, piece_default='pawn', pos=(336, 252)):
        bg = pygame.image.load('images/backgrounds/f2c6dd.png')
        title = pygame.image.load('images/text/text-1629961276086.png')
        hover = pygame.image.load('images/backgrounds/imageedit_5_6750105135.png')
        return_button = pygame.image.load('images/icons/icons8-reply-arrow-64(2).png')
        
        pygame.init()

        root = pygame.display.set_mode((730, 730))
        pygame.display.set_caption('Piece Selection')

        king = pygame.image.load('images/pieces/icons8-king-100.png')
        queen = pygame.image.load('images/pieces/icons8-queen-100.png')
        pawn = pygame.image.load('images/pieces/icons8-pawn-100.png')
        bishop = pygame.image.load('images/pieces/icons8-bishop-100.png')
        rook = pygame.image.load('images/pieces/icons8-rook-100.png')
        knight = pygame.image.load('images/pieces/icons8-knight-100.png')

        king_font = pygame.image.load('images/text/text-1629830358075.png')
        queen_font = pygame.image.load('images/text/text-1629830461703.png')
        pawn_font = pygame.image.load('images/text/text-1629830488123.png')
        bishop_font = pygame.image.load('images/text/text-1629830514245.png')
        rook_font = pygame.image.load('images/text/text-1629830545274.png')
        knight_font = pygame.image.load('images/text/text-1629830575847.png')

        run = True

        while run:
            root.blit(bg, (0, 0))
            root.blit(return_button, (7, 7))
            root.blit(title, (274.5, 30))

            mx, my = pygame.mouse.get_pos()

            king_collide = pygame.Rect(99, 150, 100, 100)
            queen_collide = pygame.Rect(319, 150, 100, 100)
            knight_collide = pygame.Rect(539, 150, 100, 100)
            rook_collide = pygame.Rect(99, 380, 100, 100)
            pawn_collide = pygame.Rect(319, 380, 100, 100)
            bishop_collide = pygame.Rect(539, 380, 100, 100)
            return_button_collide = pygame.Rect(7, 7, 64, 64)

            
            root.blit(king, (99, 150))
            root.blit(queen, (319, 150))
            root.blit(knight, (539, 150))
            root.blit(rook, (99, 380))
            root.blit(pawn, (319, 380))
            root.blit(bishop, (539, 380))

            if king_collide.collidepoint((mx, my)):
                root.blit(hover, (99, 150))
                if click:
                    piece_default = 'king' 
                    game(board_default, piece_default, pos)
            if  queen_collide.collidepoint((mx, my)):
                root.blit(hover, (319, 150))
                if click:
                    piece_default = 'queen'
                    game(board_default, piece_default , pos)

            if knight_collide.collidepoint((mx, my)):
                root.blit(hover, (539, 150))
                if click:
                    piece_default = 'knight' 
                    game(board_default, piece_default , pos)

            if rook_collide.collidepoint((mx, my)):
                root.blit(hover, (99, 380))
                if click:
                    piece_default = 'rook'
                    game(board_default, piece_default , pos)

            if pawn_collide.collidepoint((mx, my)):
                root.blit(hover, (319, 380))
                if click:
                    piece_default = 'pawn'
                    game(board_default, piece_default , pos)

            if bishop_collide.collidepoint((mx, my)):
                root.blit(hover, (539, 380))
                if click:
                    piece_default = 'bishop'
                    game(board_default, piece_default, pos )

            if return_button_collide.collidepoint((mx, my)):
                if click:
                    game(board_default, 'pawn', pos)
                    #game(board_default, piece_default )

            root.blit(king_font, (109, 270))
            root.blit(queen_font, (314, 270))
            root.blit(knight_font, (524, 270))
            root.blit(rook_font, (99, 500))
            root.blit(pawn_font, (319, 500))
            root.blit(bishop_font, (522, 500))

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

    def board_color_select(board_default=0, piece_default='pawn', pos=(336, 252)):
        bg = pygame.image.load('images/backgrounds/ffcba4.png')
        return_button = pygame.image.load('images/icons/icons8-reply-arrow-64(1).png')
        grey_mode_button = pygame.image.load('images/buttons/CGB02-grey_M_btn.png')
        green_mode_button = pygame.image.load('images/buttons/CGB02-green_M_btn.png')

        green_font = pygame.image.load('images/text/text-1629543607354.png')
        grey_font = pygame.image. load('images/text/text-1629543845773.png')
        pink_font = pygame.image.load('images/text/text-1629544089972.png')
        blue_font = pygame.image.load('images/text/text-1629544268459.png')
        purple_font = pygame.image.load('images/text/text-1629544429630.png')
        red_font = pygame.image.load('images/text/text-1629544606588.png')
        board_font = pygame.image.load('images/text/text-1629544715543.png')
        
        pygame.init()

        root = pygame.display.set_mode((730, 730))
        pygame.display.set_caption('Board Design')

        run = True
        
        while run:
            root.blit(bg, (0, 0))
            root.blit(board_font, (258, 30))
            root.blit(return_button, (7, 7))

            mx, my = pygame.mouse.get_pos()

            mode_one_button_collide = pygame.Rect(50, 150, 256, 140)
            mode_two_button_collide = pygame.Rect(50, 320, 256, 140)
            mode_three_button_collide = pygame.Rect(50, 490, 256, 140)
            mode_four_button_collide = pygame.Rect(420, 150, 256, 140)
            mode_five_button_collide = pygame.Rect(420, 320, 256, 140)
            mode_six_button_collide = pygame.Rect(420, 490, 256, 140)
            return_button_collide = pygame.Rect(7, 7, 50, 50)

            if board_default == 1: #if mode 1 is selected
                root.blit(grey_mode_button, (50, 320))
                root.blit(grey_mode_button, (50, 150))
                root.blit(grey_mode_button, (50, 490))
                root.blit(grey_mode_button, (420, 150))
                root.blit(grey_mode_button, (420, 320))
                root.blit(grey_mode_button, (420, 490))
                game(board_default, piece_default, pos)

            elif board_default == 0:
                root.blit(grey_mode_button, (50, 150))
                root.blit(grey_mode_button, (50, 320))
                root.blit(grey_mode_button, (50, 490))
                root.blit(grey_mode_button, (420, 150))
                root.blit(grey_mode_button, (420, 320))
                root.blit(grey_mode_button, (420, 490))
                
            elif board_default == 2:
                root.blit(grey_mode_button, (50, 150))
                root.blit(grey_mode_button, (50, 320))
                root.blit(grey_mode_button, (50, 490))
                root.blit(grey_mode_button, (420, 150))
                root.blit(grey_mode_button, (420, 320))
                root.blit(grey_mode_button, (420, 490))
                game(board_default, piece_default, pos)

            elif board_default == 3:
                root.blit(grey_mode_button, (50, 150))
                root.blit(grey_mode_button, (50, 320))
                root.blit(grey_mode_button, (50, 490))
                root.blit(grey_mode_button, (420, 150))
                root.blit(grey_mode_button, (420, 320))
                root.blit(grey_mode_button, (420, 490))
                game(board_default, piece_default, pos)

            elif board_default == 4:
                root.blit(grey_mode_button, (50, 150))
                root.blit(grey_mode_button, (50, 320))
                root.blit(grey_mode_button, (50, 490))
                root.blit(grey_mode_button, (420, 150))
                root.blit(grey_mode_button, (420, 320))
                root.blit(grey_mode_button, (420, 490))
                game(board_default, piece_default, pos)

            elif board_default == 5:
                root.blit(grey_mode_button, (50, 150))
                root.blit(grey_mode_button, (50, 320))
                root.blit(grey_mode_button, (50, 490))
                root.blit(grey_mode_button, (420, 150))
                root.blit(grey_mode_button, (420, 320))
                root.blit(grey_mode_button, (420, 490))
                game(board_default, piece_default, pos)

            elif board_default == 6:
                root.blit(grey_mode_button, (50, 150))
                root.blit(grey_mode_button, (50, 320))
                root.blit(grey_mode_button, (50, 490))
                root.blit(grey_mode_button, (420, 150))
                root.blit(grey_mode_button, (420, 320))
                root.blit(grey_mode_button, (420, 490))
                game(0, piece_default, pos)

            if mode_two_button_collide.collidepoint((mx, my)):
                root.blit(green_mode_button, (50, 320))
                if click:
                    board_default = 1 #mode 2
                    
            elif  mode_one_button_collide.collidepoint((mx, my)):
                root.blit(green_mode_button, (50, 150))
                if click:
                    board_default = 6 #mode 1

            elif mode_three_button_collide.collidepoint((mx, my)):
                
                root.blit(green_mode_button, (50, 490))
                if click:
                    board_default = 2 #mode 3

            elif mode_four_button_collide.collidepoint((mx, my)):
                root.blit(green_mode_button, (420, 150))
                if click:
                    board_default = 3 #mode 4
            elif mode_five_button_collide.collidepoint((mx, my)):
                root.blit(green_mode_button, (420, 320))
                if click:
                    board_default = 4 #mode 5
            elif mode_six_button_collide.collidepoint((mx, my)):
                root.blit(green_mode_button, (420, 490))
                if click:
                    board_default = 5 #mode 6
            elif return_button_collide.collidepoint((mx, my)):
                if click:
                    game(board_default, piece_default, pos)

            root.blit(green_font, (84, 187.5))
            root.blit(grey_font, (99, 357.5))
            root.blit(pink_font, (102, 527.5))
            root.blit(blue_font, (470, 187.5))
            root.blit(purple_font, (436.5, 357.5))
            root.blit(red_font, (484, 527.5))
            
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

    
    def game(default_board=0, default_piece='pawn', pos=(336, 252)):
        purple_board = pygame.image.load('images/boards/checkerboard_purple(1).png')
        red_board = pygame.image.load('images/boards/checkerboard_red(1).png')
        pink_board = pygame.image.load('images/boards/checkerboard_pink(1).png')
        green_board = pygame.image.load('images/boards/checkerboard_green(2).png')
        blue_board = pygame.image.load('images/boards/checkerboard_blue(1).png')
        grey_board = pygame.image.load('images/boards/chessboard.gif')
        
        green_bg = pygame.image.load('images/backgrounds/80bd8f.png')
        blue_bg = pygame.image.load('images/backgrounds/2ca7b9.png')
        pink_bg = pygame.image.load('images/backgrounds/d394bb.png')
        red_bg = pygame.image.load('images/backgrounds/e4746b.png')
        purple_bg = pygame.image.load('images/backgrounds/9394cc.png')
        grey_bg = pygame.image.load('images/backgrounds/d7ded3.png') 

        return_icon = pygame.image.load('images/icons/icons8-reply-arrow-50(3).png')
        exit_icon = pygame.image.load('images/icons/icons8-close-window-50.png')

        chessboard_icon_green = pygame.image.load('images/icons/icons8-chess-board-50.png')
        chesspiece_icon_green = pygame.image.load('images/icons/icons8-board-game-figure-50.png')
        mute_icon_green = pygame.image.load('images/icons/icons8-mute-50(3).png')
        position_icon_green = pygame.image.load('images/icons/icons8-place-marker-50.png')

        chessboard_icon_black = pygame.image.load('images/icons/icons8-chess-board-50(2).png')
        chesspiece_icon_black = pygame.image.load('images/icons/icons8-board-game-figure-50(1).png')
        mute_icon_black = pygame.image.load('images/icons/icons8-mute-50(2).png')
        position_icon_black = pygame.image.load('images/icons/icons8-place-marker-50(2).png')

        chessboard_icon_blue = pygame.image.load('images/icons/icons8-chess-board-50(3).png')
        chesspiece_icon_blue = pygame.image.load('images/icons/icons8-board-game-figure-50(2).png')
        mute_icon_blue = pygame.image.load('images/icons/icons8-mute-50(4).png')
        position_icon_blue = pygame.image.load('images/icons/icons8-place-marker-50(3).png')

        chessboard_icon_red = pygame.image.load('images/icons/icons8-chess-board-50(1).png')
        chesspiece_icon_red = pygame.image.load('images/icons/icons8-board-game-figure-50(3).png')
        mute_icon_red = pygame.image.load('images/icons/icons8-mute-50(5).png')
        position_icon_red = pygame.image.load('images/icons/icons8-place-marker-50(4).png')

        chessboard_icon_purple = pygame.image.load('images/icons/icons8-chess-board-50(5).png')
        chesspiece_icon_purple = pygame.image.load('images/icons/icons8-board-game-figure-50(4).png')
        mute_icon_purple = pygame.image.load('images/icons/icons8-mute-50(6).png')
        position_icon_purple = pygame.image.load('images/icons/icons8-place-marker-50(5).png')

        chessboard_icon_pink = pygame.image.load('images/icons/icons8-chess-board-50(6).png')
        chesspiece_icon_pink = pygame.image.load('images/icons/icons8-board-game-figure-50(5).png')
        mute_icon_pink = pygame.image.load('images/icons/icons8-mute-50(7).png')
        position_icon_pink = pygame.image.load('images/icons/icons8-place-marker-50(6).png')

        chessboard_hover = pygame.image.load('images/text/text-1629794955368.png')
        chesspiece_hover = pygame.image.load('images/text/text-1629795041496.png')
        mute_hover = pygame.image.load('images/text/text-1629795088276.png')
        position_hover = pygame.image.load('images/text/text-1629795118799.png')
        return_hover = pygame.image.load('images/text/text-1629795781903.png')
        exit_hover = pygame.image.load('images/text/text-1629795796445.png')
        unmute_hover = pygame.image.load('images/text/text-1630148453325.png')

        player_king = pygame.image.load('images/pieces/icons8-king-80(4).png')
        player_queen = pygame.image.load('images/pieces/icons8-queen-80(2).png')
        player_knight = pygame.image.load('images/pieces/icons8-knight-80(11).png')
        player_rook = pygame.image.load('images/pieces/icons8-rook-80(2).png')
        player_pawn = pygame.image.load('images/pieces/icons8-pawn-80(2).png')
        player_bishop = pygame.image.load('images/pieces/icons8-bishop-80(2).png')

        possible = pygame.image.load('images/icons/icons8-square-84(1).png')

        pygame.init()

        root = pygame.display.set_mode((730, 730))
        
        pygame.display.set_caption('Chess')

        run = True
        click_cnt = 0

        board_color = green_board
        bg_color = green_bg
        chessboard_default_icon = chessboard_icon_green
        chesspiece_default_icon = chesspiece_icon_green
        mute_default_icon = mute_icon_green
        position_default_icon = position_icon_green
        
        while run:
            if default_board == 0:
                board_color = green_board
                bg_color = green_bg
                chessboard_default_icon = chessboard_icon_green
                chesspiece_default_icon = chesspiece_icon_green
                mute_default_icon = mute_icon_green
                position_default_icon = position_icon_green
                
            elif default_board == 1:
                board_color = grey_board
                bg_color = grey_bg
                chessboard_default_icon = chessboard_icon_black
                chesspiece_default_icon = chesspiece_icon_black
                mute_default_icon = mute_icon_black
                position_default_icon = position_icon_black

            elif default_board == 2:
                board_color = pink_board
                bg_color = pink_bg
                chessboard_default_icon = chessboard_icon_pink
                chesspiece_default_icon = chesspiece_icon_pink
                mute_default_icon = mute_icon_pink
                position_default_icon = position_icon_pink

            elif default_board == 3:
                board_color = blue_board
                bg_color = blue_bg
                chessboard_default_icon = chessboard_icon_blue
                chesspiece_default_icon = chesspiece_icon_blue
                mute_default_icon = mute_icon_blue
                position_default_icon = position_icon_blue

            elif default_board == 4:
                board_color = purple_board
                bg_color = purple_bg
                chessboard_default_icon = chessboard_icon_purple
                chesspiece_default_icon = chesspiece_icon_purple
                mute_default_icon = mute_icon_purple
                position_default_icon = position_icon_purple

            elif default_board == 5:
                board_color = red_board
                bg_color = red_bg
                chessboard_default_icon = chessboard_icon_red
                chesspiece_default_icon = chesspiece_icon_red
                mute_default_icon = mute_icon_red
                position_default_icon = position_icon_red

            root.blit(bg_color, (0, 0))
            root.blit(board_color, (0, 0))
            root.blit(chessboard_default_icon, (677, 4))
            root.blit(chesspiece_default_icon, (677, 68))
            root.blit(mute_default_icon, (677, 133))
            root.blit(position_default_icon, (677, 197))
            root.blit(return_icon, (677, 261))
            root.blit(exit_icon, (677, 325))

            if default_piece == 'pawn':
                root.blit(player_pawn, pos)
            elif default_piece == 'knight':
                root.blit(player_knight, pos)
            elif default_piece == 'rook':
                root.blit(player_rook, pos)
            elif default_piece == 'queen':
                root.blit(player_queen, pos)
            elif default_piece == 'king':
                root.blit(player_king, pos)
            elif default_piece == 'bishop':
                root.blit(player_bishop, pos)

            possible_area = show_possible(default_piece, pos)

            for i in possible_area:
                root.blit(possible, i)
            
            mx, my = pygame.mouse.get_pos()

            chessboard_icon_collide = pygame.Rect(677, 4, 50, 50)
            exit_button_collide = pygame.Rect(677, 325, 50, 50)
            return_button_collide = pygame.Rect(677, 261, 50, 50)
            piece_icon_collide = pygame.Rect(677, 68, 50, 50)
            mute_icon_collide = pygame.Rect(677, 132, 50, 50)
            position_icon_collide = pygame.Rect(677, 196, 50, 50)

            if mute_icon_collide.collidepoint((mx, my)):
                if click: 
                    increase_mute_click_cnt()
                    if get_mute_click_cnt() % 2 == 0:
                            pygame.mixer.init()
                            soundtrack = pygame.mixer.music.load('music/SYML - I Wanted to Leave.wav')
                            pygame.mixer.music.play(-1)

                    else:
                        pygame.mixer.quit()

            if chessboard_icon_collide.collidepoint((mx, my)):
                root.blit(chessboard_hover, (573, 21))
                if click:
                    board_color_select(0, default_piece, pos)

            elif piece_icon_collide.collidepoint((mx, my)):
                root.blit(chesspiece_hover, (548, 85))
                if click:
                    piece_choose(default_board, default_piece, pos)

            elif mute_icon_collide.collidepoint((mx, my)):
                if get_mute_click_cnt() % 2 != 0:
                    root.blit(unmute_hover, (560, 149))
                else:
                    root.blit(mute_hover, (573, 149))

            elif position_icon_collide.collidepoint((mx, my)):
                root.blit(position_hover, (537, 213))
                if click:
                    set_pos(board_color, bg_color, default_piece, default_board)

            elif return_button_collide.collidepoint((mx, my)):
                root.blit(return_hover, (511, 277))
                if click:
                    pygame.mixer.quit()
                    menu.menu()

            elif exit_button_collide.collidepoint((mx, my)):
                root.blit(exit_hover, (573, 341))
                if click:
                    pygame.quit()
                    exit()

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

    game()
