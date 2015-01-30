#Counting bobs 
 
s = 'azcbobobegghakl';
 
i=0;
ans=0;
while i!=len(s):
    if i<len(s)-2:
        if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
            ans+=1;
    i+=1;
print str(ans);
    
 