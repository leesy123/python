num = list(map(int, input().split()))

for i in range(int(len(num)/2)):
    tmp = num[i]
    num[i] = num[len(num)-1-i]
    num[len(num)-1-i] = tmp

for i in range(len(num)):
    print(f'{num[i]} ', end='')
print()