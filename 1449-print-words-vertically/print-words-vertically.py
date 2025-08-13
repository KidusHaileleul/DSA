class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max(len(word) for word in words)
        new_words = []
        for i in range(max_len):
            row_letters = []
            for word in words:
                if i < len(word):
                    row_letters.append(word[i])
                else:
                    row_letters.append(" ")
            new_words.append("".join(row_letters).rstrip())
        return new_words

        