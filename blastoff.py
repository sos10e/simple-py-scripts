# A function to count down
def countdown(n):
     if n <= 0:
          print('Blastoff!')
     else:
          print(n)
          countdown(n-1)
# A function to count up
def countup(n):
    if n>=0:
        print("Blastoff!")
    else:
        print(n)
        countup(n+1)

# Input the numbe from user using input
number=input("Enter a  number: ")
# convert the input into an integer
number=int(number)
# Check if wether to call countup or countdown
# First conditional make sure that contdown handles the zero input as well as other positive number
if(number>=0):
    countdown(number)
else:
    countup(number)