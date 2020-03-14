class Team:
    name = ""
    matches = 0
    wins = 0
    losses = 0
    draws = 0
    points = 0

    def __init__(self, teamname):
        self.name = teamname

    def loss(self):
        self.losses += 1
        self.matches += 1

    def win(self):
        self.wins += 1
        self.matches += 1
        self.points += 3

    def draw(self):
        self.draws += 1
        self.matches += 1
        self.points += 1

    def __repr__(self):
        return '{:<30} |  {} |  {} |  {} |  {} |  {}'.format(self.name,self.matches,self.wins, self.draws, self.losses, self.points)

def tally(rows):
    teams = {}
    for row in rows:
        results = row.split(";")
        if results[0] not in teams:
            teams[results[0]] = Team(results[0])
        if results[1] not in teams:
            teams[results[1]] = Team(results[1])
        if results[2] == "win":
            teams[results[0]].win()
            teams[results[1]].loss()
        elif results[2] == "loss":
            teams[results[1]].win()
            teams[results[0]].loss()
        elif results[2] == "draw":
            teams[results[0]].draw()
            teams[results[1]].draw()


    sorting_table = {}
    sorted_table = ["Team                           | MP |  W |  D |  L |  P"]
    for team in teams.keys():
        sorting_table[team] = teams[team].points
    for sort_team in {key: value for key, value in sorted(sorting_table.items(), key=lambda item: (-item[1], item[0]))}:
        sorted_table.append(str(teams[sort_team]))

    return sorted_table