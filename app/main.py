import bottle
import json


past_move = ""
head_position = ""

width = 0
height = 0

def setWidth(w):
    global width
    width = w

def setHeight(h):
    global height
    height = h


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

    setWidth(data["width"])
    setHeight(data["height"])

    print "Board: ", width, height

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
    
    global past_move

    past_move = move
    print "saved past move:" past_move

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
        print "Board Width: ", width
        print past_move

        if (snake[0] < width - 1) and past_move != 'left':
            return True

    elif m == 'up':
        print "snake Y:", snake[1]
        if (snake[1] > 0) and past_move != 'down':
            return True

    return False


# Expose WSGI app
application = bottle.default_app()
