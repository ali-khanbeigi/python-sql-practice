import random

def welcome():
    print("welcome to this funny game")
    print("I will guess number between 1 100 and")
    print("you have to guess it...")
    print("are you ready?")
    print("go go go!")
    print()
    
def finish(number ,  count):
    print("good game!")
    print(f"my number was {number} and you found in {count} guesses")    
    print()
    answer =  input("do you want to play again? (Y/N)")
    if answer.upper() in ["y" or "are" or "yes"]:
        return True
    else:
        return False
        
def win(computer_number , guess):
    return computer_number == guess
    
def answer(computer , user):
    if computer>user:
        return "my number is larger"
    elif computer<user:
        return "ohh... you went so larger! mine is smaller"
    
    return "wow! you won! good game"
    
    
    
def get_a_guess():
        ans = input("what is your guess?")
        return int(ans)
welcome()
continue_playing = True
while (continue_playing):
    computer_number = random.randint(1,100)
    guess = 0
    count = 0
    while (not win(computer_number , guess)):
        guess = get_a_guess()
        count += 1
        print(answer(computer_number , guess))
    
    continue_playing = finish(computer_number, count)