data = int(input('숫자로 이루어진 문자열을 입력하세요. '))
ans = 1

while data != 0 :
  if data%10 == 1 : ans += data%10
  elif data%10 != 0 : ans *= (data % 10)
  data = data//10

print(ans)