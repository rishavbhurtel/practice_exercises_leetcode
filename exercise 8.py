class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        set_sentence = set(sentence)
        if len(set_sentence) == 26:
            return True
        else:
            return False
