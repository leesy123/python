num = list(map(int, input().split()))
minimum = num[0]
maximum = num[0]
min_index = 0
max_index = 0

for i in range(1,len(num)):
    if minimum > num[i] :
        minimum = num[i]
        min_index = i
    if maximum < num[i] :
        maximum = num[i]
        max_index = i
    
print(f'최대값 : {maximum} / 인덱스 : {max_index}')
print(f'최소값 : {minimum} / 인덱스 : {min_index}')