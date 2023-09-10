class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr_1 = [0] * 26
        arr_2 = [0] * 26
        for ch in s:
            arr_1[ord(ch)-97] += 1
        
        for ch in t:
            arr_2[ord(ch)-97] += 1
        
        for i in range(26):
            if arr_1[i] != arr_2[i]:
                return False

        return True