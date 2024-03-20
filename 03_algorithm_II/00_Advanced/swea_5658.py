# 5658 보물상자 비밀번호

for tc in range(int(input())):
    N, K = map(int, input().split())
    lock, nums = input(), set()
    for _ in range(N//4):
        for i in range(0, N, N//4):
            nums.add(int('0x' + ''.join(lock[i:i+N//4]), 16))
        lock = lock[-1] + lock[:-1]
    print(f'#{tc+1} {sorted(nums, reverse=True)[K-1]}')