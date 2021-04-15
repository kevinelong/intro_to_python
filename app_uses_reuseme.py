# LEAST SAFE
from reuseme import *

# SAFER
# from reuseme import do_a_thing, URLS, Food

# SAFEST
# import reuseme

print(do_a_thing(11, 44))
print(do_a_thing(13, 13))

print(randint(100,1000))
print(reuseme.do_a_thing(11, 44))

for u in reuseme.URLS:
for u in URLS:
    print(u)

donut = Food("Donut!")
print(donut.name)


# def do_a_thing(a, b):
#     return a * b
#
#
# print(do_a_thing(4,7))