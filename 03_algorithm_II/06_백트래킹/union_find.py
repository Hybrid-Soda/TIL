# 유일한 멤버를 포함하는 새로운 집합을 생성하는 연산
def make_set(n):
    parent = [i for i in range(n)]
    rank = [0] * n
    return parent, rank

# x를 포함하는 집합을 찾는 연산
def find_set(x):
    # 특정 노드에서 루트까지의 경로를 찾으며 노드들의 부모를 갱신
    if parent[x] != x:
        parent[x] = find_set(parent, parent[x])
    return parent[x]

# x와 y를 포함하는 두 집합을 통합하는 연산
def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    # 두 값의 루트가 같으면 종료
    if root_x == root_y:
        return

    # 루트의 랭크를 비교하여 어디에 소속될 지 결정
    if rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    elif rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

# 예시 사용법
n = 5
parent, rank = make_set(n)

# Union 연산 수행
union(parent, rank, 0, 1)
union(parent, rank, 2, 3)
union(parent, rank, 0, 4)

# Find 연산 수행
print(find_set(parent, 1))  # 출력: 0
print(find_set(parent, 3))  # 출력: 2
print(find_set(parent, 4))  # 출력: 0
