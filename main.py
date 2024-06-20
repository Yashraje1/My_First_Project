rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

while True:
    print("⬇️⬇️" * 50)
    user_choice = int(
        input(
            "\nWhat is your choice?\n Type:- \n0 for Rock\n1 for Paper\n2 for scissors\n"
        ))
    if user_choice == 0:
        print(rock)
    elif user_choice == 1:
        print(paper)
    elif user_choice == 2:
        print(scissors)
    else:
        print("!!!!!!!!!Please Enter a Valid Choice!!!!!!!!!")
        break
    import random
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print(f"Computer's choice:-\n{rock}")
    elif computer_choice == 1:
        print(f"Computer's choice:-\n{paper}")
    else:
        print(f"Computer's choice:-\n{scissors}")
    #comparative if else
    if user_choice == computer_choice:
        print("It's a Draw! try again")
    elif user_choice == 0:
        if computer_choice == 1:
            print("Computer Wins! try again")
        else:
            print("You win!")
    elif user_choice == 1:
        if computer_choice == 0:
            print("You win!")
        else:
            print("Computer Wins! try again")
    elif user_choice == 2:
        if computer_choice == 0:
            print("Computer Wins! try again")
        else:
            print("You win!")
