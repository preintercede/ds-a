'''Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Input: nums = [1,2,3,4]
Output: [1,3,6,10]

'''


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        # make an empty list and a temp variable
        addedList = []
        added = 0

        # loop through list and append the added variable to the new list
        for i in nums:
            added += i
            addedList.append(added)
        return addedList
