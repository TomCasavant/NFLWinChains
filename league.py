
class Team:
	"""A node, representing a team in a graph"""
	def __init__(self, name):
		self.name = name
		self.wins = []
		self.losses = []
		self.seen = False

	def numberOfWins(self):
		self.numWins = len(self.wins)

	def numberOfLosses(self):
		self.numLosses = len(self.losses)



class League:
	""" A collection of team nodes representing the league (i.e the graph of nodes"""
	def __init__(self):
		self.teams = []
		self.rankedTeams = []

	def winChain(self, team1, team2):
		"""Finds the shortest path (of wins) between team1 and team2 using Dijkstra's algortithm"""
		currentChain = []
		for team in team1.wins:
			newChain = []
			if (team == team2):
				currentChain = [team]
			elif (not team.seen):
				team.seen = True
				newChain += [team] + self.winChain(team, team2)
				if(len(currentChain) == 0):
					currentChain += newChain
				elif (len(newChain) < len(currentChain)):
					currentChain = newChain
		return currentChain


if __name__ == "__main__":
	bengals = Team("bengals")
	ravens = Team("ravens")
	browns = Team("browns")
	steelers = Team("steelers")

	bengals.wins = [ravens]
	ravens.wins = [browns]
	steelers.wins = [bengals, browns, ravens]
	browns.wins = [bengals, steelers]
	league = League()
	chain = league.winChain(bengals, steelers)
	for team in chain:
		print (team.name)
