import os

key = os.environ.get('RIOT_API_KEY', 'add_key_here')

# this key is low usage, mostly for retrieving the users current game
API_KEY = key

# this key is very high usage, used to gather data for machine learning
DATA_GATHERING_API_KEY = key
