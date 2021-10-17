
N, K = map(int, input().split())
a = list(map(int, input().split()))

count = dict()
now_kind = 0
ans = 0
now = 0

for i in range(N):
    if not a[i] in count or count[a[i]] == 0:
        count[a[i]] = 1
        now_kind += 1

    else:
        count[a[i]] += 1

    while now_kind > K:
        count[a[i-now]] -= 1
        if count[a[i-now]] == 0:
            now_kind -= 1
        now -= 1

    now += 1
    ans = max(ans, now)
print(ans)
