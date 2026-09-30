import random

def display_welcome():
    print("Welcome to my game!")
    print("_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________")   
    
    print(
        """ || I'm  thinking of a number between 1 and 100......  ||
                | Can you guess it ? |"""
    )
    
def get_user_guess():
    while True :
        guess = int(input("Enter your guess : "))
        try:
            if guess >=1 and guess<=100:
                return guess
            else : 
                print("Enter again....  ")
            
            # return guess
        except ValueError:
            print(" please enter a valid number. ")

def evaluate_guess(target, guess) :
    if guess < target :
        return  "Too low"
    elif guess > target :
        return  "Too high"
    else:
        return "Congratulations! You guessed the correct number. "
        
def play_game():
    target_number = random.randint(1,100)
    attempts=0
    max_attempts =10
    display_welcome()
    while attempts < max_attempts:
        user_guess = get_user_guess()
        result = evaluate_guess(target_number , user_guess)
        print(result)

        if user_guess == target_number:
            print(f" It took you {attempts+1} attempts to guess the number {target_number}")
            break
        attempts+=1

        if attempts == max_attempts :
             print(f"""sorry! you ran out of attempts.
                  The number was {target_number}""")

if __name__ == "__main__" : 
    play_game()

print("         | || ||    GAME OVER.....     | || ||   Hope you enjoyed it. ")