def twoSum(nums, target):
    
    for n in range(len(nums)):
        for m in range(n + 1,len(nums)):
            if nums[n] + nums[m] == target:
                print(n, m)
    
print(twoSum([2,15,11,7],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))