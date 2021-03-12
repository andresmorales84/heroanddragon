import random

try:
    hero_hp = int(input("how many hp does the hero have?"))
    dragon_hp = int(input("how many hp does the dragon have?"))
    hero_max_dmg = int(input("What is the maximum hero's damage?"))
    dragon_max_dmg = int(input("What is the maximum dragon's damage?"))

except ValueError:
    print("Please provide numbers only")

while True:
    print("The dragon with", dragon_hp, "hp attacks out hero with", hero_hp, "hp")
    dragon_attack = random.randint(1, dragon_max_dmg)
    hero_hp=hero_hp-dragon_attack
    print("The dragon does", dragon_attack, "damage and the hero has", hero_hp, "hp left")

    if hero_hp==0:
        print("Unfortunately the dragon killed our hero. RIP sir Bravealot")
        break

    hero_attack = random.randint(1, hero_max_dmg)
    dragon_hp=dragon_hp-hero_attack
    print("The hero does", hero_attack, "damage and the dragon has", dragon_hp, "hp left")

    if dragon_hp==0:
        print("Our valiant hero has slain the dragon!")
        break
    input("Round over. Press any key")





