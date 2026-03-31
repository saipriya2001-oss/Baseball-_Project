from collections import deque

class BaseballElimination:

    # =========================================================
    # Focus: Parsing input and handling simple eliminations.
    # =========================================================
    def __init__(self, n, data):
        self.teams = []
        self.wins = {}
        self.losses = {}
        self.remaining = {}
        self.games = {}

        # Store team data into accessible dictionaries
        for i in range(n):
            team = data[i][0]
            self.teams.append(team)
            self.wins[team] = int(data[i][1])
            self.losses[team] = int(data[i][2])
            self.remaining[team] = int(data[i][3])

        # Store games matrix (who plays whom)
        for i in range(n):
            team = self.teams[i]
            self.games[team] = {}
            for j in range(n):
                opponent = self.teams[j]
                self.games[team][opponent] = int(data[i][4 + j])

    def is_trivial(self, team):
        """Checks if a team is eliminated just by current win totals."""
        max_wins = self.wins[team] + self.remaining[team]
        for other in self.teams:
            if self.wins[other] > max_wins:
                # If 'other' already has more wins than our max possible, we are out.
                return True, [other]
        return False, []


    # =========================================================
    # 
    # Focus: The mathematical 'Black Box' that calculates max flow.
    # =========================================================
    def bfs(self, capacity, flow, source, sink, parent):
        """Finds an augmenting path in the residual graph."""
        visited = set()
        queue = deque([source])
        visited.add(source)

        while queue:
            u = queue.popleft()
            for v in capacity.get(u, {}):
                if v not in visited and capacity[u][v] - flow[u][v] > 0:
                    parent[v] = u
                    visited.add(v)
                    queue.append(v)
                    if v == sink:
                        return True
        return False

    def max_flow(self, capacity, source, sink):
        """Standard Edmonds-Karp implementation."""
        flow = {u: {v: 0 for v in capacity[u]} for u in capacity}
        total_flow = 0
        parent = {}

        while self.bfs(capacity, flow, source, sink, parent):
            # Find the bottleneck capacity along the path found by BFS
            path_flow = float('inf')
            v = sink
            while v != source:
                u = parent[v]
                path_flow = min(path_flow, capacity[u][v] - flow[u][v])
                v = u

            # Update flow and residual edges
            v = sink
            while v != source:
                u = parent[v]
                flow[u][v] += path_flow
                if v not in flow: flow[v] = {}
                if u not in flow[v]: flow[v][u] = 0
                flow[v][u] -= path_flow
                v = u
            total_flow += path_flow

        return total_flow, flow

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------









# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
def is_eliminated(self, team):
        """Returns True if the team is mathematically eliminated."""
        trivial, _ = self.is_trivial(team)
        if trivial: return True

        capacity, source, sink, _ = self.build_graph(team)
        total_games_possible = sum(capacity[source].values())
        flow_value, _ = self.max_flow(capacity, source, sink)

        # If we couldn't fit all the remaining games into the flow, the team is out.
        return flow_value != total_games_possible

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
if __name__ == "__main__":
    n = int(input("Enter number of teams: "))
    data = [input().split() for _ in range(n)]

    obj = BaseballElimination(n, data)
    for team in obj.teams:
        if obj.is_eliminated(team):
            print(f"{team} is eliminated by R = {obj.certificate_of_elimination(team)}")
        else:
            print(f"{team} is not eliminated")