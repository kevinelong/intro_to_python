#TERNARY - THREE WAY OPERATOR like ? :
likes_coffee = True

print("coffee" if likes_coffee else "tea")

drink = "coffee" if likes_coffee else "tea"
print(drink)

#LONG WAY

if likes_coffee:
    drink = "coffee"
else:
    drink = "tea"
print(drink)
