from collections import deque

Q = deque()
Q.append(1)
mychew_counts = {1: 1}  # 받은 마이쮸 개수 저장
left_mychew = 20  # 남은 마이쮸 개수

while left_mychew > 0:
    # 마이쮸를 받는다
    person = Q.popleft()
    left_mychew -= mychew_counts[person]
    mychew_counts[person] += 1

    # 그 다음 줄을 선다
    Q.append(person)

    # 새로운 사람이 들어와서 줄을 선다
    new_person = len(mychew_counts) + 1
    Q.append(new_person)
    mychew_counts[new_person] = 1

print(f'Owner of last mychew : {Q[-2]}')