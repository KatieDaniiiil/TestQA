n = int(input())
counter = 0
for i in range(n, n+1):
    if n**2 % 10 == 2 or n**2 % 10 == 5 or n**2 % 10 == 8:
        counter = counter + 1
print(counter)
