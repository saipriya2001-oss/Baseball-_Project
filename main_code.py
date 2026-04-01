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
   
    
    # Focus: Translating baseball stats into a flow network.
    # =========================================================
    def build_graph(self, team):
        """Creates the nodes and capacities for the Max-Flow problem."""
        capacity = {"S": {}}
        source, sink = "S", "T"
        max_wins = self.wins[team] + self.remaining[team]
        others = [t for t in self.teams if t != team]

        # 1. Create Game Nodes (Source -> Game_Node)
        for i in range(len(others)):
            for j in range(i + 1, len(others)):
                t1, t2 = others[i], others[j]
                game_node = f"{t1}_{t2}"
                
                # Capacity is the number of games left between these two teams
                capacity[source][game_node] = self.games[t1][t2]
                
                # Game Node -> Team Nodes (Infinite capacity)
                capacity[game_node] = {t1: float('inf'), t2: float('inf')}

        # 2. Create Team Nodes (Team -> Sink)
        for t in others:
            if t not in capacity: capacity[t] = {}
            # Capacity is how many more games this team can win without passing our team
            val = max_wins - self.wins[t]
            capacity[t][sink] = max(0, val)

        return capacity, source, sink, others

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
    
    def certificate_of_elimination(self, team):
        """Finds the subset of teams responsible for the elimination."""
        trivial, by = self.is_trivial(team)
        if trivial: return by

        capacity, source, sink, others = self.build_graph(team)
        _, flow = self.max_flow(capacity, source, sink)

        # To find the Min-Cut, find all nodes reachable in the residual graph
        visited = set()
        queue = deque([source])
        while queue:
            u = queue.popleft()
            if u in visited: continue
            visited.add(u)
            # Forward reachable
            for v in capacity.get(u, {}):
                if capacity[u][v] - flow[u][v] > 0 and v not in visited:
                    queue.append(v)
            # Backward reachable
            for v in flow:
                if u in flow[v] and flow[v][u] > 0 and v not in visited:
                    queue.append(v)

        # Any team node reachable from source is in the 'Eliminating Subset'
        return [t for t in others if t in visited]


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