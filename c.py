# # 入力受け取り
# N, W = map(int, input().split())
# a = [int(input()) for _ in range(N)]
# # bitは2^N通りの部分集合全体を動きます。
# exist = False
# for bit in range(0, 1 << N):
#     # print(bin(bit))
#     sum = 0 # 部分集合に含まれる要素の和
#     for i in range(N):
#         # i番目の要素a[i]が部分集合に含まれているかどうか
#         if bit & (1 << i):
#             sum += a[i]
#         # sumがWに一致するかどうか
#         if sum == W:
#             exist = True

N = input()
a = list(map(int,N))
k = len(a)
print("N={}, a={}, k={}".format(N,a,k))

m = -1
for bit in range(1<<k): #0桁からk桁まで
    # print(bin(bit))
    s = ''
    # print(len(s))
    # s = "1"
    # print(len(s))
    for i in range(k):
      if bit & (1<<i):
        s += str(a[i])
    if s == '' or int(s) % 3 != 0:
        continue
    elif int(s) % 3 == 0:
        m = max(len(s),m)
if m != -1:
   print(k - m)
else:
   print(-1)
