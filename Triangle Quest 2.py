#getting the inputs in the for loop as the range end.
#1^2=1,11^2=121,11^3=12321.....basic ideation
for i in range(1,int(input())+1):                     #running the forloop from 1 to input(n)
  print(pow(((pow(10,i)-1)//9),2))                    #frstly getting the values as 1,11,111, for respective 1,2,3..
                                                      #then squaring them to get the required output.
