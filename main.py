def on_button_pressed_a():
    if PaddleA.get(LedSpriteProperty.X) > 0:
        PaddleA.change(LedSpriteProperty.X, -1)
        PaddleB.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if PaddleA.get(LedSpriteProperty.X) < 3:
        PaddleA.change(LedSpriteProperty.X, 1)
        PaddleB.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

PaddleB: game.LedSprite = None
PaddleA: game.LedSprite = None
PaddleA = game.create_sprite(2, 4)
PaddleB = game.create_sprite(3, 4)
Ball = game.create_sprite(randint(0, 4), 0)
DirectionY = 1
DirectionX = randint(-1, 1)
game.set_score(0)
basic.pause(500)

def on_every_interval():
    music.play_melody("B A G A G F E C ", 120)
loops.every_interval(20, on_every_interval)

def on_forever():
    global DirectionY, DirectionX
    Ball.change(LedSpriteProperty.X, DirectionX)
    Ball.change(LedSpriteProperty.Y, DirectionY)
    if Ball.is_touching(PaddleA) or Ball.is_touching(PaddleB):
        Ball.change(LedSpriteProperty.X, DirectionX * -1)
        Ball.change(LedSpriteProperty.Y, -1)
        DirectionY = -1
        DirectionX = randint(-1, 1)
    else:
        if Ball.get(LedSpriteProperty.Y) <= 0:
            DirectionY = 1
            DirectionX = randint(-1, 1)
        elif Ball.get(LedSpriteProperty.Y) >= 4:
            Ball.set(LedSpriteProperty.BLINK, 1)
            basic.pause(2000)
            game.game_over()
        if Ball.get(LedSpriteProperty.X) <= 0:
            DirectionX = 1
        elif Ball.get(LedSpriteProperty.X) >= 4:
            DirectionX = -1
        basic.pause(500)
basic.forever(on_forever)

def on_forever2():
    if Ball.is_touching(PaddleA) or Ball.is_touching(PaddleB):
        game.add_score(1)
basic.forever(on_forever2)
