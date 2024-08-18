class Solution:
    def triangleType(self, nums: List[int]) -> str:
        
        s = sum(nums)
        max_length_sides = max(nums)
        
        if max_length_sides >= s - max_length_sides :
            return "none"
        
        # check scalene 
        a,b,c = nums
        ans = "scalene"
        
        # check isosceles
        for i,v in enumerate(nums):
            arrs = []
            for j,item in enumerate(nums):
                if i != j :
                    arrs.append(item)
            b,c = arrs 
            if v == b or v == c :
                ans = "isosceles"
        

        # check equilateral 
        for i,v in enumerate(nums):
            arrs = []
            for j,item in enumerate(nums):
                if i != j :
                    arrs.append(item)
            b,c = arrs 
            
            if v == b and v == c and b == c :
                ans = "equilateral"
        return ans