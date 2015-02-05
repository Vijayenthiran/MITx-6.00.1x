#For this problem, write a recursive function, lenRecur, which computes the length of an input argument (a string), by counting up the number of characters in the string.

#hint: http://www.greenteapress.com/thinkpython/html/thinkpython009.html#toc89

increment = 0
def lenRecur(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    global increment
    ans = 0
    if aStr == '':
        ans = increment
        increment = 0
        return ans
    else:
        increment += 1
        return lenRecur (aStr[1:])
print lenRecur ("abcdefq")
