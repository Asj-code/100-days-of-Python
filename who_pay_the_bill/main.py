import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
name = names.len()
random_name = random.randint(0, name)

print(names[random_name])