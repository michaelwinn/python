import time


class Ball():
    def __init__(self, mass, density, velocity, x0, y0):
        self.mass = mass
        self.density = density
        self.velocity = velocity
        self.volume = mass / density
        self.x0 = x0
        self.y0 = y0
        self.x = x0
        self.y = y0
        self.position = [x0, y0]

    def move(self, t, a):
        try:
            while True:
                self.x = self.x0 + self.velocity[0] * t
                self.y = self.y0 + self.velocity[1] * t + 1/2 * a * t ** 2
                self.position = [self.x, self.y]
                print(str(self.x) + ", " + str(self.y))
                t = t + 0.1
                time.sleep(0.1)
##                self.move(t, a)
        except KeyboardInterrupt:
            print("End of the line...")


new_ball = Ball(0.25, 1.0, [1, 10], 0.0, 0.0)
new_ball.move(0, -9.81)

old_ball = Ball(0.5, 1.0, [0.5, 15], 0.0, 0.0)
old_ball.move(0, -9.81)

