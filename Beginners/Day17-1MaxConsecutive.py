def findMaxConsecutiveOnes( nums):
        count = 0
        max_value = 0
        
        for i in nums:
            if i == 1 :
                count +=1
            else :
                if count > max_value:
                    max_value = count
                count = 0
        return max(count, max_value)
