# LoLgenius

Will you win your LoL match? \
LoLgenius can tell you using machine learing!

# Features

## Basic

-   Users can enter a username, the model runs through the current game of the user and gives
    a predicted result (W/L)

## Future

-   Users can specify 10 champions, patch number, and gamemode to give direct params to the model
-   Conduct some sort of dimensionality reduction analysis

# Dataset Gathering Method

-   Dataset is gathered through the RIOT GAMES API
-   MMR is gathered through 3rd party whatismymmr API

1. Starting with an initial summoner, we insert their most recent game into our dataset
2. We then recursively do the same for the lowest and highest mmr players within the game from step 1.
3. We give some sort of max depth to avoid overflow
4. As a result, we get a dataset with diverse ranks, modes, and champions.

# Keeping Data Fresh

-   League of Legends is updated very frequently
-   To keep data fresh and models accurate, we periodically flush our entire datamodel starting from scratch.

# Data Dimensionality

-   10 features for each champion played
-   10 features for each players mmr depending on the game mode
-   10 features for each players tilt score (based on previous winrate for the day)
-   1 feature for result of match (W/L)
-   1 feature for game mode

# Application Archetecture

## Frontend

-   A simple React frontend
-   Axios for requesting backend
-   Base Web framwork for UI

## Backend

-   Flask REST backend
-   RIOT API to gather user information (current match details) : https://developer.riotgames.com/apis#
-   Periodic scheduling : https://github.com/viniciuschiele/flask-apscheduler (for periodic rebuilding of model)
-   SCIKIT LEARN for building the model
-   pickle for storing / restoring models

## Datastorage

-   Since we only insert and bulk read from our database, we can simply use csv format (Pandas)
-   this method is much more simple, as our database becomes a text file

## Deployment

-   Dockerize
-   todo

# Credits

1. Zekic-Susac, Marijana & Pfeifer, Sanja & Sarlija, Natasa. (2014). A Comparison of Machine Learning Methods in a High-Dimensional Classification Problem. Business Systems Research Journal. 5. 10.2478/bsrj-2014-0021. https://www.researchgate.net/publication/276530335_A_Comparison_of_Machine_Learning_Methods_in_a_High-Dimensional_Classification_Problem
    - this paper greatly influenced the Neural Network chosen
