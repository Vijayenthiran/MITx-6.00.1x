#The function recurPower(base, exp) from Problem 2 computed baseexp by decomposing the problem into one recursive case and one base case:

#baseexpbaseexp==base⋅baseexp−11ifexp>0ifexp=0

#Write a procedure recurPowerNew which recursively computes exponentials using this idea.

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    elif exp%2 ==0: 
        return recurPowerNew(base*base,exp/2)
    else:
        return base*recurPowerNew(base,exp-1)


#Write a function recurPower(base, exp) which computes baseexp by recursively calling itself to solve a smaller version of the same problem, and then multiplying the result by base to solve the initial problem.

#This function should take in two values - base can be a float or an integer; exp will be an integer ≥0. It should return one numerical value. Your code must be recursive - use of the ** operator or looping constructs is not allowed.

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    else:
        return base * recurPower(base,exp-1)
