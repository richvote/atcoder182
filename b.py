N = int(input())
a = list(map(int,input().split()))

max_count = 0
num = 0

for i in range(2,1000):
    count = 0
    for j in range(len(a)):
        if a[j] % i == 0:
            count += 1
    if max_count < count:
        max_count = count
        num = i
print(num)