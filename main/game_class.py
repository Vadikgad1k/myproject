class Warrior:
    def __init__(self,health=100,stamina=100):
        self.__health = health
        self.__stamina = stamina
    @property
    def health(self):
        return self.__health
    @health.setter
    def health(self,new_health):
        if new_health>100:
            self.__health=100
        elif new_health<0:
            self.__health=0
        else:
            self.__health=new_health
    @property
    def stamina(self):
        return self.__stamina
    @stamina.setter
    def stamina(self,new_stamina):
        if new_stamina>100:
            self.__stamina=100
        elif new_stamina>0:
            self.__stamina=0
        else:
            self.__stamina=new_stamina
    def introduces(self):
        print('---------------')
        print(f'Class:{self.__class__.__name__}',
              f'\nHealth:{self.__health}',
              f'\nStamina:{self.__stamina}')
        print('---------------')
    def heals(self,target):
        if self.__stamina>=20:
            print('---------------')
            print(f'{self.__class__.__name__} накладывает повязку из целебных трав',
              f' {target.__class__.__name__}')
            target.health+=10
            self.__stamina-=20
            print(f'здоровье у {target.__class__.__name__} повышено до {target.health}',
            f'\nУ {self.__class__.__name__} осталось {self.__stamina} единиц запаса сил')
            print('---------------')
        else:
            print('Недостаточно сил для использывание этой способности.')
    def attacks(self,target):
        if target.health>3:
            print('---------------')
            print(f'{self.__class__.__name__} наносит урон мечом {target.__class__.__name__}')
            target.health-=3
            self.__stamina-=5
            print(f'Здоровье у {target.__class__.__name__} понижено до {target.health} осталось сил {self.__stamina}')
            print("---------------")
        else:
            target.health-=3
            self.__stamina -= 5
            print('---------------')
            print(f'{self.__class__.__name__} наносит последний удар и побеждает {target.__class__.__name__}')
            print(f'{target.__class__.__name__} покидает отряд')
            print('---------------')
class Mage:
    def __init__(self,health=60,mana=100):
        self.__health = health
        self.__mana = mana
    @property
    def health(self):
        return self.__health
    @health.setter
    def health(self, new_health):
        if new_health > 100:
            self.__health = 100
        elif new_health < 0:
            self.__health = 0
        else:
            self.__health = new_health = new_health
    def introduces1(self):
        print('---------------')
        print(f'Class:{self.__class__.__name__}',
              f'\nHealth:{self.__health}',
              f'\nMana:{self.__mana}')
        print('---------------')
    def heals(self,target):
        if self.__mana>=20:
            print('---------------')
            print(f'{self.__class__.__name__} применяет заклияние на лечения',
                  f'к {target.__class__.__name__}')
            target.health+=10
            self.__mana-=20
            print(f'здоровье у {target.__class__.__name__} повышено до {target.health}',
                  f'\nУ {self.__class__.__name__} осталось {self.__mana} единиц магии')
            print('---------------')
        else:
            print('Недостаточно маны для использывание этой способности.')
    def attacks(self,target):
        if self.__mana>=5 and target.health>3:
            print('---------------')
            print(f'{self.__class__.__name__} наносит урон магией {target.__class__.__name__}')
            target.health-=3
            self.__mana-=5
            print(f'Здоровье у {target.__class__.__name__} понижено до {target.health} осталось единиц магией {self.__mana}')
            print("---------------")
        else:
            print('---------------')
            print(f'{self.__class__.__name__} наносит последний удар и побеждает {target.__class__.__name__}')
            print(f'{target.__class__.__name__} покидает отряд')
            print('---------------')
unit1=Warrior()

unit1.introduces()
unit2=Warrior()
unit3=Mage()
unit3.introduces1()
unit4=Mage(health=50,mana=110)

print(unit1.health)
print(unit1.__dict__)
unit1.heals(unit3)
unit3.heals(unit1)
unit1.attacks(unit3)
unit3.attacks(unit1)
print(unit1.__dict__)
print(unit2.__dict__)
print(unit3.__dict__)
print(unit4.__dict__)