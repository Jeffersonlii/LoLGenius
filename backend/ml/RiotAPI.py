
import secrets
import requests
import sys

API_PATHS = {
    4: r"https://na1.api.riotgames.com/",
    5: r"https://americas.api.riotgames.com/"
}


class RiotAPI():

    def __init__(self, API_KEY):
        self.API_KEY = API_KEY

    # builds the api call url

    def _get_url(self, strng, version=4):
        try:
            r = requests.get(
                API_PATHS[version]+strng, headers={"X-Riot-Token": self.API_KEY})
            r.raise_for_status()
            return r.json()
        except requests.exceptions.HTTPError as e:
            print(e)
            print('riot api request error (most likely rate limited)')
        return None

    def get_summoner_info(self, summonername: str):
        # https://developer.riotgames.com/apis#summoner-v4/GET_getBySummonerName
        return self._get_url(
            'lol/summoner/v4/summoners/by-name/'+summonername)

    def get_live_match(self, summonerID: str):
        # https://developer.riotgames.com/apis#spectator-v4/GET_getCurrentGameInfoBySummoner
        return self._get_url(
            'lol/spectator/v4/active-games/by-summoner/'+summonerID)

    def get_most_recent_match(self, puuid: str):
        # https://developer.riotgames.com/apis#match-v5/GET_getMatch
        matchID = self._get_url('lol/match/v5/matches/by-puuid/' +
                                puuid+'/ids?start=0&count=1', 5)[0]
        return self._get_url('lol/match/v5/matches/'+matchID, 5)

    def get_tilt_score(self, puuid: str) -> int:
        tilt_score = 0
        last_n_games = 5

        matchIDs = RiotAPI._get_url('lol/match/v5/matches/by-puuid/' +
                                    puuid+'/ids?start=0&count='+str(last_n_games), 5)
        for i, matchID in enumerate(matchIDs):
            match_details = RiotAPI._get_url(
                'lol/match/v5/matches/'+matchID, 5)
            for participant in match_details['info']['participants']:
                if participant['puuid'] == puuid:
                    weight = 10 * (last_n_games + 1 - i)
                    tilt_score += weight if participant['win'] else -weight
                    break
        return tilt_score

    def get_summoner_mmr(self, summonername: str, game_mode: str) -> int:
        mmr = 1000

        try:
            r = requests.get(
                'https://na.whatismymmr.com/api/v1/summoner?name='+summonername)
            r.raise_for_status()

            for mode, info in r.json().items():
                if info["avg"] != None:  # we have mmr for this mode
                    if mode == game_mode:  # if its the mode we're looking for, perfect!
                        return info["avg"]
                    mmr = info["avg"]  # store the next best mmr
            return mmr
        except requests.exceptions.HTTPError as e:
            print(e)
            print('no mmr found')
        return mmr  # default mmr

    # todo get patch number?


def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        def f(obj): return str(obj).encode(
            enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)
