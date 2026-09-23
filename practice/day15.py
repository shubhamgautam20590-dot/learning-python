#to find largest no in the list without max()

class Solution:
    def findLargest(self,nums):
        maximum= nums[0]

        for i in range(len(nums)):
            if nums[i]>maximum:
                maximum=nums[i]

        return(maximum)

nums = [2, 5, 7, 6, 9]
obj=Solution()
print(obj.findLargest(nums))        