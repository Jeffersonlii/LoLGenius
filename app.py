from flask import Flask
import pickle

from backend.ml.DataGathering import DataGatherer
from backend.ml.RiotAPI import RiotAPI
from backend.ml.secrets import *
from backend.ml.NN import Predictor

app = Flask(__name__)

predictor = None
gatherer = None
riotAPI = None


def instantiations():
    # todo load in model to use
    global predictor
    global gatherer
    global riotAPI

    gatherer = DataGatherer(0, 0)
    riotAPI = RiotAPI(API_KEY)

    with open('ml/models/NN.model', 'rb') as model_file:
        # load model from file
        predictor = Predictor(pickle.load(model_file))
    pass


instantiations()


@app.route('/winprob-by-summoner/<summonername>', methods=['GET'])
def get_win_probability_by_summonername(summonername):
    summoner_info = riotAPI.get_summoner_info(summonername)
    if not summoner_info:
        return 'user doesnt exist'
    match = riotAPI.get_live_match(summoner_info['id'])
    if not match:
        return 'user not in game'

    summoner_on_first_team = True
    for index in range(0, 10):
        if match["participants"][index]["summonerName"] == summonername:
            summoner_on_first_team = index <= 4

    row = gatherer.live_match_to_row(match)
    first_team_result = predictor.predict(row)
    result = first_team_result if summoner_on_first_team else not first_team_result
    return 'win!' if result else 'loss'


if __name__ == '__main__':
    app.run(debug=True)
