# This program demostrates the use of chained contitional in python
# Chained conditional if occurs when you write conditional selection that perform more than 2 selection
# To accomplish this we use if/elif/else
#The shows the program uses chained conditional to determine the  continent of given person




#Function to accept the 
def input_continent():
    name=input("Enter your name: ")
    continent=input("Enter your continent: ")
    continent_checker(continent, name)

# function that demostrates the uses of chained conditionals
def continent_checker(continent, name):
    #It check wether the continent is known or not
    if(continent=="North America"):
        print(f"Oooh, I know Silicon Valley.  {name} , You are from North America" )
    elif(continent=="South America"):
        print(f"Oooh, I  know amazon.  {name}, You are from South America" )
    elif(continent=="Europe"):
        print(f"Oooh, Watch soccer(football).  {name}, You are from Europe" )
    elif(continent=="Europe"):
        print(f"Oooh, I know kangaroo.   {name},You are from Australia" )        
    elif(continent=="Africa"):
        print(f"Oooh, I know lions.  {name}, You are from Africa")
    elif(continent=="Asia"):
        print(f"Oooh, I know lions.  {name}, You are from Africa")
    elif(continent==""):
        print(f"Oooh, its interesting to meet iceman.  {name}, You are from Antarctica")
    else:
        print(f"Oooh I know the Santa. {name}, You are from the moon")
#Prompt user to display the functions
input_continent()