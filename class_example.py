

class Character:
    def __init__(self, name, hp, mp, attack, magic, defense):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = attack
        self.mag = magic
        self.df = defense

    def attack(self, opponent):
        opponent.hp -= self.atk
        print(opponent.name + "'s hp fell to " + str(opponent.hp))

class Hero(Character):
    def __init__(self, name, hp, mp, attack, magic, defense, exp, level):
        super().__init__(name, hp, mp, attack, magic, defense)
        self.exp = exp
        self.level = level

    def lvl_up(self):
        if self.exp >= self.level * 100:
            self.level += 1
            print(self.name + " is now at level " + str(self.level))
            self.lvl_up()

class Enemy(Character):
    def __init__(self, name, hp, mp, attack, magic, defense):
        super().__init__(name, hp, mp, attack, magic, defense)
        

main_name = input("What is your name?\n")
main_char = Hero(main_name, 250, 20, 15, 10, 8, 150, 1)
side_name = input("What is your sidekick's name?\n")
side_char = Hero(side_name, 140, 10, 10, 5, 5, 0, 1)

print(main_char.name + " and " + side_char.name + " enter the evil forest...\n")

goblin = Enemy("Goblin", 40, 10, 10, 4, 5)

print(main_char.name + "'s attack is " + str(main_char.atk))
print(goblin.name + "'s attack is " + str(goblin.atk))

main_char.attack(goblin)

goblin.attack(main_char)

main_char.lvl_up()


