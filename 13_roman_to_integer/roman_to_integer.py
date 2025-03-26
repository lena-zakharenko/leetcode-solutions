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

len_input = len(input)
sum = 0

i = 0
while i <= (len(input)) - 1:
    if i+1 <= len(input) - 1:
        if symbols[input[i]] < symbols[input[i+1]]:
            sum = sum + (symbols[input[i+1]] - symbols[input[i]])
            i = i + 2
        elif symbols[input[i]] == symbols[input[i+1]]:
            sum = sum + symbols[input[i]]
            i = i + 1
        elif symbols[input[i]] > symbols[input[i+1]]:
            sum = sum + symbols[input[i]]
            i = i + 1
        else:
            print("Something went wrong")
    else:
        print("End of input")
        sum = sum + symbols[input[i]]
        i = i + 1

print(sum)