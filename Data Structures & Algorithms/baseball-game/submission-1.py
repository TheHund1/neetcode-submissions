class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        result = 0
        for char in operations:
            if char == "+":
                points = stack[-1] + stack[-2]
                stack.append(points)
                result += points
            elif char == "D":
                points = 2 * stack[-1]
                stack.append(points)
                result += points
            elif char == "C":
                points = stack.pop()
                result -= points
            else:
                points = int(char)
                stack.append(points)
                result += points
        return result