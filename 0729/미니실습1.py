def min_of(a) :
    minimum = a[0]
    for i in range(1,len(a)):
        if minimum > a[i] : minimum = a[i]
    return minimum

t = (4,7,5.6,2,3.14,1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(min_of(t))
print(min_of(s))
print(min_of(a))