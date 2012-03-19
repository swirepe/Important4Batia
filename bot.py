	# To fetch a single user's public status messages, where "user" is either
	# a Twitter "short name" or their user id.

	#   >>> statuses = api.GetUserTimeline(user)
	#   >>> print [s.text for s in statuses]

	# To use authentication, instantiate the twitter.Api class with a
	# consumer key and secret; and the oAuth key and secret:

	#   >>> api = twitter.Api(consumer_key='twitter consumer key',
	#                         consumer_secret='twitter consumer secret',
	#                         access_token_key='the_key_given',
	#                         access_token_secret='the_key_secret')

	#   >>> status = api.PostUpdate('I love python-twitter!')
	# >>> print status.text
	# I love python-twitter!

from message import compose_message
import twitter
import time
import shelve
from random import randint, choice
from clint.textui import colored

already_tweeted = None

api = None


def setup():
    global already_tweeted
    already_tweeted = shelve.open("already_tweeted.shelf")

    global api
    api = twitter.Api(consumer_key=open("consumer_key.txt").read(),
        consumer_secret=open('consumer_secret.txt').read(),
        access_token_key=open('access_token_key.txt').read(),
        access_token_secret='eomElR6mh4A4nTIq5Z6e0bQmrmQro1DLaOc534muVw')




def idle(minutes=15):
    """just hold on for a bit.  Time is in minutes."""
    print colored.blue("IDLING"), "for minutes = ", minutes
    time.sleep(minutes*60)



def _getTweets():
    """for retrying in case of capacity problems"""
    global api
    try:
        return api.GetUserTimeline("kreayshawn")
    except:
        idle(randint(1,5))
        return False


def getTweets(tries = 10):
    """
    Get the latest tweets from kreayshawn
    you know, I could make a retry metafunction..."""
    global api
    global already_tweeted
    attempt = 0
    s = _getTweets()
    while s == False and attempt < tries:
        s = _getTweets()
        attempt += 1

    if attempt >= tries:
        print colored.red("FAILURE"), "Failed to get any kreayshawn tweets."
        return []


    ret = [a.text for a in s if a.text not in already_tweeted.keys()]
    print colored.green("SUCCESS"), "Got this many unseen tweets:", len(ret)
    return ret

		
def post(message):
    try:
        api.PostUpdate(message)
        print colored.green("SUCCESS"), "Posted message successfully!"
        return True
    except:
        print colored.red("FAILURE"), "Failed to post message."
        return False


def save(msg):
    global already_tweeted
    already_tweeted[msg.encode("utf-8")] =  time.asctime(time.localtime())


def main():
    setup()

    while True:

        tweets = getTweets()
        if tweets != []:
            next_up = choice(tweets)
            msg = compose_message(next_up)
            
            if post(msg):
                save(next_up)

        idle()


if __name__ == "__main__":
    main()