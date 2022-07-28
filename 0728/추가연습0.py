def solution(a, b):
  ans = -1
  min = a
  if a == b : ans = a
  elif a > b : min = b
  
  for i in range(1, a+1):
    if (a/i==a//i) and (b/i==b//i) : ans = i
  return ans

c = solution(12,16)
print(c)