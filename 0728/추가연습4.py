data = int(input('숫자로 이루어진 문자열을 입력하세요. '))
ans = 1

while data != 0 :
  if data%10 == 1 or data%10==0 :
    ans += data%10
  else : ans *= (data % 10)
  data = data//10

print(ans)