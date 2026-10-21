class Solution(object):
    def letterCombinations(self, digits):
        

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = [""]

        for digit in digits:
            letters = phone[digit]
            temp = []

            for combination in result:
                for letter in letters:
                    temp.append(combination + letter)

            result = temp

        return result

        """
        :type digits: str
        :rtype: List[str]
        """
        