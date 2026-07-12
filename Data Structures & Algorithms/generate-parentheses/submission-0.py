class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open_count, close_count, curr):
            if len(curr) == 2 * n:
                res.append(curr)
                return
            if open_count < n:
                dfs(open_count + 1, close_count, curr + "(")
            if close_count < open_count:
                dfs(open_count, close_count + 1, curr + ")")

        dfs(0, 0, "")
        return res