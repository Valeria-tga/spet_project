
board={
    'top-L': '',
    'mid-L': '',
    'low-L': '',
    'top-M': '',
    'mid-M': '',
    'low-M': '',
    'top-R': '',
    'mid-R': '',
    'low-R': '',
}

def printBoard(board):
    print(f'  {board['top-L']} | {board['top-M']} | {board['top-R']}')
    print(f' --+--+-- ')
    print(f'  {board['mid-L']} | {board['mid-M']} | {board['mid-R']}')
    print(f' --+--+-- ')
    print(f'  {board['low-L']} | {board['low-M']} | {board['low-R']}')
    print(f' --+--+-- ')

printBoard(board)