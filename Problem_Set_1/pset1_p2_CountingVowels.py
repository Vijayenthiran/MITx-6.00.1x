#Counting Vowels

s = 'azcbobobegghakl';
#print (len(s));
i=0;
ans=0;
while i!=len(s):
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
       ans+=1;
    i+=1;
print (str(ans));