print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first_path = input("You are standing in front of two possible paths, choose one to start, right or left? Type right or left:  ").lower()

if first_path == "right":
  print("You have chosen the path of the eagle. Good choise, now you receive the gold eagle that will help you to find the treasure.")
  second_path = input("Now you are in front of a lake where there is a boat. What do you will do, choose the boat or swimming? Type boat or swim:  ").lower()
  if second_path == "boat":
    third_path = input("Congrats! You reach the island. Now you are in front of a mountain. What do you choose, climb it or circle aroun it? Type clim or circle:  ").lower()
    if third_path == "circle":
      print("You found the treasure! You win!")
    else:
      print("Canibals aet you! Game over!")
  else:
    print("You drowned! Game over")
else:
  print("You fall into a big hole. Game over")
