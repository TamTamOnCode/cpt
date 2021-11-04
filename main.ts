input.onButtonPressed(Button.A, function () {
    if (PaddleA.get(LedSpriteProperty.X) > 0) {
        PaddleA.change(LedSpriteProperty.X, -1)
        PaddleB.change(LedSpriteProperty.X, -1)
    }
})
input.onButtonPressed(Button.B, function () {
    if (PaddleA.get(LedSpriteProperty.X) < 3) {
        PaddleA.change(LedSpriteProperty.X, 1)
        PaddleB.change(LedSpriteProperty.X, 1)
    }
})
let PaddleB: game.LedSprite = null
let PaddleA: game.LedSprite = null
PaddleA = game.createSprite(2, 4)
PaddleB = game.createSprite(3, 4)
let Ball = game.createSprite(randint(0, 4), 0)
let DirectionY = 1
let DirectionX = randint(-1, 1)
game.setScore(0)
basic.pause(500)
loops.everyInterval(20, function () {
    music.playMelody("B A G A G F E C ", 120)
})
basic.forever(function () {
    Ball.change(LedSpriteProperty.X, DirectionX)
    Ball.change(LedSpriteProperty.Y, DirectionY)
    if (Ball.isTouching(PaddleA) || Ball.isTouching(PaddleB)) {
        Ball.change(LedSpriteProperty.X, DirectionX * -1)
        Ball.change(LedSpriteProperty.Y, -1)
        DirectionY = -1
        DirectionX = randint(-1, 1)
    } else {
        if (Ball.get(LedSpriteProperty.Y) <= 0) {
            DirectionY = 1
            DirectionX = randint(-1, 1)
        } else if (Ball.get(LedSpriteProperty.Y) >= 4) {
            Ball.set(LedSpriteProperty.Blink, 1)
            basic.pause(2000)
            game.gameOver()
        }
        if (Ball.get(LedSpriteProperty.X) <= 0) {
            DirectionX = 1
        } else if (Ball.get(LedSpriteProperty.X) >= 4) {
            DirectionX = -1
        }
        basic.pause(500)
    }
})
basic.forever(function () {
    if (Ball.isTouching(PaddleA) || Ball.isTouching(PaddleB)) {
        game.addScore(1)
    }
})
