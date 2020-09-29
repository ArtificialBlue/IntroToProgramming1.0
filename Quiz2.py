def get_animal(sound):
    if sound == "meow":
        return "cat"
    elif sound == "woof":
        return "dog"
    elif sound == "quack":
        return "duck"
    else:
        return "I don't recognize that animal sound"

    
colors = ["red","yellow","green","blue","purple"]
colors.append("violet")
del colors[1]

for i in colors:
    print(i)

get_animal("Yeet")
    
