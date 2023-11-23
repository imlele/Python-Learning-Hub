class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

#### OR ####
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """        
        s[:] = s[::-1]

#### OR ####
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """        
        for i in range(len(s) // 2):
            s[i], s[-i-1] = s[-i-1], s[i] # a, b = b, a       swaps a and b
        