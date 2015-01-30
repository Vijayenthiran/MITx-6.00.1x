#Alphabetical Substrings 
s = 'abcdefghijklmnopqrstuvwxyz';
i=0;
start_index=0;end_index=0;length=0;length_prev=0;length_flag=0;flag=0;
while i!=len(s):
    if i>0 and i<len(s):
        if ord(s[i-1])<=ord(s[i]) and flag==0:
            start_index=i-1;
            end_index=i+1;
            flag=1;
            length+=1;
                                
        elif ord(s[i-1])<=ord(s[i]) and flag!=0:
            end_index=i+1;
            length+=1;
            
        elif ord(s[i-1])>ord(s[i]) and ord(s[i-2])<=ord(s[i-1]) and length_flag==0:
            flag=0;
            length_prev=length;
            length=0;
            start_index_prev=start_index;
            end_index_prev=end_index;
            length_flag=1;
            #print s[start_index_prev:end_index_prev];  #unwanted
            #print str("1st loop"); #unwanted
            #print str(length); #unwanted
        elif ord(s[i-1])>ord(s[i]) and ord(s[i-2])<=ord(s[i-1]) and length_flag==1:
            flag=0;
            #print ("2nd god loop");
            #print s[start_index:end_index]; #unwanted
            #print str(length_prev); #unwanted
            #print str(length); #unwanted
            if length_prev<length:
                length_prev=length;
                length=0;
                start_index_prev=start_index;
                end_index_prev=end_index;
                #print s[start_index_prev:end_index_prev]; #unwanted
                #print ("2nd loop"); #unwanted
            length=0; 
            
    i+=1;

    
if length>length_prev:
    #if end_index==len(s)-1: 
    #    print s[start_index:]
    if start_index==0 and end_index==0 and (length==0 or length_prev==0):
        print s[0];            
    else:
        print s[start_index:end_index]
else:
    #if end_index_prev==len(s)-1 :
    #    print s[start_index_prev:]
    if start_index_prev==0 and end_index_prev==0 and (length==0 or length_prev==0):
        print s[0]; 
    else:
        print s[start_index_prev:end_index_prev]
    