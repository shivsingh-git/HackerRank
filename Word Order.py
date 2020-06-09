from collections import OrderedDict.                #importing ordered dictionary
words = OrderedDict()

for _ in range(int(input())):           
    word = input()                                  #getting all the inputs required
    words.setdefault(word, 0)                       #making the value for the word as 0
    words[word] += 1                                #increasing the word count.
   
print(len(words))                                   #printing the lenght of the dictionary   
print(*words.values())                              #printing every single words by value
