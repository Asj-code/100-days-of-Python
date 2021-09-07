welcome = print("Welcome to the bill calculator")

bill = float(input("Type how much is the bill today? "))

tip = int(input("How much of tip do you want to leave? 10, 12, 15: "))

persons = int(input("how many people are? "))

tip_leave = int(bill * tip / 100)

tip_leave_by_person = (tip_leave / persons)

print(tip_leave_by_person)