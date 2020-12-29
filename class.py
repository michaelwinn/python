import random

class MyClass():
    def __init__(self, name, fav_color):
        self.name = name
        self.fav_color = fav_color


class Eight_ball():
    def __init__(self, sides, dist):
        self.sides = sides
        self.dist = dist

    def shake(self):
        answers = ('yes', 'no', 'try again', 'not likely', 'looks promising', /
                   'reply')


michael = MyClass('michael', 'green')

print(michael.fav_color)

