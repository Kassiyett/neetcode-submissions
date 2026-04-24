class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        names = {}
        emailsGraph = defaultdict(list)

        for account in accounts:
            name = account[0]
            firstEmail = account[1]
            for email in account[1:]:
                emailsGraph[firstEmail].append(email) # neet@gmail.com : neet_dsa@gmail.com
                emailsGraph[email].append(firstEmail) # neet_dsa@gmail.com : neet@gmail.com
                names[email] = name # neet@gmail.com : neet
        
        visited = set() # emails
        result = []
        def dfs(email, components):
            visited.add(email)
            components.append(email)
            for nei in emailsGraph[email]:
                if nei not in visited:
                    dfs(nei, components)
        
        for email in emailsGraph:
            components = []
            if email not in visited:
                dfs(email, components)
                result.append([names[email]] + sorted(components))
                
        return result