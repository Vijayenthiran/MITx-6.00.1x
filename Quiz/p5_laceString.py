#Suppose you are given two strings (they may be empty), s1 and s2. You would like to "lace" these strings together, by successively alternating elements of each string (starting with the first character of s1). If one string is longer than the other, then the remaining elements of the longer string should simply be added at the end of the new string. For example, if we lace 'abcd' and 'efghi', we would get the new string: 'aebfcgdhi'.

#Write an iterative procedure, called laceStrings(s1, s2) that does this.

def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    i = 0
    s3 = ""
    if len(s1) <= len (s2):
        for letter in s1:
            s3 = s3 + letter + s2[i]
            i += 1
        while i < len(s2):
            s3 = s3 + s2[i]
            i += 1
    else:
         for letter in s2:
            s3 = s3 +  s1[i] + letter 
            i += 1 
         while i < len(s1):
            s3 = s3 + s1[i]
            i += 1  
    return s3
