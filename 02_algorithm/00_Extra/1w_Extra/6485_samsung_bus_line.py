import sys
sys.stdin = open('input.txt')

# 6485 삼성시의 버스 노선
# N개의 버스 노선 / 5000개의 버스 정류장
# i번째 버스 노선은 번호가 A 이상, B 이하인 모든 정류장만을 다님
# P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 풀이

for tc in range(int(input())):

    # index : 버스 정류장 번호 / value : 정류장을 지나는 버스 수
    bus_stops = [0] * 5001

    # 노선 개수 입력 및 버스 정류장 카운트
    for route in range(int(input())):
        start, end = map(int, input().split())
        for num in range(start, end+1):
            bus_stops[num] += 1

    # 입력한 인덱스를 bus_stops 배열에 넣어 버스 수를 받아 답안 배열에 추가
    answer = []
    for station in range(int(input())):
        answer.append(bus_stops[int(input())])

    print(f'#{tc+1}', *answer)
