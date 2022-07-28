def solution(a, b):
  ans = -1

  for i in range(1, a*b+1):
    if (i//a==i/a) and (i//b==i/b) : return i

  return ans

c = solution(2,4)
print(c)