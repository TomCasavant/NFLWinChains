import requests
import random
import time
from teamCreation import setup, compareTeams
from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read("config.ini")
GROUPME_TOKEN = config.get("GROUPME", "GROUPME_TOKEN")
GROUP_ID = config.get("GROUPME", "GROUP_ID")
BOT_ID = config.get("GROUPME", "BOT_ID")
keyword = "!nfl "

def postMessage(message):
	post_params = { 'bot_id' : BOT_ID, 'text': message }
	requests.post('https://api.groupme.com/v3/bots/post', params = post_params)

def getLatestMsgID(request_params):
	response = requests.get('https://api.groupme.com/v3/groups/' + GROUP_ID + '/messages', params = request_params).json()['response']['messages']
	for message in response:
		id = message['id']
	return id


def generateResponse(team1, team2, league):
	chain = compareTeams(team1, team2, league)
	result = []
	for team in chain:
		result.append(team.name)
	return " -> ".join(result)

if __name__ == "__main__":
	latestID = getLatestMsgID({'token': GROUPME_TOKEN})
	request_params = {'token': GROUPME_TOKEN, 'since_id': latestID}
	league = setup()
	while True:
		response = requests.get('https://api.groupme.com/v3/groups/' + GROUP_ID + '/messages', params = request_params)
		if (response.status_code == 200):
			try:
				response_messages = response.json()['response']['messages']
				for message in response_messages:
					if (keyword in message['text']):
						team = message['text'].replace(keyword, "").split()
						print (team[0], team[1])
						postMessage(generateResponse(team[0], team[1], league))
						request_params['since_id'] = message['id']
						break
			except:
				continue
		time.sleep(5)


