class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        result = []
        for c in address:
            if c == '.':
                result.append("[.]")
            else:
                result.append(c)
        return "".join(result)

val=Solution()
s=input()
print(val.defangIPaddr(s)) 
