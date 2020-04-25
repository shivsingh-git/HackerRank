if __name__ == '__main__':
    s = raw_input()
    f=0
    f1=0
    f2=0
    f3=0
    f4=0
    for i in range(0,len(s)):
        if(s[i].isalnum()==True):
            f=1
        if(s[i].isalpha()==True):
            f1=1
        if(s[i].isdigit()==True):
            f2=1
        if(s[i].islower()==True):
            f3=1
        if(s[i].isupper()==True):
            f4=1
    if (f==1):
        print("True")
    if (f==0):
        print(False)
    if(f1==1):
        print("True")
    if(f1==0):
        print("False")    
    if(f2==1):
        print("True")
    if(f2==0):
        print("False")    
    if(f3==1):
        print("True")
    if(f3==0):
        print("False")    
    if(f4==1):
        print("True")
    if(f4==0):
        print("False")                            
