class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)

        seen = set()
        q = deque()

        q.append((-1, 0))
        seen.add(0)

        while q:
            parent, node = q.popleft()

            for nei in adj[node]:
                if nei not in seen:
                    seen.add(nei)
                    q.append((node, nei))
                elif nei != parent:
                    return False

        return len(seen) == n
                    
            