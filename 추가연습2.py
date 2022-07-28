N = int(input())
count = 0

num = N
new = 0

while N != new :
  new = num//10 + num%10
  new = new%10 + (num %10) * 10
  num = new
  count += 1

print(count)
