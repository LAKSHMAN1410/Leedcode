class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev=0
        n=x
        if x >= 0:
            while n > 0:
                digit=n%10
                rev=rev*10+digit
                n=n//10
            if rev==x:
                return True
            else:
                return False    
        else:
            return False