class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        nums: 1, 2
        if + - * /
        2, 1 add = 3
        3, 3


        """
        s = [] # stack

        for t in tokens:
            if t == "+":
                n1 = s.pop()
                n2 = s.pop()
                s.append(n1+n2)
            elif t == "*":
                n1 = s.pop()
                n2 = s.pop()
                s.append(n1*n2)
            elif t == "/":
                n1 = s.pop()
                n2 = s.pop()
                s.append(int(n2/n1))
            elif t == "-":
                n1 = s.pop()
                n2 = s.pop()
                s.append(n2-n1)
            else:
                s.append(int(t))
            print(s)
        return s.pop()