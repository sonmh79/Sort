class Solution:
    # 스왑 조건에 부합하는지 판단
    def to_swap(self, n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)
    
    def largestNumber(self, nums: List[int]) -> str:
        
        # 삽입 정렬
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j-1],nums[j]):
                nums[j-1] , nums[j] = nums[j], nums[j-1]
                j -=1
            i += 1
            
        return str(int(''.join(map(str,nums))))
