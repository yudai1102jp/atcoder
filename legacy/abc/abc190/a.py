

a, b, c = map(int, input().split())
if a == b:
    if c:
        print('Takahashi')
    else:
        print("Aoki")
elif a > b:
    print('Takahashi')
else:
    print("Aoki")
