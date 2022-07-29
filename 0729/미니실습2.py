from tkinter import X


print('리스트를 역순으로 출력합니다.')
len = int(input('원소 수를 입력하세요. '))
x = []

for i in range(0, len) :
    n = int(input(f'x[{i}]값을 입력하세요 : '))
    x.append(n)

print('리스트를 역순으로 출력합니다.')
for i in range(0, len) :
    print(f'x[{i}] = {x[len-i-1]}')