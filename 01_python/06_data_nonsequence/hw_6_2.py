# 아래 함수를 수정하시오.
def remove_duplicates_to_set(arr):
    return set(arr)
# 가정 : arr에 1~9 까지의 정수만 요소로 삽입된다면,
def remove_duplicates_to_set(arr):
    # 기본 dict # 첫 초기화는 0번 나왔다고 초기화
    # counut_dict = {1: 0, 2: 0, 3: 0, 4: 0}
    # dict_comprehension
    counut_dict = {i: 0 for i in range(1, 10)}
    # return counut_dict
    # 중복이 없다.
    # 배열의 모둔 요소를 순회한다.
    # 이떄, 순회 대상이, 이전에 한번도 나온적이 없다.
        # 요소를 중심으로 해당요소가 몇번 나왔는지 셀 수 있어야함.
        # 1이 1번 나왔으면 1=1
        # 2가 3번 나왔으면 2=3
        # dict = {1: 1, 2: 3}
    for num in arr:
        counut_dict[num] += 1
    # 모든 출현횟수 기록해둔 dict를 순회해서
        # value가 1인 (1번 이상 나온 값) key 모아서 새 list
    result = [key for key, item in counut_dict.items() if item >= 1]
    return set(result)

# 가정 : arr에 1~9 까지의 정수만 요소로 삽입된다면,
def remove_duplicates_to_set(arr):
    count_list = [0 for i in range(10)]
    for index in arr:
        count_list[index] += 1
    result = [num for num in range(len(count_list)) if count_list[num] >= 1] 
    return result

# 딕셔너리에 집중
def remove_duplicates_to_set(arr):
    # 최종 결과물
    result = set()
    duplicate_check_dict = {}
    for num in arr:
        # 해당하는 키가 dict에 없다면
        # if dict.get(key) == None:
        #     dict[key] = 0
        # else:
        #     dict[key] += 1
        # if dict[key]: (키가 없는경우 KeyError)
        duplicate_check_dict[num] = duplicate_check_dict.get(num, 0) + 1
        # 중복없음 == 1번만 나왔으면 아무튼 나온거임
        if duplicate_check_dict[num] == 1:
            result.add(num)
    return result

result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)
