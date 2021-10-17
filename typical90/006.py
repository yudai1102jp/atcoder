N, K = map(int, input().split())
S = input()


word = [[] for i in range(32)]

i = 0
for w in S:
    now_w = ord(w)-ord('a')
    word[now_w].append(i)
    i += 1

now = 0
print_n = 0
while K:
    for i, w in enumerate(word):
        if w and now <= w[0] and w[0] <= N-K:
            print(chr(ord('a')+i), end='')
            now = w[0]
            K -= 1
            w.pop()
            break
print()
