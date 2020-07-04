nums = [-2,1,-3,4,-1,2,1,-5,4]

golbal_max, local_max = 0,0

if max(nums) < 0:
    golbal_max = max(nums)
else:
    for num in nums:
        local_max = max(0, local_max + num)
        golbal_max = max (golbal_max, local_max)
