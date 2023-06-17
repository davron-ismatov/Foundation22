class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        dct = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        lst = []
        length = len(digits)
        for i in dct[digits[0]]:
            if length>1:
                for a in dct[digits[1]]:
                    if length>2:
                        for j in dct[digits[2]]:
                            if length>3:
                                for k in dct[digits[3]]:
                                    lst.append(i+a+j+k)
                            else:
                                lst.append(i+a+j)
                    else:
                        lst.append(i+a)
            else:
                lst.extend(i)
        return lst     