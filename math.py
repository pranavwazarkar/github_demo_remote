#addition
def add(x,y):
    return x+y; 
#substraction
def sub(x,y):
    return x-y 
#division###
def divd(x,y):
    if y==0:
        return ERROR
    else:
        return x/y
#multiplication
def mult(x,y):
    if x==0 or y==0:
        return 0
    else:
        return x*y
#mod_Fn
def mod(x,y):
    if y==0:
        return "infinity"
    else:
        
        return x%y
#square Fn
def square(x):
    return x*x
