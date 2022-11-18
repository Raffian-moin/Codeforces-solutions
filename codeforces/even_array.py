test_cases = int(input())
# element_count = input()

while test_cases:
    element_count = int(input())
    element_list = list(map(int,input().split()))

    even = 0
    odd = 0
    for index, value in enumerate(element_list):
        # print(f"index1- {index}  value-{value}")
        if index % 2 != value % 2:
            if value % 2 == 1:
                odd = odd+1
            else:
                even = even+1

    if even == odd:
        print(even)
    else:
        print(-1)
    test_cases -=1