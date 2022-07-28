def solution(n):
  sqr = 1
  ans = -1
  while 1 :
    if sqr ** 2 == n :
      ans = (sqr+1) ** 2
      break
    elif sqr ** 2 > n : break
    sqr += 1
  return ans

num = int(input('정수 n을 입력하세요 : '))
print(solution(num))