import random


health = 50

difficulty = 3

potion_health = int (random.randint(15,25) / difficulty)

health = health + potion_health

print(health)


