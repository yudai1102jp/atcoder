# a = list(input())
T = int(input())

for t in range(T):
    R, G, B = map(int, input().split())
    if R == G or R == B:
        print(R)
    elif B == G:
        print(B)
    else:
        ans = int(1e8+5)
        A1, A2, A3 = sorted((R, G, B))
        if (A2-A1) % 3 == 0:
            ans = A2
        if ((A3-A1) % 3 == 0 or (A3-A2) % 3 == 0) and A2 > 0:
            ans = min(ans, A3)

        if ans == int(1e8+5):
            ans = -1
        print(ans)

# for t in range(T):
#     R1, G1, B1 = map(int, input().split())

#     R, G, B = R1, G1, B1
#     if (2*B+G) % 3 == 0 and (B-G) % 3 == 0:
#         n = (G+2*B)//3
#         m = (B-G)//3
#         if n >= 0 and m >= 0:
#             print(n+m)
#             continue
#     G, B = B1, G1
#     if (2*B+G) % 3 == 0 and (B-G) % 3 == 0:
#         n = (G+2*B)//3
#         m = (B-G)//3
#         if n >= 0 and m >= 0:
#             print(n+m)
#             continue
#     R, G, B = G1, B1, R1
#     if (2*B+G) % 3 == 0 and (B-G) % 3 == 0:
#         n = (G+2*B)//3
#         m = (B-G)//3
#         if n >= 0 and m >= 0:
#             print(n+m)
#             continue
#     G, B = B, G
#     if (2*B+G) % 3 == 0 and (B-G) % 3 == 0:
#         n = (G+2*B)//3
#         m = (B-G)//3
#         if n >= 0 and m >= 0:
#             print(n+m)
#             continue
#     R, G, B = B1, R1, G1
#     if (2*B+G) % 3 == 0 and (B-G) % 3 == 0:
#         n = (G+2*B)//3
#         m = (B-G)//3
#         if n >= 0 and m >= 0:
#             print(n+m)
#             continue
#     G, B = B, G
#     if (2*B+G) % 3 == 0 and (B-G) % 3 == 0:
#         n = (G+2*B)//3
#         m = (B-G)//3
#         if n >= 0 and m >= 0:
#             print(n+m)
#             continue
#     print(-1)
