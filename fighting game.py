#Combat game where 2 players have their own party of different party members
#Parent class with generic attributes (health, armor)
#Specialized classes (healer, fighter) that have unique abilities
from random import randint
my_team = []
enemy_team = []
class Generic:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def getName(self):
        return self.name

    def getHealth(self):
        return int(self.health)
    
    def setHealth(self, h):
        self.health = h
    
    def emote(self):
        print("{} does a little jig".format(self.name))


class Fighter(Generic):
    def __init__(self, name, power, health, crit):
        super().__init__(name, health)
        self.power = power
        self.crit = crit

    def getCrit(self):
        return self.crit
    
    def getPower(self):
        return self.power
    
    def __repr__(self):
        return ("\"My name is {} and I have a power level of {}!\"".format(self.name, self.power))
    

class Healer(Generic):
    def __init__(self, name, healing, health, power):
        super().__init__(name, health)
        self.healing = healing
        self.power = power
    def getHealing(self):
        return self.healing
    def getPower(self):
        return self.power
    
    def __repr__(self):
        return ("My name is {} and I can healing ability of {}!".format(self.name, self.healing))
    
def makeMove(char, enemy_team, my_team):
    if isinstance(char, Fighter):
        move = input("{} has current move set: \n1. Attack \n2. Dance \nChoose your move: ".format(char.getName()))
        if move == '1':
            for i in range(len(enemy_team)):
                print("Enter {} to attack {}".format(i+1, enemy_team[i].getName()))
            target = int(input("Choose target to attack: ")) -1
            enemy = enemy_team[target]
            num = enemy.getHealth() - char.getPower()
            enemy.setHealth(num)
            print("{} does {} damage to {}".format(char.getName(), char.getPower(), enemy.getName()))
            crit_chance = randint(1, 10)
            if crit_chance <= char.getCrit():
                num = enemy.getHealth() - char.getPower()
                enemy.setHealth(num)
                print("{} does a critical hit doing double damage!".format(char.getName()))
            if enemy.getHealth() <= 0:
                del enemy_team[target]
                print("{} has been slain!".format(enemy.getName()))
            else:
                print("{} has {} health remaining".format(enemy.getName(), enemy.getHealth()))
        elif move == '2':
            char.emote()
        else:
            makeMove(char, enemy, my_team)
    if isinstance(char, Healer):
        move = input("{} has current move set: \n1. Attack\n2. Heal\n3. Dance \nChoose your move: ".format(char.getName()))
        if move == '1':
            for i in range(len(enemy_team)):
                print("enter {} to attack {}".format(i+1, enemy_team[i].getName()))
            target = int(input("Choose target to attack: ")) -1
            enemy = enemy_team[target]
            num = enemy.getHealth() - char.getPower()
            enemy.setHealth(num)
            print("{} does {} damage to {}".format(char.getName(), char.getPower(), enemy.getName()))
            print("{} has {} health remaining".format(enemy.getName(), enemy.getHealth()))
        elif move == '2':
            print("You can heal 1 of {} characters".format(len(my_team)))
            for i in range(len(my_team)):
                print("enter {} to heal {}".format(i+1, my_team[i].getName()))
            target = int(input("Choose target to heal: ")) -1
            num = my_team[target].getHealth() + char.getHealing()
            my_team[target].setHealth(num)
            print("{} now has {} health".format(my_team[target].getName(), my_team[target].getHealth()))
        elif move == '3':
            char.emote()
        else:
            makeMove(char, enemy, my_team)
                
def genEnemyTeam(numEnemies):
    for i in range(numEnemies):
        power = 3 + randint(0, 5)
        health = 20 + randint(0, 15)
        crit = 1 + randint(0, 2)
        name = 'Enemy ' + str(i+1)
        enemy_team.append(Fighter(name, power, health, crit))

def enemyMoves(my_team, enemy_team):
    for i in range(len(enemy_team)):
        enemy = enemy_team[i]
        target = randint(0, len(my_team)-1)
        num = my_team[target].getHealth() - enemy.getPower()
        my_team[target].setHealth(num)
        print("{} did {} damage to {} leaving them at {} health".format(enemy.getName(), enemy.getPower(), my_team[target].getName(), my_team[target].getHealth()))
        if my_team[target].getHealth() <= 0:
            del my_team[target]
            print("{} has been slain!".format(my_team[target]))

def Fight(my_team, enemy_team, numEnemies):
    genEnemyTeam(numEnemies)
    print("You have {} enemies this round. Good luck!".format(numEnemies))
    for i in range(len(enemy_team)):
        print(enemy_team[i])
    while len(enemy_team) > 0 and len(my_team) > 0:
        if len(my_team) > 0:
            print("\nYour turn!")
            for i in range(len(my_team)):
                if len(enemy_team) > 0:
                    c_p = my_team[i]
                    print("\nParty member {}'s turn! Go {}!".format(i+1, c_p.getName()))
                    makeMove(c_p, enemy_team, my_team)
        #Then enemies turn
        if len(enemy_team) > 0:
            print("\nEnemy team's turn to attack!")
            enemyMoves(my_team, enemy_team)
        else:
            break
    if len(enemy_team) == 0:
        print("All enemies have been slain! Prepare for the next round")
    if len(my_team) == 0:
        pass

def buildFighter(i):
    print("\nBuilding fighter {}:".format(i+1))
    print("A fighter starts with 20 health and 3 power. You have 10 points that you can attribute to his power, health, or crit ability.")
    power = int(input("How much more power should he have? "))
    health = int(input("How much more health should he have? "))
    crit = int(input("How much crit should he have? "))
    if power + health + crit <= 10:
        name = input("What should his name be? ")
        my_team.append(Fighter(name, power + 3, health + 20, crit))
        print("Fighter built!")
    else:
        print("You used more than 10 points. Try again")
        buildFighter(i)

def buildHealer(i):
    print("\nBuilding healer {}:".format(i+1))
    print("A healer starts with 30 health and 6 healing power. You have 10 points that you can attribute to his power, health, or healing ability.")
    power = int(input("How much power should he have? "))
    health = int(input("How much more health should he have? "))
    healing = int(input("How much more healing should he have? "))
    if power + health + healing <= 10:
        name = input("What should his name be? ")
        my_team.append(Healer(name, healing+6, health+30, power))
        print("Healer built!")
    else:
        print("You used more than 10 points. Try again")
        buildFighter(i)

def buildTeam():
    numFighters = int(input("How many fighters would you like? You can have 0, 1, 2, or 3: "))
    numHealers = 3-numFighters
    if numFighters == 0 or numFighters == 1 or numFighters == 2 or numFighters == 3:
        print("you will have {} fighters and {} healers.".format(numFighters, numHealers))
        for i in range(numFighters):
            buildFighter(i)
        for i in range(numHealers):
            buildHealer(i)
    else:
        buildTeam()

    

def start(my_team):
    print("You can have three characters total. You can have a mix of fighters and healers.")
    buildTeam()
    print("\nYour team is built:")
    for i in range(len(my_team)):
        print(my_team[i])
    print('\n')
    numEnemies = 1
    while len(my_team) > 0:
        Fight(my_team, enemy_team, numEnemies)
        numEnemies += 1
    print("All team members have been slain. You made it to round {}. Good job!".format(numEnemies))
start(my_team)

#commentaasdf a'hiufdasuidfsa
