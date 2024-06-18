# Programmer:   Stephen Myers
# Program:      2-Player Chess Game

# Synopsis:     This program implements a two player chess game using the pygame module.
#               The player should have a general idea of the rules of chess prior to playing this game
#-----------------------------------------------------------------------------------------------------
import pygame
#game window 
WIDTH = 1150 
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
from functions import*
pygame.init()


create_black_squares()
create_white_squares()
black_options = check_options(black_pieces, black_locations, 'black') 
white_options = check_options(white_pieces, white_locations, 'white')
# Main Game loop 
#----------------------------------------------------------------------------------------------------------------------------
run = True 
while run:
    screen.fill('grey')
    #draw the black squares on to the screen 
    draw_board(screen)
    draw_pieces(screen)
    display_turn(screen)
    draw_captured_pieces(screen)
    check(check)
    #enforce_check_move()
    # if a piece has been clicked on 
    if selection != 100:
        valid_moves = check_valid_moves()
       
        draw_valid_moves(valid_moves)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # The x coordinate of the event divided by floor(100)
            x_coord = event.pos[0]  // 100
            # The y coordinate of the event 
            y_coord = event.pos[1]  // 100
            # Store the coordinates in a tuple 
            click_coords = (x_coord, y_coord)
            # if it is the white players turn 
            if turn_step <= 1:
                if click_coords in white_locations:
                    # Make the selection variable equal to the coordinates of the selected piece 
                    selection = white_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                # if the selected piece is moved to a valid location, update its coordinates
                if click_coords in valid_moves and selection != 100: 
                    white_locations[selection] = click_coords
                    # Check to see if white is attempting to capture an enemy piece
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        black_captured_pieces.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    # Updated the valid moves available for each player
                    black_options = check_options(black_pieces, black_locations, 'black') 
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                # if the selected piece is moved to a valid location, update its coordinates
                if click_coords in valid_moves and selection != 100: 
                    black_locations[selection] = click_coords
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        white_captured_pieces.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = check_options(black_pieces, black_locations, 'black') 
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
