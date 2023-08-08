s = input()
w = '0123456789'
flag = False
for i in range(len(s)):
    if s[i] in w:
        flag = True
        print(s[i])
        print(s[i] in w)

if flag:
    print("Цифра")
else:
    print("Цифр нет")