# LoLgenius

Will you win your LoL match? \
LoLgenius can tell you using machine learning!

# Get Started

-   `cd frontend; npm i; npm build; cd ..`
-   `pip install -r requirements; python -u "app.py"`

# Dataset Gathering Method

-   Dataset is gathered through the RIOT GAMES API
-   MMR is gathered through 3rd party whatismymmr API

1. Starting with an initial summoner, we insert their most recent game into our dataset
2. We then recursively do the same for the lowest and highest mmr players within the game from step 1.
3. We give some sort of max depth to avoid overflow
4. As a result, we get a dataset with diverse ranks, modes, and champions.

# Data Features

-   <s>10 features for each champion played</s>
    -   (lack of data, NN has hard time learning all the champion combinations, leading to sub 50% prediction rate)
-   10 features for each players mmr depending on the game mode
-   10 features for each players tilt score (based on previous winrate for the day)
-   1 feature for result of match (W/L)
-   1 feature for game mode

# Application Archetecture

## Frontend

-   A simple React frontend
-   Axios for requesting backend
-   Base Web framwork for UI
-   served over flask

## Backend

-   Flask REST backend
-   RIOT API to gather user information (current match details) : https://developer.riotgames.com/apis#
-   SCIKIT LEARN for building the NN model
-   pickle for storing / restoring models

## Datastorage

-   Since we only insert and bulk read from our database, we can simply use csv format (Pandas)
-   this method is much more simple, as our database becomes a text file

## Deployment

-   use `cmd`
-   `python -m pipenv install -r requirements.txt` or `python -m pipenv shell` create pipenv
-   `cd frontend; npm i; npm run build; cd ..`
-   make sure frontend build is up to date commit changes and push
-   `git push heroku main` push current branch (main) to heroku

# TODO

-   [x] Frontend interface
-   [x] backend rest api
-   [x] data gathering
-   [x] NN Model
-   [ ] save previous ran models
-   [x] HTTPS
-   [x] deploy

# Credits

1. Zekic-Susac, Marijana & Pfeifer, Sanja & Sarlija, Natasa. (2014). A Comparison of Machine Learning Methods in a High-Dimensional Classification Problem. Business Systems Research Journal. 5. 10.2478/bsrj-2014-0021. https://www.researchgate.net/publication/276530335_A_Comparison_of_Machine_Learning_Methods_in_a_High-Dimensional_Classification_Problem

    - this paper greatly influenced the Neural Network chosen

2. https://pbpython.com/categorical-encoding.html
3. https://www.pluralsight.com/guides/machine-learning-neural-networks-scikit-learn
