from random import randint
from time import sleep
i = 1
class Hero():
   #конструктор класса
   def __init__(self, name, health, armor, power, weapon):
       self.name = name
       self.health = health #число
       self.armor = armor #строка
       self.power = power #число
       self.weapon = weapon #строка
   #печать инфо о персонаже:
   def print_info(self):
       print('->' + self.name)
       print('Уровень здоровья:', self.health)
       print('Класс брони:', self.armor)
       print('Сила удара:', self.power)
       print('Оружие:', self.weapon, '\n')
   #нанести удар по другому персонажу
   def strike(self, enemy):
       attack1 = randint(self.power+0, self.power+20)*i/2
       print('-> УДАР! ' + self.name + ' атакует ' + enemy.name + ' с силой ' + str(attack1) + ', используя ' + self.weapon + '\n')
 
       enemy.armor -= attack1
       if enemy.armor < 0:
           enemy.health += enemy.armor
           enemy.armor = 0
      
       print(enemy.name + ' покачнулся.\nКласс его брони упал до ' + str(enemy.armor) + ', а уровень здоровья до ' + str(enemy.health) + '\n')
  
   #вступить в поединокpip install pyinstaller pyinstaller --onefile -w hello_world.py
   def fight(self, enemy):
       while self.health and enemy.health > 0:
           enemy.strike(self)
           if self.health < 0:
               print(self.name, 'пал в этом нелегком бою!\n')
               break
           self.strike(enemy)
           if enemy.health < 0:
               print(enemy.name, 'пал в этом нелегком бою!\n')
               self.power += 10
               break
           sleep(1)


knight = Hero('Ричард', 50, 25, 20, 'меч')
dragon = Hero('Дракон', 100, 25, 10, 'пламя')

#print('Средиземье в опасности! На помощь спешит доблестный рыцарь...')
knight.print_info()
 
sleep(1)
print(knight.name + ' идёт по лесу. Вдруг видит на пути мелкого воришку...')
 
sleep(1)
rascal = Hero('Питер', 20, 5, 5, 'нож')
rascal.print_info()
 
sleep(1)
if True:#input('Сразиться? (да/нет) >>') == 'да':
   print('\nДА НАЧНЁТСЯ БИТВА!\n')
   sleep(1)
   knight.fight(rascal)
   sleep(1)
 
if knight.health > 0:
       knight.health = 50
       knight.power *= 2
       knight.armor *= 2
       print('\n' + knight.name + ' восстановил силы и стал опытнее. Теперь сила его удара: ' + str(knight.power) + ', а класс брони:' + str(knight.armor) + '\n')
 
sleep(1)
print('\nНаконец-то ' + knight.name + ' добирается до подземелья!')
dragon.print_info()
 
print('\nДА НАЧНЁТСЯ БИТВА!\n')
sleep(1)
knight.fight(dragon)
knight.print_info()
