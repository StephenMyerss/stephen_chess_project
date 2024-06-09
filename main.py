# Programmer:   Stephen Myers
# Program:      Personal Project
# Due Date:     02/13/2024
# Synopsis:     This program implements a two player chess game using the pygame module.
#               The player should have a general idea of the rules of chess prior to playing this game

import pygame
from images import*
pygame.init()

#game window 
WIDTH = 1150 
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2 Player Chess Game")

# Define variables to keep track of whos turn it is and selection is used to determine which piece is selected 
turn_step = 0
selection = 100

# Create lists to hold all the sqaures that make the chess board
black_squares = []
white_squares = []
# Create lists to hold captured pieces and places where pieces can move 
valid_moves   = []
white_captured_pieces = []
black_captured_pieces = []
captured_pieces = []
check = False
by = 1.5
bby = by + 0.9
black_captured_locations = [(8, by),     (8.4, by),   (8.8, by),
                            (9.2, by),   (9.6, by),   (10,by),
                            (10.4, by),  (10.8, by),  (8, bby),
                            (8.4, bby),  (8.8, bby),  (9.2, bby),
                            (9.6, bby),  (10, bby),   (10.4, bby),
                            (10.8, bby)]
wy = 6
wwy = wy + 0.9
white_captured_locations = [(8, wy),     (8.4, wy),   (8.8, wy),
                            (9.2, wy),   (9.6, wy),   (10, wy),
                            (10.4, wy),  (10.8, wy),  (8, wwy),
                            (8.4, wwy), (8.8, wwy), (9.2, wwy),
                            (9.6, wwy), (10, wwy),  (10.4, wwy),
                            (10.8, wwy)]

# Create lists to hold the pieces and thier locations 
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn',   'pawn',   'pawn', 'pawn',  'pawn',   'pawn',   'pawn']

black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7,7),
                  (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn',   'pawn',   'pawn', 'pawn',  'pawn',   'pawn',   'pawn']
                
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                  (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7,1)]


#---------------------------------------------------------------------------------------------
def draw_pieces():
    for i in range(len(black_pieces)):
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * 100 + 15, black_locations[i][1] * 100 + 25))
        elif black_pieces[i] == 'rook':
            screen.blit(black_rook, (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 20))
        elif black_pieces[i] == 'knight':
            screen.blit(black_knight, (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 20))
        elif black_pieces[i] == 'bishop':
            screen.blit(black_bishop, (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 20))
        elif black_pieces[i] == 'queen':
            screen.blit(black_queen, (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 20))
        elif black_pieces[i] == 'king':
            screen.blit(black_king, (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 20))
        # Draw red outline around the piece a player has selectd to move 
        if turn_step >=2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1, 
                                  100, 100], 3)
            
    for i in range(len(white_pieces)):
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0] * 100 + 15, white_locations[i][1] * 100 + 25))
        elif white_pieces[i] == 'rook':
            screen.blit(white_rook, (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))
        elif white_pieces[i] == 'knight':
            screen.blit(white_knight, (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))
        elif white_pieces[i] == 'bishop':
            screen.blit(white_bishop, (white_locations[i][0] * 100 + 10,white_locations[i][1] * 100 + 10))
        elif white_pieces[i] == 'queen':
            screen.blit(white_queen, (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))
        elif white_pieces[i] == 'king':
            screen.blit(white_king, (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))
        if turn_step <= 1:
            if selection == i:
             pygame.draw.rect(screen, 'red', [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1, 
                                  100, 100], 2)            

# This function creates all the black squares and adds them to the list 
def create_black_squares():
    sx = 0
    sy = 0
    i = 2
    while sy < 800:   
        black_square = pygame.Rect(sx, sy, 100, 100)
        black_squares.append(black_square)
        sx += 200
        if sx > 700:
            sy += 100
            if i % 2 == 0:
                sx = 100
                i += 1
            else:
                sx = 0
                i += 1
 # This function creates all the white squares and addes them to the list 
def create_white_squares():
    wsx = 100
    wsy = 0
    i = 2
    while wsy < 800:
        white_square = pygame.Rect(wsx, wsy, 100, 100)
        white_squares.append(white_square)
        wsx += 200
        if wsx > 700:
            wsy += 100
            if i % 2 == 0:
                wsx = 0
                i += 1
            else:
                wsx = 100
                i += 1
def draw_board():
    for black_square in black_squares:
        pygame.draw.rect(screen, 'Black', black_square)
    for white_square in white_squares:
        pygame.draw.rect(screen, 'White', white_square)
#----------------------------------------------------------------------------------------
# Check valid pawn moves
def check_pawn(position, color):
    
    moves_list = []
    if color == 'white':
        # Move forward one square if available
        if (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7 and position[1] >= 1:
            moves_list.append((position[0], position[1] + 1))
        # Move foreward 2 sqaures if move is first move
        if (position[0], position[1] + 2) not in white_locations and \
                (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        # Attack Diagonally to the right if an enemy piece is there 
        if(position[0] + 1, position[1] + 1 ) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        # Attack Diagonllay to the left is an enemy piece is there 
        if(position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0] ,position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if(position[0] + 1, position[1] - 1, ) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if(position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list
#-------------------------------------------------------------------------------------------------
# A function to check the valid moves for the rook 
def check_rook(location, color):
    moves_list = [] 
    if color == 'white':
        friends_list = white_locations
        enemies_list = black_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # Check the 4 different move options:  Up, down, left, right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for direction in directions:
        dx = direction[0]
        dy = direction[1]
        while (0 <= (location[0] + dx) <= 7) and (0 <= (location[1] + dy) <= 7):
            if(((location[0] + dx, location[1] + dy) in friends_list)):
                break
            elif((location[0] + dx, location[1] + dy) in enemies_list):
                moves_list.append((location[0] + dx, location[1] + dy))
                break
            else:
                moves_list.append((location[0] + dx, location[1] + dy))
            if dx < 0:
                dx = dx + -1
            if dy < 0:
                dy = dy + -1
            if dx > 0:
                dx = dx + 1
            if dy > 0:
                dy = dy + 1 
    return moves_list
#----------------------------------------------------------------------------------------
def king_check_rook(location, color):
    moves_list = [] 
    if color == 'white':
        friends_list = white_locations
        enemies_list = black_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # Check the 4 different move options:  Up, down, left, right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for direction in directions:
        dx = direction[0]
        dy = direction[1]
    
        while (0 <= (location[0] + dx) <= 7) and (0 <= (location[1] + dy) <= 7):
            if(((location[0] + dx, location[1] + dy) in friends_list)):
                moves_list.append((location[0] + dx, location[1] + dy))
                break
            else:
                moves_list.append((location[0] + dx, location[1] + dy))
            if dx < 0:
                dx = dx + -1
            if dy < 0:
                dy = dy + -1
            if dx > 0:
                dx = dx + 1
            if dy > 0:
                dy = dy + 1 
    return moves_list
#----------------------------------------------------------------------------------------------
def king_check_bishop(location, color):
    moves_list = []
    if color == 'white':
        friends_list = white_locations
        enemies_list = black_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # Generate the directions a bishop can move IE if a biship is at positon (3,3) it could move to 
    # positon (x - 1, y -1) (x + 1, y + 1), (x + 1, y -1), and (x - 1, y + 1)
    directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    for direction in directions:
        dx = direction[0]
        dy = direction[1]
    
        while (0 <= (location[0] + dx) <= 7) and (0 <= (location[1] + dy) <= 7):
            
            if ((location[0] + dx, location[1] + dy)) in friends_list:
                moves_list.append((location[0] + dx, location[1] + dy))
                break
            else:
                moves_list.append((location[0] + dx, location[1] + dy))
            # updated the loop control variables, while account for negative values
            if dx < 0:
                dx = dx + -1
            else:
                dx = dx + 1
            if dy < 0:
                dy = dy + -1
            else:
                dy = dy + 1
                
    return moves_list
#-----------------------------------------------------------------------------------------------------           
def check_bishop(location, color):
    moves_list = []
    if color == 'white':
        friends_list = white_locations
        enemies_list = black_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # Generate the directions a bishop can move IE if a bishop is at positon (3,3) it could move to 
    # positon (x - 1, y -1) (x + 1, y + 1), (x + 1, y -1), and (x - 1, y + 1)
    directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    for direction in directions:
        dx = direction[0]
        dy = direction[1]
    
        while (0 <= (location[0] + dx) <= 7) and (0 <= (location[1] + dy) <= 7):
            
            if ((location[0] + dx, location[1] + dy)) in friends_list:
                break
            elif ((location[0] + dx, location[1] + dy)) in enemies_list:
                moves_list.append((location[0] + dx, location[1] + dy))
                break
            else:
                moves_list.append((location[0] + dx, location[1] + dy))
            # updated the loop control variables, while account for negative values
            if dx < 0:
                dx = dx + -1
            else:
                dx = dx + 1
            if dy < 0:
                dy = dy + -1
            else:
                dy = dy + 1
                
    return moves_list    
#------------------------------------------------------------------------------------
# the queen's moves are a combination of the rook and bishops moves
# so just make a list for each and use the functions already made 
# and add the 2 lists together 
def check_queen(location, color):
    moves_list = []
    second_list = []
    moves_list = check_rook(location, color)
    second_list = check_bishop(location, color)
    # Combine the two lists into one list 
    moves_list.extend(second_list)
        
    return moves_list
#--------------------------------------------------------------------------
def king_check_queen(location, color):
    moves_list = []
    second_list = []
    moves_list = king_check_rook(location, color)
    second_list = king_check_bishop(location, color)
    # Combine the two lists into one list 
    moves_list.extend(second_list)
        
    return moves_list
#--------------------------------------------------------------------------------------
def check_knight(location, color):
    moves_list = []
    if color == 'white':
        friends_list = white_locations
        enemies_list = black_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # Account for all 8 places  the knight can move 
    directions = [(2, 1), (2, -1), (-2, 1), (-2, -1),(1, 2), (-1, 2), (1, -2), (-1, -2)]
    
    for direction in directions:
        dx = direction[0]
        dy = direction[1]
        
        if( (0 <= location[0] + dx <= 7) and (0 <= location[1] + dy <= 7) ):
            if((location[0] + dx, location[1] + dy) not in friends_list):
                moves_list.append((location[0] + dx, location[1] + dy))
            
    return moves_list
#---------------------------------------------------------------------------------------
def king_check_knight(location, color):
    moves_list = []
    if color == 'white':
        friends_list = white_locations
        enemies_list = black_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # Account for all 8 places  the knight can move 
    directions = [(2, 1), (2, -1), (-2, 1), (-2, -1),(1, 2), (-1, 2), (1, -2), (-1, -2)]
    
    for direction in directions:
        dx = direction[0]
        dy = direction[1]
        
        if( (0 <= location[0] + dx <= 7) and (0 <= location[1] + dy <= 7) ):
                moves_list.append((location[0] + dx, location[1] + dy))
            
    return moves_list
#-----------------------------------------------------------------------------------
def check_king(location, color ):
    moves_list = []
    invalid_moves = []
    if color == 'white':
        friends_list = white_locations
        enemies_list = black_locations
        enemy_pieces = black_pieces
        enemy_color = 'black'
    else:
        friends_list = black_locations
        enemies_list = white_locations
        enemy_pieces = white_pieces
        enemy_color = 'white'

    for i in range(len(enemy_pieces)):
        piece = enemy_pieces[i]
        enemy_location = enemies_list[i]
        
        if piece == 'pawn':
            invalid_moves.extend(check_pawn_diagonal(enemy_location, enemy_color))
        elif piece == 'rook':
            invalid_moves.extend(king_check_rook(enemy_location, enemy_color))
        elif piece == 'bishop':
            invalid_moves.extend(king_check_bishop(enemy_location, enemy_color))
        elif piece == 'queen':
            invalid_moves.extend(king_check_queen(enemy_location, enemy_color))
        elif piece == 'knight':
            invalid_moves.extend(king_check_knight(enemy_location, enemy_color))
        # This if is needed to handle the special case involving a king and king moving 
        # toward each other and to prevent the king from being able to move himself into check
        elif piece == 'king':
            enemy_king_moves = []
            directions = [(1,0), (0,1), (1, 1), (-1, 0), (0, -1), (-1, 1), (1, -1), (-1, -1)]
            for direction in directions:
                dx = direction[0]
                dy = direction[1]
                if( (0 <= enemy_location[0] + dx <= 7) and (0 <= enemy_location[1] + dy <= 7)):
                    enemy_king_moves.append((enemy_location[0] + dx, enemy_location[1] + dy))

            invalid_moves.extend(enemy_king_moves)

    # Store the 8 possible directions a king can move 
    directions = [(1,0), (0,1), (1, 1), (-1, 0), (0, -1), (-1, 1), (1, -1), (-1, -1)]
    
    for direction in directions:
        dx = direction[0]
        dy = direction[1]
        
        if( (0 <= location[0] + dx <= 7) and (0 <= location[1] + dy <= 7)):
            if ((location[0] + dx, location[1] + dy) not in friends_list):
                if ((location[0] + dx, location[1] + dy) not in invalid_moves):
                    moves_list.append((location[0] + dx, location[1] + dy))
                    
    return moves_list
#--------------------------------------------------------------------------------------
"""
def enforce_check_move(king_location, color ):
    moves_list = []
    piece_move_list = []
    if color == 'white':
        friends_list = white_locations
        enemies_list = black_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
        
    if color == 'white':
       location = king_location
       directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for direction in directions:
        dx = direction[0]
        dy = direction[1]
        #check if enemy piece is a queen or rook that is putting king in check
        while (0 <= (location[0] + dx) <= 7) and (0 <= (location[1] + dy) <= 7):
            if(((location[0] + dx, location[1] + dy) in friends_list)):
                break
            elif((location[0] + dx, location[1] + dy) in enemies_list and  )):
                moves_list.append((location[0] + dx, location[1] + dy))
                break
            else:
                moves_list.append((location[0] + dx, location[1] + dy))
            if dx < 0:
                dx = dx + -1
            if dy < 0:
                dy = dy + -1
            if dx > 0:
                dx = dx + 1
            if dy > 0:
                dy = dy + 1 
       
    else:
       black_king_location = king_location
           
    
"""
            
# This functions checks if the king is in check 
#---------------------------------------------------------------------------------
def check(check): 
    moves_list = []
    font = pygame.font.Font(None, 30)
    if turn_step < 2:
        if 'king' in white_pieces:
            color = 'white'
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    check = True
                    text = 'White King is in check!'
                    text_color = 'dark red'
                    pygame.draw.rect(screen, 'orange', [white_locations[king_index][0] * 100 + 1,
                                                            white_locations[king_index][1] * 100 + 1, 100, 100], 10)
                    text_surface = font.render(text, True, text_color )
                    text_rect = text_surface.get_rect()
                    screen.blit(text_surface, (825, 50))
                    
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    check = True
                    text = 'Black king is in check!'
                    text_color = 'dark red'
                    pygame.draw.rect(screen, 'orange', [black_locations[king_index][0] * 100 + 1,
                                                            black_locations[king_index][1] * 100 + 1, 100, 100], 10)
                    text_surface = font.render(text, True, text_color )
                    text_rect = text_surface.get_rect()
                    screen.blit(text_surface, (825, 50))                               
#-------------------------------------------------------------------------------------------
# This function is needed to get all the attack paths of enemy pawns for the invalid moves
# list in the check king function to prevent the king from being able to be moved into check
def check_pawn_diagonal(location, color):
    moves_list = []
    
    #check if the white pawn can attack diagonally
    if color == 'white':
        dy = 1
        if (  0 < (location[0] - 1 <= 7 and location[1] + 1 < 7) ):
            moves_list.append((location[0] - 1, location[1] + 1))
        if ( (0 <= location[0] + 1 <= 6  and location[1] + 1 < 7)):
            moves_list.append((location[0] + 1, location[1] + 1))
    
    else :
        if(( 0 < location[0] - 1 <= 7 and   0 < location[1] - 1) < 7 ):
            moves_list.append((location[0] - 1, location[1] - 1))
        if (( 0 <= location[0] + 1 and  0 < location[1] - 1 < 7 )):
            moves_list.append((location[0] + 1, location[1] -1))

    return moves_list
 
# A function to check all the pieces valid options on the board
def check_options(pieces, locations, color):
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
         moves_list = check_pawn(location, color)
        elif piece == 'rook':
            moves_list = check_rook(location, color)
        elif piece == 'bishop':
            moves_list = check_bishop(location, color)
        elif piece == 'queen':
            moves_list = check_queen(location, color)
        elif piece == 'knight':
            moves_list = check_knight(location, color)
        elif piece == 'king':
            moves_list = check_king(location, color)
        all_moves_list.append(moves_list)
    
    return all_moves_list
#----------------------------------------------------------------------------------
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options
#----------------------------------------------------------------------------------
def draw_valid_moves(valid_moves_list):
    valid_moves = valid_moves_list
    if turn_step < 2:
        color = 'Red'
    else:
        color = 'Blue'
    for move in valid_moves:
        pygame.draw.circle(screen, color, (move[0] * 100 + 50, move[1] * 100 + 50), 10)
#----------------------------------------------------------------------------------------
def display_turn():
    font = pygame.font.Font(None, 40)
    if turn_step <= 1:
        text = "White's turn"
        text_color = 'White'
    else:
        text = "Black's turn"
        text_color = 'Black'
    text_surface = font.render(text, True, text_color )
    text_rect = text_surface.get_rect()
    screen.blit(text_surface, (825, 0))
#---------------------------------------------------------------------------
def draw_captured_pieces():
    for i in range(len(black_captured_pieces)):
        if black_captured_pieces[i] == 'pawn':
            screen.blit(small_black_pawn, (black_captured_locations[i][0] * 100 , black_captured_locations[i][1] * 50 ))
        elif black_captured_pieces[i] == 'rook':
            screen.blit(small_black_rook, (black_captured_locations[i][0] * 100 , black_captured_locations[i][1] * 50 ))
        elif black_captured_pieces[i] == 'knight':
            screen.blit(small_black_knight, (black_captured_locations[i][0] * 100, black_captured_locations[i][1] * 50 ))
        elif black_captured_pieces[i] == 'bishop':
            screen.blit(small_black_bishop, (black_captured_locations[i][0] * 100 , black_captured_locations[i][1] * 50 ))
        elif black_captured_pieces[i] == 'queen':
            screen.blit(small_black_queen, (black_captured_locations[i][0] * 100 , black_captured_locations[i][1] * 50 ))
        elif black_captured_pieces[i] == 'king':
            screen.blit(small_black_king, (black_captured_locations[i][0] * 100 , black_captured_locations[i][1] * 50 ))
            
            
    for i in range(len(white_captured_pieces)):
        if white_captured_pieces[i] == 'pawn':
            screen.blit(small_white_pawn, (white_captured_locations[i][0] * 100 , white_captured_locations[i][1] * 50 ))
        elif white_captured_pieces[i] == 'rook':
            screen.blit(small_white_rook, (white_captured_locations[i][0] * 100 , white_captured_locations[i][1] * 50 ))
        elif white_captured_pieces[i] == 'knight':
            screen.blit(small_white_knight, (white_captured_locations[i][0] * 100, white_captured_locations[i][1] * 50 ))
        elif white_captured_pieces[i] == 'bishop':
            screen.blit(small_white_bishop, (white_captured_locations[i][0] * 100 , white_captured_locations[i][1] * 50 ))
        elif white_captured_pieces[i] == 'queen':
            screen.blit(small_white_queen, (white_captured_locations[i][0] * 100 , white_captured_locations[i][1] * 50 ))
        elif white_captured_pieces[i] == 'king':
            screen.blit(small_white_king, (white_captured_locations[i][0] * 100 , white_captured_locations[i][1] * 50 ))
            
            
FPS = 60
create_black_squares()
create_white_squares()
black_options = check_options(black_pieces, black_locations, 'black') 
white_options = check_options(white_pieces, white_locations, 'white')
# Main Game loop 
run = True 
while run:
    screen.fill('grey')
    #draw the black squares on to the screen 
    draw_board()
    draw_pieces()
    display_turn()
    draw_captured_pieces()
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
