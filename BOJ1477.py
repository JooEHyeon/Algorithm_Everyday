# n, m, l = map(int, input().split())
# # road = list(map(int, input().split()))
# #
# # road.sort()
# # road.append(l)
# #
# # for tmp_i in range(m):
# #     max_dist = road[1] - road[0]
# #     pos = 0
# #     pos_idx = 0
# #     for tmp_j in range(n):
# #         diff = road[tmp_j+1] - road[tmp_j]
# #         if diff > max_dist :
# #             max_dist = diff
# #             pos = road[tmp_j] + diff/2
# #             pos_idx = tmp_j+1
# #     n += 1
# #     road.insert(pos_idx, pos)
# #
# # ans = 0
# # for i in range(len(road)-1):
# #     ans = max(ans, road[i+1] - road[i])
# #
# # print(ans)
#
# 위처럼 풀면 안된다.
# 반례 : N = 0, M = 2, L = 100 인 경우 위의 알고리즘으로는 50, 25에 설치되어 50인데
# 33 66 에 설치하면 되는 일이다.
#
# 그렇기에 하나씩 설치하지 않고 거시적으로 설치하게 하는 방법이 필요하다
# parametric search 를 사용하자
# 최적화 문제 -> 이 정도를 최대 거리로 하면 설치 가능한가에 대한 결정문제로 바뀐다!


def start(dist, diff, m):
    cnt = 0
    for i in diff:
        if i / dist > 0:
            if i % dist == 0:
                cnt += (i//dist - 1)
            else:
                cnt += (i//dist)
    if cnt <= m:
        return True
    return False


n, m, l = map(int, input().split())
road = list(map(int, input().split()))
road.append(0)
road.append(l)

road.sort()

diff = []
for i in range(len(road)-1):
    diff.append(road[i+1] - road[i])

low = 0
high = l
mid = 0
result = 0

while low <= high:
    mid = (low + high) // 2
    if start(mid, diff, m):
        high = mid - 1
        result = mid
    else:
        low = mid + 1

print(result)









