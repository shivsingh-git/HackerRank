n=int(input("Enter the total number of socks"))
l=[]
for i in range(n):
    x=input()
    l.append(x)
#print(l)   
c=0
c1=0 
for i in range(n):
    for j in range(n):
        if(l[i]==l[j]):
            c=c+1

    if((c%2) != 0):
        c1=c1+1
print (c1)              

