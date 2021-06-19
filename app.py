# non blocking
from ml.NN import Predictor
from ml.secrets import *
from ml.RiotAPI import RiotAPI
from ml.DataGathering import DataGatherer
import os
import pickle
from flask_cors import CORS
from flask import Flask, send_from_directory, jsonify


app = Flask(__name__, static_folder='frontend/build')
CORS(app)


# Serve React App


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

# -------------------------------------------------------------------------------------------


gatherer = DataGatherer(0, 0)
riotAPI = RiotAPI(API_KEY)
with open('ml/models/NN.model', 'rb') as model_file:
    # load model from file
    predictor = Predictor(pickle.load(model_file))


@app.route('/api/winprob-by-summoner/<summonername>', methods=['GET'])
def get_win_probability_by_summonername(summonername):
    summoner_info = riotAPI.get_summoner_info(summonername)
    if not summoner_info:
        return jsonify({'msg': 'User Not Found (NA)'}), 404
    match = riotAPI.get_live_match(summoner_info['id'])
    if not match:
        return jsonify({'msg': 'User Not In Game'}), 404

    summoner_on_first_team = True
    for index in range(0, 10):
        if match["participants"][index]["summonerName"] == summonername:
            summoner_on_first_team = index <= 4

    # looking into speeding  this step up
    row = gatherer.live_match_to_row(match)
    first_team_result = predictor.predict(row)
    result = first_team_result if summoner_on_first_team else not first_team_result

    return jsonify({'win': bool(result)}), 200


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
