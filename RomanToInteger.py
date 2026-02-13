class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I" : 1,"V" : 5,"X" : 10,"L" : 50,"C" : 100,"D" : 500,"M" : 1000}
        var = [roman[x] for x in s]
        total = 0
        for x in range(0, len(var)):
            if x+1 != len(var) and var[x] >= var[x+1]:
                total += var[x]
            elif x+1 != len(var) and var[x] < var[x+1]:
                total -= var[x]
            elif x+1 == len(var):
                total += var[x]
        return total
