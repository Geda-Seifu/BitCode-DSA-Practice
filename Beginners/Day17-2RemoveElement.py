
def removeElement( nums, val):
        count = 0
        
        for i in nums:
            if i == val:
                count +=1
                
        for i in range(count):
            nums.remove(val)        

        return len(nums)
    
    
removeElement([3,2,2,3],3)