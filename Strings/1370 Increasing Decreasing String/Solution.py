from string import ascii_lowercase
class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        frequency = {}
        for c in s:
            if c not in frequency:
                frequency[c] = 0
            frequency[c] += 1
            
        i = 0
        output = ""
        while i < len(s):
            for c in ascii_lowercase:
                if c in frequency and frequency[c] > 0:
                    output += c
                    frequency[c] -= 1
                    i += 1
            
            for c in ascii_lowercase[::-1]:
                if c in frequency and frequency[c] > 0:
                    output += c
                    frequency[c] -= 1
                    i += 1
        return output