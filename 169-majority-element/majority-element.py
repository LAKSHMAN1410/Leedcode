class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        d=Counter(nums)
        for k,v in d.items():
            if v>n/2:
                return k