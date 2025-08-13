class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == "#":
                combined = s[i] + s[i+1]
                result.append(int(combined))
                i += 3
            else:
                if s[i] != "#":
                    result.append(int(s[i]))
                i += 1
        letters = "".join(chr(num + 96) for num in result)
        return letters

  
    
        
        