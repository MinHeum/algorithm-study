class Solution:
    def myAtoi(self, s: str) -> int:
        arr = s.split()
        if len(arr) == 0:
            return 0
        for word in arr:
            temp = ''
            for ch in word:
                if ch.isdecimal():
                    temp += ch
                elif ch == '-' or ch == '+':
                    if len(temp) == 0:
                        temp += ch
                    else:
                        break
                else:
                    break
            if len(temp) == 0 or temp == '-' or temp == '+':
                return 0
            if int(temp) < -2 ** 31:
                return -2 ** 31 
            if int(temp) > 2 ** 31 - 1:
                return 2 ** 31 - 1 
            return int(temp)
        
        return 0
           