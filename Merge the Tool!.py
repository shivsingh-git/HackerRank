def merge_the_tools(s, k):

 n=len(s)
 for x in range(0, n, k):
     slicedStr = s[x : x+k]
     uni =[]
     for y in slicedStr:
         if y not in uni:
             uni.append(y)
     print (''.join(uni))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
