class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        list_nums = []
        num = 0

        try:
            i = 0
            while i < (len(s)):
                if len(list_nums) >=2:
                    if list_nums[-2] <= list_nums[-1]:
                        raise RuntimeError(f"The input number {s} is not a real number.")
                num = 0
                if i+1 < len(s):
                    if symbols[s[i]] < symbols[s[i+1]]:
                        num = symbols[s[i+1]] - symbols[s[i]]
                        list_nums.append(num)
                        i = i + 2
                    elif symbols[s[i]] == symbols[s[i+1]]:
                        if symbols[s[i]] == symbols[s[i+2]]:
                            num = symbols[s[i]] + symbols[s[i + 1]] + symbols[s[i + 2]]
                            list_nums.append(num)
                            i = i + 3
                        else:
                            num = symbols[s[i]] + symbols[s[i + 1]]
                            list_nums.append(num)
                            i = i + 2
                    elif symbols[s[i]] > symbols[s[i+1]]:
                        num = symbols[s[i]]
                        list_nums.append(num)
                        i = i + 1
                    else:
                        print("Something went wrong")
                else:
                    num = symbols[s[i]]
                    list_nums.append(num)
                    if len(list_nums) >= 2:
                        if list_nums[-2] <= list_nums[-1]:
                            raise RuntimeError(f"The input number {s} is not a real number.")
                    i = i + 1
        except KeyError:
            raise RuntimeError(f"The input number {s} is not a real number.")

        sum_nums = sum([number for number in list_nums])
        return sum_nums


class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        sum_nums = 0

        i = 0
        while i < (len(s)):
            if i+1 < len(s):
                if symbols[s[i]] < symbols[s[i+1]]:
                    sum_nums = sum_nums + (symbols[s[i+1]] - symbols[s[i]])
                    i = i + 2
                elif symbols[s[i]] == symbols[s[i+1]]:
                    sum_nums = sum_nums + symbols[s[i]] + symbols[s[i+1]]
                    i = i + 2
                elif symbols[s[i]] > symbols[s[i+1]]:
                    sum_nums = sum_nums + symbols[s[i]]
                    i = i + 1
                else:
                    print("Something went wrong")
            else:
                sum_nums = sum_nums + symbols[s[i]]
                i = i + 1

        return sum_nums