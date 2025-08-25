class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x=set()
        i=0
        j=0
        answer=0
        while j < len(s):
            if s[j] not in x:
                x.add(s[j])
                answer=max(answer, j - i + 1)
                j += 1
            else:
                x.remove(s[i])
                i+=1
        return answer

        