import csv

from .RiotAPI import RiotAPI
from .secrets import *

STARTING_SUMMONER = 'Jefferson'


class DataGatherer:

    def __init__(self, max_depth, num_of_recent_matches):
        self.max_depth = max_depth
        self.num_of_recent_matches = num_of_recent_matches

        self.RiotAPI = RiotAPI(DATA_GATHERING_API_KEY)
        self.seen_matches = {}
    # main function to gather data

    def gather_data(self):
        with open('backend/ml/datasets/lol_data.csv', 'w+') as file:
            fieldnames = ['c1', 'c2', 'c3', 'c4', 'c5',
                          'c6', 'c7', 'c8', 'c9', 'c10',

                          's1r', 's2r', 's3r', 's4r', 's5r',
                          's6r', 's7r', 's8r', 's9r', 's10r',

                          's1ts', 's2ts', 's3ts', 's4ts', 's5ts',
                          's6ts', 's7ts', 's8ts', 's9ts', 's10ts',

                          'result', 'gamemode']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            self._recursive_gatherer(
                writer, self.RiotAPI.get_summoner_info(STARTING_SUMMONER)['puuid'])

    # recursively gather data

    def _recursive_gatherer(self, writer, puuid, depth=0):
        if depth == self.max_depth:
            return
        most_recent_matches = self.RiotAPI.get_most_recent_matches(
            puuid, self.num_of_recent_matches)

        try:
            for match in most_recent_matches:
                # if we already inserted this match, skip it
                if match['metadata']["matchId"] in self.seen_matches:
                    continue
                self.seen_matches[match['metadata']["matchId"]] = True

                (lowest, highest) = self._insert_data_point(
                    writer, match)
                if lowest and highest:
                    self._recursive_gatherer(writer, lowest, depth + 1)
                    self._recursive_gatherer(writer, highest, depth + 1)
        except Exception as e:
            print(e)

    # inserts the match into the csv file, returns the lowest, middle and highest mmr player from the match
    # # maybe to improve learing, we should insert each match 2 times, 1 win 1 loss (mirrored entry)
    def _insert_data_point(self, writer, match):
        (row, lowest, highest) = self.match_to_row(match)
        writer.writerow(row)
        print(row)
        print((lowest, highest))
        return (lowest, highest)

    # translate a match object into a row object
    # also returns the puuid of the lowest and highest mmr player of the game
    def match_to_row(self, match):
        partics = match["info"]["participants"]
        game_mode = self._gamemode_translate(match["info"]["gameMode"])

        mmt = {  # min max tracker
            'min': 9999,
            'minpuuid': None,
            'max': 0,
            'maxpuuid': None
        }
        row = {}
        for index in range(0, 10):
            i = str(index+1)

            puuid = partics[index]["puuid"]
            mmr = self.RiotAPI.get_summoner_mmr(
                partics[index]["summonerName"], game_mode)

            if mmr < mmt['min']:
                mmt['min'] = mmr
                mmt['minpuuid'] = puuid
            elif mmr > mmt['max']:
                mmt['max'] = mmr
                mmt['maxpuuid'] = puuid

            row['c'+i] = partics[index]["championId"]
            row['s'+i+'r'] = mmr
            row['s'+i+'ts'] = self.RiotAPI.get_tilt_score(puuid)
        # if the first 1-5 summoners win or not
        row['result'] = partics[0]["win"]
        row['gamemode'] = game_mode
        return (row, mmt['minpuuid'], mmt['maxpuuid'])

    def live_match_to_row(self, match):
        partics = match["participants"]
        game_mode = self._gamemode_translate(match["gameMode"])

        row = {}
        for index in range(0, 10):
            i = str(index+1)

            puuid = self.RiotAPI.get_summoner_info(
                partics[index]["summonerName"])['puuid']
            mmr = self.RiotAPI.get_summoner_mmr(
                partics[index]["summonerName"], game_mode)

            row['c'+i] = partics[index]["championId"]
            row['s'+i+'r'] = mmr
            row['s'+i+'ts'] = self.RiotAPI.get_tilt_score(puuid)
        # if the first 1-5 summoners win or not
        row['gamemode'] = game_mode
        return row

    # translate between riot language and whatismymmr
    def _gamemode_translate(self, game_mode):
        # try to use ARAM mmr for aram games, else just use ranked
        return 'ARAM' if game_mode == 'ARAM' else 'ranked'


# a = DataGatherer(10, 5)
# a.gather_data()
