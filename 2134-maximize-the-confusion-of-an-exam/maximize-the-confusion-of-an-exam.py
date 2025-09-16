class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l=0
        m=0
        true=0
        false=0
        max_true=0
        max_false=0
        for r in range(len(answerKey)):
            if answerKey[r]=="F":
                false+=1
            while false>k:
                if answerKey[l]=="F":
                    false-=1
                l+=1
            max_false=max(max_false,r-l+1)
        for h in range(len(answerKey)):
            if answerKey[h]=="T":
                true+=1
            while true>k:
                if answerKey[m]=="T":
                    true-=1
                m+=1
            max_true=max(max_true,h-m+1)
        return max(max_true,max_false)
        

        

        