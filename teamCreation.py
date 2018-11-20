import nflgame
from league import Team, League


teams = ['ARI','ATL','BAL','BUF','CAR','CHI','CIN','CLE','DAL','DEN','DET','GB','HOU','IND','JAX','KC','LA','MIA','MIN','NE','NO','NYG',
    'NYJ','OAK','PHI','PIT','SD','SEA','SF','STL','TB','TEN','WAS', 'LAC']


def getData(year, weeks):
	"""Gets all the games from the given year"""
	return nflgame.games(year, week=weeks)

def createLeague():
	"""Creates a league object and fills it with all the nfl teams"""
	league = League()
	for team in teams:
		league.teams.append(Team(team))

	return league

def loadLeague(league, data):
	"""Loads the league object with the results of all the games"""
	for game in data:
		if (game.winner != None): #If the game as finished
			position = league.positionOfTeam(game.winner)
			league.teams[position].wins.append(league.teams[league.positionOfTeam(game.loser)])


def compareTeams(team1, team2, league):
	"""Creates a chain linking the two given teams"""
	team1Pos = league.positionOfTeam(nflgame.standard_team(team1))
	team2Pos = league.positionOfTeam(nflgame.standard_team(team2))

	firstTeam = league.teams[team1Pos]
	secondTeam = league.teams[team2Pos]

	return league.getWinChain(firstTeam, secondTeam)


def setup():
        data = getData(2018, range(1,17))
        league = createLeague()
        loadLeague(league, data)
        return league

if __name__ == "__main__":

	data = getData(2018, range(1,15))
	league = createLeague()
	loadLeague(league, data)
	while True:
		chain = compareTeams(raw_input("First Team: "), raw_input("Second Team: "), league)
		result = ""
		for t in chain:
			result = result + t.name + " -> "

		print result
