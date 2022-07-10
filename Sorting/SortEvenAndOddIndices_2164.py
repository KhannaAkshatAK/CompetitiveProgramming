class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        n=len(nums) 
        
        for j in range(0,n-2,2):
            swap=False
            for i in range(0,n-2-j,2):
                if nums[i]>nums[i+2]:
                    nums[i],nums[i+2]=nums[i+2],nums[i]
                    swap=True                
            if swap==False:
                break
                
        for j in range(1,n-2,2):
            swap=False
            for i in range(0,n-2-j,2):
                if nums[i+1]<nums[i+3]:
                    nums[i+1],nums[i+3]=nums[i+3],nums[i+1]
                    swap=True
            if swap==False:
                break
                
        return nums
