# a = int(input())
# if (1000 <= a <10000) and (a % 7 ==0 or a % 17 == 0):
#     print('YES')
# else:
#     print('NO')

# a, b, c  = int(input()), int(input()), int(input())
# if a + b > c and a + c > b and b + c > a:
#     print('YES')
# else:
#     print('NO')


# кратность 4, некратно 100 и кратно 400
# a = int(input())
# if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
#     print('YES')
# else:
#     print('NO')



# шахматы ходы короля
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if (a - 1 <= c <= a + 1) and (b - 1 <= d <= b + 1):
    print('YES')
else:
    print('NO')