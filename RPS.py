import random
val = ['R','P','S']#R --> ROCK, P--> Paper, S--> Scisscors
def play(chance):
    comp_count = user_count = 0
    for i in range(1,chance+1):
        computer_choice = random.choice(val)
        user_choice = input("Enter your choice: ")
            
        if computer_choice == 'R':
            x = "Rock"
        elif computer_choice == 'P':
            x = "Paper"
        else:
            x = "Scisscors"
        print("Computer choice: ",x)
        
        if (computer_choice.lower() == user_choice.lower()):
            user_count +=1
    
        else:
            comp_count += 1
    print("Your Score:",user_count)
    print("Computer Score:",comp_count)
    if (user_count > comp_count):
        print("YOU WIN")
    elif (user_count == comp_count):
        print("It's a TIE")
    else:
        print("YOU LOST")
    
    

print("      HELLO     ")
print("ROCK PAPER SCISSCORS")
while True:
    chance = int(input("How many chances do you want now: "))
    print("Denote:\n1.Rock as 'R'\n2.Paper as 'P'\n3.Scisscors as 'S'")
    play(chance)
    
    opt = input("Do you want to play again?\n1.Yes\n2.No\n")
    if opt != '1':
        print("Thank YOU 😊")
        break
    



