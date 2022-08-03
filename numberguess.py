import random
print("************************ Welcome to the Number Guessing Game.... ****************************\n")
print("**************************** Game Rules: *******************************\n")
chance = random.randint(5,8)
print(f"1.You have to guess the number in {chance} chances.\n2.If your guess is wrong, your score will reduce.\n3.In this game, you have clues also.")
print("Let's Play the game\n")
print(f"Your current score is {chance}")
print("Enter the lower range of number: ")
lower_range = int(input())
print("Enter the higher range of number: ")
higher_range = int(input())
print("You have to guess the number between {} and {}".format(lower_range,higher_range))
num = random.randint(lower_range,higher_range)
attempt=0
while(True):
    attempt += 1
    guess = int(input("Guess the number: "))
    if guess > num:
        if((chance - attempt) == 0):
            break
        print("Take a small number")
        if ((num % 2) == 0):
            print("It is an even no.")
        elif(chance == 0):
            print("You Lost the Game....")
            break 
        else:
            print("It is an odd no.")
            
    elif guess < num:
        if((chance - attempt) == 0):
                break
        print("Take a large number")
        if ((num % 2) == 0):
               print("It is an even no.")
        elif ((num%3)==0):
                print("It is divisible by 3")
        elif(chance == 0):
                print("You Lost the Game....")
                break
        else:
               print("It is an odd no.")
               
    else:             
            break              
    
if(chance > attempt):
    print(f"Great! You got the number in just {attempt} guesses..")
    print("************ Hurrah!You have win the Game **************")
    print(f"Your new score is: {chance-attempt}")
else:
    print("As your chance limit is up, So,You lost the Game......")     
   
print("**************** Thanks for Playing the Game *******************")
