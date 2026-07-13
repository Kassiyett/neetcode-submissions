class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res = 0
        adj = defaultdict(list)
        for i in range(len(times)):
            ui, vi, ti = times[i]
            adj[ui].append((vi, ti))

        dist = {k: 0}
        queue = deque([k])
        while queue:
            curr_vi = queue.popleft()
            curr_ti = dist[curr_vi]
            nei = adj[curr_vi]

            for vi, ti in nei:
                new_time = curr_ti + ti
                if vi not in dist or new_time < dist[vi]:
                    dist[vi] = new_time
                    queue.append(vi)
        if len(dist) != n:
            return -1
            
        return max(dist.values())

