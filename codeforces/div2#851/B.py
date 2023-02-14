for _ in range(int(input())):
    n = int(input())

    def count_odd_digits(n):
        ans = 0
        for i in str(n):    
            if int(i) %2 == 1:
                ans += 1
        return ans

    odds = count_odd_digits(n)

    if odds == len(str(n)) and len(str(n)) > 1:
        print(*[(n//2)+5, (n//2)-4])
    else:
        print(*[n//2, n-(n//2)])