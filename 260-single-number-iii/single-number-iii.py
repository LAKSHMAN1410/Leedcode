class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d=Counter(nums)
        arr=[]
        for k,v in d.items():
            if v==1:
                arr.append(k)
        return arr
