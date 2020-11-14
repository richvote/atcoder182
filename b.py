N = int(input())
A = list(map(int,input().split()))
gcd = 0
ans = 0
for k in range(2,1000+1):
    # 数列Aについて、kのgcd度を計算
    count = 0
    for a in A:
        if a % k == 0:
            count += 1
    # gcdが最大なら更新
    if gcd <= count:
        gcd = count
        ans = k
print(ans)