# print("Hello world")

# guests_names = [
# 'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
# 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
# ]
# for guest in enumerate(guests_names):
#     print(guest[1])

# eval() with user input

from math import *
import time
for l in range(1, 3):

    a = 5
    func = input("Enter Math Function to Evaluate:\n")
    try:
        print(eval(func))
    except Exception as ex:
        print(ex)
        break
print('Done')
