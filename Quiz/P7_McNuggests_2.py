#Solution to McNuggests problem with nested for loop.. Idea ny Nikita Nelson
 def McNuggets (n):
    #6a+9b+20c = 0
    for a in range(n/6):
        for b in range(n/9):
            for c in range(n/20):
                #print "(6*a) + (9*b) + (20*c) :" + str((6*a) + (9*b) + (20*c))
                if ((6*a) + (9*b) + (20*c) ) > n:
                    break
                if (6*a) + (9*b) + (20*c) == n:
                    return True
    return False
print "n: " + str(McNuggets(1))
 
