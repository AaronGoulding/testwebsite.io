//set up
let ballX = 2
let ballY = 2
let velocityY = 1
let velocityX = 1
let paddleY = 2
let difficulty = 100
let points = 0
let ongoing = true
game.startStopwatch()
led.plot(0, paddleY)
//Paddle Movement
input.onButtonPressed(Button.A, () => {
    led.unplot(0, paddleY)
    paddleY += 1
    led.plot(0, paddleY)
})
input.onButtonPressed(Button.B, () => {
    led.unplot(0, paddleY)
    paddleY -= 1
    led.plot(0, paddleY)
})
//Ball Movement
basic.forever(() => {
    //Every "difficulty" milliseconds
    if (game.currentTime() % difficulty == 0) {
        //Remove current ball position
        led.unplot(ballX, ballY)
        //Would it hit the bat?
        if (ballX + velocityX == 0 && paddleY == ballY) {
            velocityX *= -1
            difficulty -= 10
            points += 1
        } else if (ballX + velocityX == 0 && paddleY != ballY) {
            basic.clearScreen()
            basic.showString("GAME OVER!!!")
            basic.showNumber(points)
        }
        //Bouncing off the walls
        if (ballX == 4) {
            velocityX *= -1
        }
        if (ballY == 0 || ballY == 4) {
            velocityY *= -1
        }
        //Update ball position
        ballX += velocityX
        ballY += velocityY
        led.plot(ballX, ballY)
    }
})
