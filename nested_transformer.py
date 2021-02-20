# The main strategy is to avoid the use of nested if to know the connection between the conditional for example  determinewhether they are true if both conditional are true or not, this help to find logical operator to use


#Netsed conditinal to show if a developer is senior or not
role="devloper"
exprience=6
if role=='developer':
    if(exprience >=5):
        print('Senior developer')
'''to make simple we can use chained conditional'''
A person  is   senior developer only if role is developer and his exprience  is greater than five so we use androle="devloper"
role="devloper"
exprience=6
if role=="developer" and exprience>=5:
    print('Senior developer')