import bottle
import json
from board import Board

past_move = ""
head_position = ""

board = Board(0,0)



def myPosition(snakes):
    for s in snakes:
        if s["name"] == "Blank":
            return s["coords"][0]

def canMove(snake, m):
    global board
    if m == 'right':
        print "snake X: ", snake[0]
        print "Board Width: ", board.width

        if (snake[0] < board.width - 1) and past_move != 'left':
            return True

    return False



@bottle.get('/')
def index():
    return """
        <a href="https://github.com/sendwithus/battlesnake-python">
            battlesnake-python
        </a>
    """


@bottle.post('/start')
def start():
    data = bottle.request.json

    global board

    board.width = data["width"]
    board.height = data["height"]

    print "Board: ", board.width, board.height

    return json.dumps({
        'name': 'Blank',
        'color': '#566AE4',
        'head_url': 'http://battlesnake-python.herokuapp.com',
        'taunt': 'battlesnake-python!'
    })


@bottle.post('/move')
def move():
    data = bottle.request.json
    move = ""

    head_position = myPosition(data["snakes"])
    
    if data["turn"] == 1:
        
        print "head position", head_position

    else:
        if canMove(head_position, 'right'):
            move = 'right'
        else:
            move = 'up'
    



    return json.dumps({
        'move': move,
        'taunt': 'battlesnake-python!'
    })


@bottle.post('/end')
def end():
    data = bottle.request.json

    return json.dumps({})


# Expose WSGI app
application = bottle.default_app()
