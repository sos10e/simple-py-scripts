# This program uses the nested if to check in your are lucky
# The lucky winner is person whose name is Job and has age of 10 years or Lucky with age of 20 years

def input_winner():
    name=input("Enter your name: ")
    age=input("Enter your age: ")
    winner_checker(name, age)

#Function to demostrate the use of nested conditional
def winner_checker(name, age):
    if(name=="Job"):
        #Nested condition
        if(age==10):
            print(f"{name} you are lucky")
        else: 
            print(f"{name} you are not lucky")
    elif(name=="Lucky"):
        #Nested condition
        if(age==20):
            print(f"{name} you are lucky")
        else: 
            print(f"{name} you are not lucky")
    else:
        print(f"{name} you are not lucky")

input_winner()