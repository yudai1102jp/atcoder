a = input()
flag = False
ans = 0
for i in a:
    if i == '.':
        flag = True
        continue
    if flag:
        if int(i) >= 5:
            ans += 1
        else:
            pass
        break
    ans = ans*10+int(i)
print(str(ans))
