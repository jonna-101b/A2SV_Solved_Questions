from typing import List

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        formatted_source = []
        line = []
        blockCommented = False

        for code in source:
            slashFound = False
            astericsFound = False
            line = line if line else []

            for char in code:
                if char == "/":
                    if astericsFound:
                        blockCommented = False
                        astericsFound = False

                    elif blockCommented:
                        continue

                    elif slashFound:
                        line.pop()
                        break

                    else:
                        slashFound = True
                        line.append(char)

                elif char == "*":
                    if slashFound:
                        blockCommented = True
                        slashFound = False
                        astericsFound = False
                        line.pop()

                    else:
                        if blockCommented:
                            astericsFound = True

                        else:
                            line.append(char)

                else:
                    if blockCommented:
                        slashFound = False
                        astericsFound = False
                        continue

                    line.append(char)
                    slashFound = False
                    astericsFound = False

            if line and blockCommented:
                continue

            line = "".join(line)
            if line != "":
                formatted_source.append(line)
            line = []

        if line and blockCommented:
            line = "".join(line)
            formatted_source.append(line)

        return formatted_source