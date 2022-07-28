def solution(left, right):
  ans = 0
  for i in range(left, right + 1):
    cnt = 0

    for j in range(1, int(i/2) + 1) :
      if i // j == i/j :
        if j ** 2 == i : cnt += 1
        else : cnt += 2
    
    if cnt%2 : ans -= i
    else : ans += i

  return ans

left = int(input('left = '))
right = int(input('right = '))

c = solution(left,right)
print(c)