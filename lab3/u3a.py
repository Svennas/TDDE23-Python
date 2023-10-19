
# skapar ett nytt spelbräde
def new_board():
    board = {}
    return board


# kollar om en viss plats är ledig
def is_free(board, x, y):
    for elem in board:
        if (elem == x):
            if (board[x] == y):
                return False
    return True


# placerar en figur på en plats
def place_piece(board, x, y, key): 
    if (is_free(board, x, y)):
        board[key] = (x, y)
        return True
    return False


# returnerar pjäsen på en viss plats
def get_piece():
    return 1


# ta bort pjäsen på en viss plats
def remove_piece():
    return 1

# flytta en pjäs mellan två platser
def move_piece():
    return 1 

# returnera hur många pjäser det är på en plats
def count():
    return 1


# returnera den närmsta pjäsen, och finns det fler pjäser på samma avstånd är det fritt att välja vilken som
def nearest_piece():
    return 1