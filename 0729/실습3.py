def findIndex(b, key):
    a=b.copy()
    i=0
    a.append(key)
    
    while True :
        if a[i] == key : 
            if i == len(b) : return -1
            else : return i
        i+=1

def binarySearch(a, key):
    pl = 0
    pr = len(a) - 1
    while True :
        pc = (pr+pl)//2
        if key == a[pc] : return pc
        elif key < a[pc] : pr = pc-1
        else : pl = pc+1
        if pl>=pr : return -1

num = list(map(int, input().split()))
key = int(input())
print(findIndex(num,key))
print(binarySearch(num,key))