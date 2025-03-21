print("Welcome To Hunter & Spirit DEMO")

play = int(input("Enter 1 To Play or 2 To Exit\n"))

if play == 1:
  print("\nIn a world where spirits govern the balance of nature, a terrible curse is spreading, corrupting both spirits and humans alike. You play as a Hunter, a warrior trained to track and bind rogue spirits. During a fateful mission, you come across a mysterious Spirit on the brink of death. With its last strength, the Spirit calls out to you, urging you to come closer. In a desperate plea, it offers you a contract—one that will grant you its power, but at a cost: you and the Spirit will become one. Now you must defeat the Curse King\n")
elif play == 2:
  print("goodbye")
  exit()
else:
  print("Wrong input")

import random

print("Level 1 : village curse\nA remote village has been struck by a mysterious curse. Livestock are slaughtered, villagers disappear, and at night, horrific wails echo from the nearby forest. Rumors speak of a twisted spirit lurking near an old shrine. As a Hunter, you are sent to investigate. The village elder warns you—those who ventured into the forest never returned the same. Determined, you step into the dark woods. The air grows cold, and an unsettling silence surrounds you. Then—a piercing screech. From the shadows, a corrupted spirit emerges\n")

# stats
HP = 100
Village_Curse_HP = 200

#Your Turn
while HP > 0 and Village_Curse_HP > 0 :
  print("Choose Your Move Attack/Block/Heal")
  Move = int(input("Attack (1)\nBlock (2)\nHeal (3)\n> "))
  if Move == 1:
   Attack = random.randint(10,20)
   Village_Curse_HP = Village_Curse_HP - Attack
   print(f"\nEnemy HP:{Village_Curse_HP}\n")
  elif Move == 2:
    Block = random.randint(5,15)
    print("You use blocked\n")
  elif Move == 3:
   Heal = random.randint(15,30)
   HP = HP + Heal
   print(f"HP:{HP}\n")

  #Enemy turn
  Village_Curse_Atk = random.randint(5,25)
  if Move == 2:
    Damage_Taken = max(0, Village_Curse_Atk - Block)
  else:
    Damage_Taken = Village_Curse_Atk
    print("Enemy attack")

  HP = HP - Damage_Taken
  print(f"Your HP:{HP}\n")

  if Village_Curse_HP <= 0:
    print("You have defeated the Village Curse")
    break
  elif HP <= 0:
    print("You have lose")
    break

print("Thank you for playing :>")

