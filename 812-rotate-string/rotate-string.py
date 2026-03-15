class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        length = len(s)
        s = list(s)
        goal = list(goal)
        for i in range(length):
            element = s.pop(0)
            s.append(element)

            if s == goal:
                return True
        return False
        