import random


count_animals_for_every_player = {}

class Animal:
    pass

class Player:
    def __init__(self, name, dice1, dice2):
        self.name = name
        self.dice1 = dice1
        self.dice2 = dice2

    def throws_dices(self):
        random.shuffle(self.dice1)
        random.shuffle(self.dice2)
        result = (self.dice1[0], self.dice2[0])
        result_str = ', '.join(result)
        #return random.choice(self.animal)
        return result_str

 

class Cards:
    pass

class Dogs(Animal):
    pass

class Fox(Animal):
    pass
class Bear(Animal):
    pass

class CollectedAnimal(Animal):
    pass

def random_animal(name, result):
    count_animals_for_every_player[name] = result
    print(count_animals_for_every_player)    


def main():

    

    #while True:
    # ch_what_to_do = input("Welcome to SuperFerma Game: S-start, E-exit:> ")
    # if ch_what_to_do == 'S' or ch_what_to_do =='s':
    #     print('Start Game')
    # elif ch_what_to_do == 'E' or ch_what_to_do == 'e':
    #     print('Good Bye')
        #break

    dice1 = ['duck', 'fox', 'duck', 'sheep', 'duck', 'horse', 'duck', 'pig']
    dice2 = ['duck', 'bear', 'duck', 'sheep', 'duck', 'horse', 'duck', 'pig']


    player1 = Player('Olya', dice1, dice2)


    
    random_animal(player1.name, player1.throws_dices())

if __name__ == '__main__':
    main()
