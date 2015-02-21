import bottle
import json
from board import Board

past_move = ""
head_position = ""

board_width = 0
board_height = 0





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


    global board_width
    global board_height
    board_width = data["width"]
    board_height = data["height"]

    print "Board: ", board_width, board_height

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
    
    if data["turn"] == 0:
        print "First turn"
        move = 'right'

    else:
        if canMove(head_position, 'right'):
            move = 'right'
        elif canMove(head_position, 'up'):
            move = 'up'
        else:
            move = 'left'
    

    past_move = move

    return json.dumps({
        'move': move,
        'taunt': 'battlesnake-python!'
    })


@bottle.post('/end')
def end():
    data = bottle.request.json

    return json.dumps({})




def myPosition(snakes):
    for s in snakes:
        if s["name"] == "Blank":
            return s["coords"][0]

def canMove(snake, m):

    if m == 'right':
        print "snake X: ", snake[0]
        print "Board Width: ", board_width

        print past_move

        if (snake[0] < board_width - 1) and past_move != 'left':
            return True

    elif m == 'up':
        print "snake Y:", snake[1]
        if (snake[1] > 0) and past_move != 'down':
            return True

    return False


# Expose WSGI app
application = bottle.default_app()
