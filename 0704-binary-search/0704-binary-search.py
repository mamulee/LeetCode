class Solution:
    def bs(self, st, en, nums, target) -> int:
        if st == en:
            return st if nums[st] == target else -1
        
        mid = (st + en) // 2
        if nums[mid] < target:
            return self.bs(mid + 1, en, nums, target)
        else:
            return self.bs(st, mid, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.bs(0, len(nums) - 1, nums, target)