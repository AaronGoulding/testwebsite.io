//set up
let projectile: number[][] = []
let projectileNumber = 0
let paddleY = 2
let difficulty = 100
let points = 0
let randomY = 0
let inRow = false
//Begin game
game.startStopwatch()
led.plot(0, paddleY)
//Paddle Movement
input.onButtonPressed(Button.A, () => {
    if (paddleY != 4) {
        led.unplot(0, paddleY)
        paddleY += 1
        led.plot(0, paddleY)
    }
})
input.onButtonPressed(Button.B, () => {
    if (paddleY != 0) {
        led.unplot(0, paddleY)
        paddleY -= 1
        led.plot(0, paddleY)
    }
})

//projectiles
//Move right every 30 milliseconds
basic.forever(() => {
    if (game.currentTime() % 35 == 0) {
        for (let i = 0; i = projectileNumber - 1; i++) {
            if (projectile[i][0] != 0) {
                led.unplot(projectile[i][0], projectile[i][1])
                projectile[i][0] -= 1
            }
            if (projectile[i][0] == 0 && paddleY == projectile[i][1]) {
                points += 1
                projectile.removeAt(0);
                projectileNumber -= 1
            } else if (projectile[i][0] == 0 && paddleY != projectile[i][1]) {
                basic.clearScreen()
                basic.showString("GAME OVER!")
                basic.showNumber(points)
            }
            led.plot(projectile[i][0], projectile[i][1])
        }
    }
})
//Add a projectile every 60 milliseconds
basic.forever(() => {
    if (game.currentTime() % difficulty == 0) {
        if (difficulty >= 70) {
            difficulty -= 5
        }
        inRow = false
        for (let i = 0; i = projectileNumber - 1; i++) {
            if (projectile[i][0] == 4) {
                inRow = true
            }
        }
        if (inRow = false) {
            projectileNumber += 1
            randomY = Math.random(4)
            projectile.push([4, randomY])
        }
    }
})