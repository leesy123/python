def findIndex(b, key):
    a=b.copy()
    i=0
    a.append(key)
    
    while True :
        if a[i] == key : 
            if i == len(b) : return -1
            else : return i
        i+=1

num = list(map(int, input().split()))
key = int(input())
print(findIndex(num,key))