from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folder_stack = []

        for log in logs:
            if log == "../":
                if folder_stack: folder_stack.pop()

            elif log == "./":
                continue

            else:
                folder_stack.append(log)

        return len(folder_stack)
