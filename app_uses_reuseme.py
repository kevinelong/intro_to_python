# LEAST SAFE
# from reuseme import *
# print(do_a_thing(11, 44))

# SAFER
# from reuseme import do_a_thing, URLS, Food
# print(do_a_thing(11, 44))

# SAFEST
import reuseme

# from random import randint

print(reuseme.do_a_thing(11, 44))
print(reuseme.do_a_thing(13, 13))
for u in reuseme.URLS:
    print(u)

donut = reuseme.Food("Donut!")
print(donut.name)


def do_a_thing(a, b):
    return a * b

print(do_a_thing(4,7))