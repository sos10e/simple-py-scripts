# Define a recrusive function that generate a runtime error
def runtime_error(n):
    if(n<1): 
         print('Done.')
    else:
        print("I will be diplayed  until computer rejects me")
        runtime_error(n-1)
# Calling the function that couse runtime
runtime_error(5)