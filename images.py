
import pygame

# Load all the images of the pieces  
black_queen = pygame.image.load('chess_pieces/black queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
small_black_queen = pygame.transform.scale(black_queen, (40, 40))

black_king  = pygame.image.load('chess_pieces/black king.png')
black_king  = pygame.transform.scale(black_king,(80, 80) )
small_black_king  = pygame.transform.scale(black_king,(40, 40) )

black_bishop = pygame.image.load('chess_pieces/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
small_black_bishop = pygame.transform.scale(black_bishop, (40, 40))

black_knight = pygame.image.load('chess_pieces/black knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
small_black_knight= pygame.transform.scale(black_knight, (40, 40))

black_rook   = pygame.image.load('chess_pieces/black rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
small_black_rook = pygame.transform.scale(black_rook, (40, 40))

black_pawn = pygame.image.load('chess_pieces/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
small_black_pawn = pygame.transform.scale(black_pawn, (40, 40))

white_queen = pygame.image.load('chess_pieces/white queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
small_white_queen = pygame.transform.scale(white_queen, (40, 40))

white_king  = pygame.image.load('chess_pieces/white king.png')
white_king  = pygame.transform.scale(white_king, (80, 80) )
small_white_king  = pygame.transform.scale(white_king,(40, 80) )

white_bishop = pygame.image.load('chess_pieces/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
small_white_bishop = pygame.transform.scale(white_bishop, (40, 40))

white_knight = pygame.image.load('chess_pieces/white knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
small_white_knight = pygame.transform.scale(white_knight, (40, 40))

white_rook   = pygame.image.load('chess_pieces/white rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
small_white_rook = pygame.transform.scale(white_rook, (40, 40))

white_pawn = pygame.image.load('chess_pieces/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
small_white_pawn = pygame.transform.scale(white_pawn, (40, 40))
