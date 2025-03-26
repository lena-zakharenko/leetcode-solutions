nums = [2,7,11,15]
# nums = [3,2,4]
# nums = [3,3]
# nums = [0,4,3,0]
# nums = [-1,-2,-3,-4,-5]
target = 9

res = []

assert 2 <= len(nums) <= 10**4
assert -10**9 <= target <= 10**9

for i, value in enumerate(nums):
    assert -10**9 <= value <= 10**9
    if (target - value) in nums:
        if nums.index(target - value) != i:
            res = [i, nums.index(target - value)]
            break

if res:
    print(res)
else:
    print("FAIL")
