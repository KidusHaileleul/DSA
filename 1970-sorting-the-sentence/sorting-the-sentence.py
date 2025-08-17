class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        x=[i[::-1]for i in s]
        x=sorted(x)
        y=[j[::-1]for j in x]
        e=" ".join(y)
        e = ''.join(char for char in e if not char.isdigit())
        return e