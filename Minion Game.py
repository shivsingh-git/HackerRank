def minion_game(string):
    vowel='AEIOU'                           #initializng the vowels
    kev=0
    stu=0 
    for i in range (len(string)):           #running loop on whole String
        if s[i] in vowel:                   #if starting of the strng is a vowel
            kev=kev+(len(string)-i)         #total number of strings that can be formed with s[i] as strt vowel
        else:
            stu=stu+(len(string)-i)         #total number of consonants starting string
    
    if(kev>stu):
        print("Kevin",kev)                  #if vowel count is more than the consonant count
    elif(kev<stu):
        print("Stuart",stu)                 #if consonant count is more than vowel count
    else:
        print("Draw")                       #if both the counts are equal.
        
        
if __name__ == '__main__':
    s = input()
    minion_game(s)
