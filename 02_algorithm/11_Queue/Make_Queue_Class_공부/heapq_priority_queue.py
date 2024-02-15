from queue import PriorityQueue
import heapq

q = PriorityQueue()
q.put((45, 'z'))
q.put((17, 'x'))
print(q.queue)

arr = [(45, 'z'), (17, 'x'), (6, 'a'), (100, 'b')]
heapq.heapify(arr)
print(arr)

# 트리에 push하면 맨 끝에 우선 삽입이 된 후 부모 노드와 우선순위를 비교해서 자리를 바꿈
'''
heapQueue 구조 : 2진 트리 구조
        6
    17      45
100
'''
heapq.heappush(arr, (4, 't'))
print(arr)
'''
heapQueue 구조 : 2진 트리 구조
            4
        6       45
    100    17
'''
heapq.heappush(arr, (30, 'f'))
print(arr)
'''
heapQueue 구조 : 2진 트리 구조
                4
        6               30
    100    17       45
'''
heapq.heappop(arr)  # (4, 't')
print(arr)
'''
heapQueue 구조 : 2진 트리 구조
        6
    17      30
100    45
'''