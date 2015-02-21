import bottle
import json

past_move = ""
head_position = ""
width = 0
height = 0


def myPosition(snakes):
    for s in snakes:
        if s["name"] == "Blank":
            return s["coords"][0]

def canMove(snake, m):
    if m == 'right':
        print snake[0], str(width -1 ), past_move
        if (snake[0] < width - 1) and past_move != 'left':
            return true



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

    width = data["width"]
    height = data["height"]

    print "width", width
    print "height", height

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


    if data["turn"] == 1:
        head_position = myPosition(data["snakes"])
        print "head position", head_position
        if canMove(head_position, 'right'):
            move = 'right'
        else:
            move = 'up'



    past_move = move
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
