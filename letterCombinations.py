def letterCombinations(digits):
    def genCombinations(digits, current, res):
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if not digits:
            if current == '':
                return
            else: 
                res.append(current)
                return 
        
        first_dig = digits[0]
        for letter in digit_to_letters[first_dig]:
            genCombinations(digits[1:], current + letter, res)
    result = []
    genCombinations(digits, '', result)
    return result