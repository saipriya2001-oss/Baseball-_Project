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









if __name__ == "__main__":
    n = int(input("Enter number of teams: "))
    data = [input().split() for _ in range(n)]

    obj = BaseballElimination(n, data)
    for team in obj.teams:
        if obj.is_eliminated(team):
            print(f"{team} is eliminated by R = {obj.certificate_of_elimination(team)}")
        else:
            print(f"{team} is not eliminated")