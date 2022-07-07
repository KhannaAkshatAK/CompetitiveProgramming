class Solution:
    def arrayPairSum(self, nums):
        nums=self.mergeSort(nums)
        tot=0
        for i in nums[::2]:
            tot+=i
        return tot
        
        
    def mergeSort(self, arr):
        n=len(arr)
        if n<=1:
            return arr
        mid=-n//2
        left=self.mergeSort(arr[:mid])
        right=self.mergeSort(arr[mid:])
        return self.mergeSortedArray(left,right)
    
    def mergeSortedArray(self,arrL,arrR):
        i=j=0
        a,b=len(arrL),len(arrR)
        newArr=[]
        while i<a and j<b:
            if arrL[i]>arrR[j]:
                newArr.append(arrR[j])
                j+=1
            else:
                newArr.append(arrL[i])
                i+=1
        while j<b:
            newArr.append(arrR[j])
            j+=1
        while i<a:
            newArr.append(arrL[i])
            i+=1
        return newArr
