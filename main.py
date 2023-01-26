from typing import Union #not used right now, might come back later
import random as r
#Used to make 
class GeneralItemError(Exception):
    def __init__(self):
        pass


class item:
    def __init__(self):
        raise GeneralItemError
    class healthpotion:
        def __init__(self,restoredhp: int):
            super.count = 1
    class speedpotion:
        def __init__(self, speedboost: int):
            super.count = 1
    class arrow:
        pass #ammo, does not take inventory space

class weapon:
    def __init__(self):
        raise GeneralItemError
    class melee:
        def __init__(self,*,name: str,dmg: int,durab: int) -> None:
            self.name = name
            self.dmg = dmg
            self.durab = durab
    class ranged:
        def __init__(self,*,name: str,dmg: int,durab:int,ammo:item):
            pass
class npc:
    def __init__(self, name, occupation: str=None) -> None:
        pass
class monster:
    def __init__(self, name, hp, gold, atk, df, spd, type):
        self.name = name
        self.hp = hp
        self.reward = gold
        self.atk = atk
        self.df = df
        self.spd = spd
        self.type = type
    def take_damage(self,damage: int, def_mod: int=0) -> bool:
      pass
class player:
    def __init__(self,name: str,*,hp: int,atk: int,df: int,spd: int, wp: weapon= None) -> None:
        self.name = name
        self.hp = hp
        self.atk = atk
        self.df = df
        self.spd = spd
        self.cash = 0
        self.inv = []
        if wp == None:
            wp = weapon.melee(name="Your fists", dmg=1, durab=-1)
        self.equipped = {"armour": None, "weapon": wp}
        if hp <= 0:
            raise ValueError
    def take_damage(self,damage: int,def_mod: int = 0) -> bool:
        if def_mod == 0:
            if self.df >= damage:
                return False
            else:
                reduced = damage*0.1*def_mod
                dmg = r.randint(-6,5) - reduced
                self.hp -= dmg
    def add_item(self, item: item, count: int)-> bool:
        if len(self.inv) >= self.maxinv:
            pass
        else:
            return False
    def attack(self,monster: monster):
        if monster.spd <= self.spd:
          monster.take_damage()
        else:
          self.take_damage(monster.atk)
class shop:
    """
    Item format: [{'item': item object, 'price': int, 'stock': int}, {'item': item2 object, 'price': int, 'stock': int}, etc]
    """
    def __init__(self,shopkeeper: npc,items: list):
        for item in items: #Check that the items are formatted properly
            if not isinstance(item, dict):
                raise TypeError
            if len(item) != 3:
                raise ValueError
            try:
                if (not isinstance(item['item'], (weapon)) or (not isinstance(item['price'], int)) or (not isinstance(item['stock'], int))):
                    raise ValueError
            except:
                raise ValueError
        self.stock = items

#If this file was run:
if __name__ == "__main__":
    p1 = player("Jake",hp=100,atk=20,df=20,spd=5,wp=weapon.ranged(name="Bow",dmg=20,durab=-1,ammo=item.arrow()))