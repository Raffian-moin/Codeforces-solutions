# test_cases = int(input())
# count = 0
# while count < test_cases:
#     inputs = list(map(int, input().split()))

#     number_count = inputs[0]
#     sum_of_lost_numbers = inputs[1]

#     numbers = list(map(int, input().split()))

#     numbers.sort()

#     lost_numbers = []

#     for i in range(numbers[len(numbers)-1]):

#         if i+1 not in numbers:
#             lost_numbers.append(i+1)


#     for number in lost_numbers:
#         sum_of_lost_numbers = sum_of_lost_numbers - number


#     new_number = numbers[len(numbers) - 1]+ 1


#     while(sum_of_lost_numbers > 0):
#         sum_of_lost_numbers = sum_of_lost_numbers - new_number
#         new_number += 1

#     if sum_of_lost_numbers == 0:
#         print('YES')
#     else:
#         print('NO')
#     count += 1

# 2nd submission

for _ in range(int(input())):
    n,s=list(map(int, input().split()))
    a=list(map(int, input().split()))
    a.sort()
    total=a[-1]*(a[-1]+1)//2
    m=total-sum(a)

    x=a[-1]+1
    while m<s:
        m+=x
        x+=1

    if (s==m):
        print('YES')
    else:
        print('NO')


        