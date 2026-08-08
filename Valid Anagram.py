class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        # Count characters
        for ch in s:
            count[ch] = count.get(ch , 0) + 1
        # Remove characters
        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1

            if count[ch] < 0:    # so that  -Ve value ko satisfie na kare
                return False

        return True
        