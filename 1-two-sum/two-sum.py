class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashy={}
        for i,j in enumerate(nums):
            secondnum= target- j
            if secondnum in hashy:
                return [hashy[secondnum], i]
            hashy[j]=i