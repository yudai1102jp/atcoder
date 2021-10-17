N = int(input())
ok = 1
no = 10**8
while no-ok > 1:
    now = (ok+no)//2
    if pow(now, 3) <= N:
        ok = now
    else:
        no = now

if pow(ok, 3) == N:
    print('Yes')
else:
    print('No')
