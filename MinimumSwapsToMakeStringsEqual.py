class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x_y = 0
        y_x = 0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            if s1[i] == 'x' and s2[i] == 'y':
                x_y += 1
            elif s1[i] == 'y' and s2[i] == 'x':
                y_x += 1
        if (x_y + y_x) % 2 != 0:
            return -1
        else:
            x_y2 = x_y // 2
            y_x2 = y_x // 2
            return (x_y2 + y_x2) if x_y % 2 == 0 else (x_y2 + y_x2 + 2)
