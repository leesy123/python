str = input('숫자를 입력하세요. ')
l = len(str)
num = int(str)

left = num // (10**(l/2))
right = num % (10**(l/2))

lsum = 0
rsum = 0

for i in range(1,int(l/2) + 1) :
  lsum += left%10
  rsum += right%10
  left = left//10
  right = right//10

if lsum == rsum : print('LUCKY')
else : print('READY')