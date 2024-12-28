def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] + nums[j] == target:
                return [i,j]
        
nums = nums =[3,2,3]
target = 6

print(twoSum(nums,target))

l1 = [2,4,3]
l2 = [5,6,4]

a = split(l1,2)

b = str(l2.reverse())

print(a,l2)