# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
def max_digits(n):
  a = '9'*n
  return int(a)

def min_digits(n):
  a = '1'+ '0'*(n-1)
  return int(a)

def is_sym(inp):
  if str(inp) == str(inp)[::-1]:
    return True
  else:
    return False



digits = 3

starting = min_digits(digits)
ending = max_digits(digits)

print('Min digits = {}'.format(starting))
print('Max digits = {}'.format(ending))
print()

prev_ans = 0
ans_list = []
for i in range(starting, ending + 1):
  for j in range(starting, ending + 1):
    ans = i*j
    if is_sym(ans):
      # print('{} x {} = {}'.format(i, j, ans))
      ans_list.append(ans)

print(str(max(ans_list)) + ' is the highest')