s=input("Enter the string: ")
revstr=[]
revstr=s[::-1]
l1=[]
                                    #print(revstr)  Checking if the string is getting correctly reversed            
for x in s:
    l1.append(ord(x))
l2=[]                               #list initialization
for i in range(0,len(l1)-1):
    if(l1[i]>l1[i+1]):
        l2.append(l1[i]-l1[i+1])
    else:
        l2.append(l1[i+1]-l1[i])  
#print(l1)
#print(l2)         

lr1=[]
for x in revstr:
    lr1.append(ord(x))
lr2=[]
for i in range(0,len(lr1)-1):
    if(lr1[i]>lr1[i+1]):
        lr2.append(lr1[i]-lr1[i+1])
    else:
        lr2.append(lr1[i+1]-lr1[i])    
#print(lr1)
#print(lr2)    
if (l2==lr2):
    print("Funny")
else:
    print("Not Funny")    
