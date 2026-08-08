class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowSum = sum(nums[ :k])
        maxSum = windowSum

        for i in range (k , len(nums)):
            windowSum = windowSum - nums[i - k] + nums [i]
            maxSum = max(windowSum , maxSum)

        return maxSum / k
