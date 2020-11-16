import os
import time
import re
from slackclient import SlackClient
import requests
import mysql.connector
import logging
logging.basicConfig()

#DBA Connection
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="password")


# instantiate Slack client
slack_client = SlackClient('xoxb-1474844397573-1502414790320-wZK8mj2JrBPaDtE8V5yuw4rY')
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
INFO_COMMAND = "info"
HELP_COMMAND = "help"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"
url = None

def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def handle_command(command, channel):
    """
        Executes bot command if the command is known
    """
    # Default response is help text for the user
    default_response = "Not sure what you mean. Try *{}*.".format(HELP_COMMAND)

    # Finds and executes the given command, filling in response
    response = None
    # This is where you start to implement more commands!
    if command.startswith(INFO_COMMAND):
        
        #JSON Request to middleware
        

        #response = requests.post(URL, data= jsonRequest)
        response = "Sure...write some more code then I can do that!"

	if command.startswith(HELP_COMMAND):
    	respose = "Puede utilizar el comando info"

    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response or default_response
    )

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")
#def main():
#	HOST = '127.0.0.1'
#
#	info = {
#	"id": "EUApp_CC8Project001",
#	"url": "192.168.1.14",
#	"date": "1989-12-20T07:35:12.457Z"
#	}
#
#	y = json.dumps(info)
#	print(y)

#'xoxb-1474844397573-1478320398931-Er7uRLXEbZSMUrQ81fAGijfF'