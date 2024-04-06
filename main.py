from abc import ABC, abstractmethod

class Weapon(ABC):       #создаём абстрактный класс
    @abstractmethod      # декоратор
    def attack(self):
        pass

class Sword(Weapon):    #создаём типы оружия
    def attack(self):
        return "Боец наносит удар мечом."
class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."


class Fighter:      # создаём класс штурмовик
    def __init__(self, weapon):   # начальное оружие
        self.weapon = weapon
    def changeWeapon(self, new_weapon):  #новое оружие
        self.weapon = new_weapon
    def fight(self):
        print(self.weapon.attack())

class Monster():
    def __init__(self):
        self.is_defeated = False    #монстр жив
    def defeat(self):
        self.is_defeated = True      #монстр побеждён
        print("Монстр побежден!")


# Создаем оружие
sword = Sword()
bow = Bow()

# Создаем бойца с мечом
fighter = Fighter(sword)

# Создаем монстра
monster = Monster()

# бой с мечом
fighter.fight()
monster.defeat()

# Меняем оружие на лук
fighter.changeWeapon(bow)

#  бой с луком
fighter.fight()
monster.defeat()


