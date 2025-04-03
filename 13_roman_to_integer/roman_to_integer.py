symbols = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

# input = "III"
# input = "LVIII"
input = "MCMXCIV"
# input = "XIX"
# input = "XIIX"
# input = "SXIX"
# input = "DMLSI"

list_nums = []
num = 0

try:
    i = 0
    while i < (len(input)):
        if len(list_nums) >=2:
            if list_nums[-2] <= list_nums[-1]:
                raise RuntimeError(f"The input number {input} is not a real number.")
        num = 0
        if i+1 < len(input):
            if symbols[input[i]] < symbols[input[i+1]]:
                num = symbols[input[i+1]] - symbols[input[i]]
                list_nums.append(num)
                i = i + 2
            elif symbols[input[i]] == symbols[input[i+1]]:
                if symbols[input[i]] == symbols[input[i+2]]:
                    num = symbols[input[i]] + symbols[input[i + 1]] + symbols[input[i + 2]]
                    list_nums.append(num)
                    i = i + 3
                else:
                    num = symbols[input[i]] + symbols[input[i + 1]]
                    list_nums.append(num)
                    i = i + 2
            elif symbols[input[i]] > symbols[input[i+1]]:
                num = symbols[input[i]]
                list_nums.append(num)
                i = i + 1
            else:
                print("Something went wrong")
        else:
            print("End of input")
            num = symbols[input[i]]
            list_nums.append(num)
            if len(list_nums) >= 2:
                if list_nums[-2] <= list_nums[-1]:
                    raise RuntimeError(f"The input number {input} is not a real number.")
            i = i + 1
except KeyError:
    raise RuntimeError(f"The input number {input} is not a real number.")

sum_nums = sum([number for number in list_nums])
print(sum_nums)
