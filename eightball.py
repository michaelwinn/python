import random


class Eight_ball():
    def __init__(self, sides=6, dist='none'):
        self.sides = sides
        self.dist = dist

    def shake(self):
        answers = ('yes', 'no', 'try again', 'not likely', 'looks promising', \
                   'reply murky\ntry again')
        print(answers[random.randint(0,len(answers)-1)])


def main():
    eightball = Eight_ball()
    question = input("Ask the eight ball a question:\n")
    eightball.shake()


if __name__ == '__main__':
    main()


