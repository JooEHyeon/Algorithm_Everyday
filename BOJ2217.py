# 실행을 위해서는 shift+alt+f10을 누르면 된다.

n = int(input())
ropes = []

for i in range(n):
    ropes.append(int(input()))

ropes.sort()

num = 0
weight = 0

for i in reversed(ropes):
    if weight < (num+1)*i:
        weight = (num+1)*i
    num += 1

print(weight)
