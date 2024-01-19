food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

# 아래에 코드를 작성하시오.
for idx in range(len(food_list)):
    food_name = food_list[idx]["이름"]
    food_type = food_list[idx]["종류"]

    if food_name == '토마토':
        food_list[idx]["종류"] = '과일'
    
    if food_name == '자장면':
        print(f'{food_name}엔 고춧가루지')

    print(f'{food_name} 은/는 {food_type} (이)다.')

print(food_list)