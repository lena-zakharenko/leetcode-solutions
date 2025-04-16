#strs = ["flower","flow","flight"]
#strs = ["dog","racecar","car"]

strs = [""]
if len(strs) == 0:
    prefix = ""
elif len(strs) == 1:
    prefix = strs[0]
else:
    if len(strs[0]) < len(strs[1]):
        l = len(strs[0])
        while l >= 0:
            if l == 0:
                prefix = ""
                break
            else:
                if not strs[1].startswith(strs[0][:l]):
                    l = l - 1
                else:
                    prefix = strs[0][:l]
                    l = - 1
    else:
        l = len(strs[1])
        while l >= 0:
            if l == 0:
                prefix = ""
                break
            else:
                if not strs[0].startswith(strs[1][:l]):
                    l = l - 1
                else:
                    prefix = strs[1][:l]
                    print(prefix)
                    l = -1
i = 2
print("First prefix: ", prefix)
while i < len(strs):
    print("i: ", i)
    lp = len(prefix)
    while lp >= 0:
        print("lp: ", lp)
        if lp == 0:
            print("second prefix")
            prefix = ""
            break
        else:
            print("item: ", strs[i], "startswith ", prefix[:lp])
            if not strs[i].startswith(prefix[:lp]):
                lp = lp - 1
            else:
                prefix = prefix[:lp]
                lp = -1
    i = i + 1

print("Prefix :", prefix)
