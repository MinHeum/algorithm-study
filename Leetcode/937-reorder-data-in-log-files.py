class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def flat(lst):
            flat_list = []
            for item in lst:
                if isinstance(item, list):
                    flat_list.extend(flat(item))
                else:
                    flat_list.append(item)
            return flat_list

        letter_arr = []
        digit_arr = []
        modified_log = []
        answer = []

        for log in logs:
            splited_log = log.split()
            identifier = splited_log[:1][0]
            content = splited_log[1:]
            modified_log.append([identifier, content])

        for log in modified_log:
            if log[1][0].isalpha():
                letter_arr.append([log[0],log[1]])
            else:
                digit_arr.append([log[0],log[1]])

        letter_arr.sort(key= lambda x: (x[1], x[0]))
        
        for letter in letter_arr:
            answer.append(' '.join(flat(letter)))

        for digit in digit_arr:
            answer.append(' '.join(flat(digit)))

        return answer
