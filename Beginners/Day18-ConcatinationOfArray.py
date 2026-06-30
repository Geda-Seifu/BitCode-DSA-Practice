class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        i=0
        j=0
        while i < 2*len(nums):
            if(i<len(nums)):
                ans.append(nums[i])
            else:
                ans.append(nums[j])
                j+=1
            i+=1
        return ans

