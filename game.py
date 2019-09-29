import random
import math
 

class Warrior:
    def __init__(self, name="warrior", health=0, attkMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax
 
    def attack(self):
       
        attkAmt = (int(input("enter attak between 1 to 10 and then let other take turn: ")))
        if attkAmt > 11:
            print("disquilified only attaks between 1-10 , other player wins!")
        else:
            print("attacking")
        
        return attkAmt

    def block(self):

        blockAmt = 5 *(random.random())
 
        return blockAmt
 

class Battle:
 
    def startFight(self, warrior1, warrior2):
 
        # Continue looping until a Warrior dies switching back and
        # forth as the Warriors attack each other
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break
 
            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAAttkAmt = warriorA.attack()
 
        warriorBBlockAmt = warriorB.block()
 
        damage2WarriorB = math.ceil(warriorAAttkAmt - warriorBBlockAmt)
 
        warriorB.health = warriorB.health - damage2WarriorB
 
        print("{} attacks {} and deals {} damage".format(warriorA.name,
                                                         warriorB.name, damage2WarriorB))
 
        print("{} is down to {} health".format(warriorB.name,
                                               warriorB.health))
 
        if warriorB.health <= 0:
            print("{} has Died and {} is Victorious".format(warriorB.name,
                                                            warriorA.name))
 
            return "Game Over"
        else:
            return "Fight Again"
 
 
def main():

    player1= Warrior(input("enter player 1 name : "), 50, 20, 10)
    player2 = Warrior(input("enter player 2 name : "), 50, 20, 10)

    battle = Battle()

    battle.startFight(player1, player2)


main()
