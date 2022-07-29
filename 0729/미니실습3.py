def linearSearch(a, key):
    count = 0
    i = 0
    
    while True :
        count += 1
        if i == len(a) : return count
        count +=1
        if a[i]== key : return count
        i+=1

def sentinelMethod(b, key):
    a = b.copy()
    a.append(key)
    i = 0
    count = 0
    
    while True :
        count += 1
        if a[i] == key : break
        i += 1
    return count

a = [2,5,1,3,9,6,7]
print(linearSearch(a,7))
print(sentinelMethod(a,7))