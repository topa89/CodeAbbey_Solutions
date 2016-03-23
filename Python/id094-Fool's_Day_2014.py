problems=int(input())
answer = []
for problem in range(problems):
    total = 0
    numbers = input().split()
    for num in numbers:
        total += int(num)*int(num)
    answer.append(str(total))
print(' '.join(answer))
