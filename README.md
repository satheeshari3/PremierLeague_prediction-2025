🏆 Premier League 2025 Winner Prediction — Project Notes

This notebook predicts the 2025 Premier League winner using team performance statistics and a simple machine learning model. The goal is not to be 100% accurate (football is unpredictable), but to build a clean, end-to-end ML workflow that uses real-world data and produces interpretable results.

🔥 What This Notebook Does

Loads Premier League team stats (goals, xG, passing, defence, etc.)

Cleans and preprocesses the dataset

Engineers features like attack strength, defense strength, xG difference, etc.

Trains a machine learning model to estimate each team's overall performance

Ranks all 20 PL teams

Predicts the most likely 2025 Premier League winner

Displays win probabilities in a simple output table

📊 Dataset Details

The dataset contains team-level season performance metrics such as:

Goals For / Goals Against

Expected Goals For (xG) / Expected Goals Against (xGA)

Goal Difference

Possession %

Shots & Shots on Target

Pass Completion %

Progressive Passes

Points per 90 minutes

The file for this project:
premier_league_2025_team_stats.csv

You can update it anytime to improve predictions.

🤖 Model Used

The model used in the notebook is:

RandomForestClassifier

Why?

Simple

Performs well on structured numeric data

Handles non-linear relationships

Robust to noise

Provides feature importance

The model outputs a probability for each team, representing their likelihood of winning the league.
