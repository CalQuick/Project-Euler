'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

end = 20
num = end

answer = ''

while not answer:
  for i in range(end, 0, -1):
    if num % i != 0:
      num += end
      break
    elif i == 1:
      answer = num

print(answer)