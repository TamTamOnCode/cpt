def on_button_pressed_a():
    music.play_tone(165, music.beat(BeatFraction.HALF))
    if PaddleA.get(LedSpriteProperty.X) > 0:
        PaddleA.change(LedSpriteProperty.X, -1)
        PaddleB.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.play_tone(554, music.beat(BeatFraction.HALF))
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

def on_forever():
    music.play_melody("A F E F D G E F ", 120)
    music.play_melody("B G F G E A F G ", 120)
    music.play_melody("C5 A G A F B G A ", 120)
    music.play_melody("C B A B G C5 A B ", 120)
    music.play_melody("D C5 B C5 A C B C5 ", 120)
    music.play_melody("E C C5 C B D C5 C ", 120)
    music.play_melody("F D C D C5 E C D ", 120)
    music.play_melody("G E D E C F D E ", 120)
basic.forever(on_forever)

def on_forever2():
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
basic.forever(on_forever2)

def on_forever3():
    if Ball.is_touching(PaddleA) or Ball.is_touching(PaddleB):
        game.add_score(1)
basic.forever(on_forever3)
