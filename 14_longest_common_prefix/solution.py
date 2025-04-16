class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            if len(strs[0]) < len(strs[1]):
                l = len(strs[0])
                while l >= 0:
                    if l == 0:
                        return ""
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
                        return ""
                    else:
                        if not strs[0].startswith(strs[1][:l]):
                            l = l - 1
                        else:
                            prefix = strs[1][:l]
                            l = -1
            i = 2
            while i < len(strs):
                lp = len(prefix)
                while lp >= 0:
                    if lp == 0:
                        return ""
                    else:
                        if not strs[i].startswith(prefix[:lp]):
                            lp = lp - 1
                        else:
                            prefix = prefix[:lp]
                            lp = -1
                i = i + 1
            return prefix