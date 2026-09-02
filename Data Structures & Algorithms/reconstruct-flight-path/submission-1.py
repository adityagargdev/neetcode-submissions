import heapq
from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(adj[src], dst)  # min-heap keeps lexical order

        route = []
        def visit(airport):
            while adj[airport]:
                next_dest = heapq.heappop(adj[airport])
                visit(next_dest)
            route.append(airport)  # post-order: append AFTER exhausting all edges

        visit("JFK")
        return route[::-1]