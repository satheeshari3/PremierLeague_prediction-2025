import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def load_data(path):
    print("🔹 Loading team stats...")
    df = pd.read_csv(https://fbref.com/en/comps/9/Premier-League-Stats)
    print("Done. Columns found:")
    print(df.columns)
    return df

def prepare_data(df):
    # Choose useful features
    feature_cols = [
        'Poss',           # possession %
        'Gls',            # goals
        'Ast',            # assists
        'xG',             # expected goals
        'xGA',            # expected goals against
        'PrgP',           # progressive passes
        '1/3',            # passes into final third
        'PPA',            # passes into penalty area
        'CrsPA',          # crosses into penalty area
        'Sh',             # total shots
        'SoT',            # shots on target
    ]

    # Keep only available columns
    feature_cols = [c for c in feature_cols if c in df.columns]

    X = df[feature_cols]
    y = df['Points']  # YOU must add this column manually (last season's points)

    return X, y, feature_cols

def train_model(X, y):
    print("🔹 Training model...")
    model = RandomForestRegressor(n_estimators=400, random_state=42)
    model.fit(X, y)
    print("Model training completed.")
    return model

def predict_points(model, df, features):
    X_pred = df[features]
    df["PredictedPoints"] = model.predict(X_pred)
    return df

def main():
    data_path = "premier_league_2025_team_stats.csv"  # <-- YOU SAVE FBREF table AS THIS CSV
    df = load_data(data_path)

    X, y, features = prepare_data(df)
    model = train_model(X, y)

    result = predict_points(model, df, features)
    result = result.sort_values(by="PredictedPoints", ascending=False)

    print("\n🏆 **Predicted Premier League Winner**:")
    print(result.iloc[0]["Squad"], " → ", round(result.iloc[0]["PredictedPoints"], 2), "points")

    print("\n📊 **Full Predicted Table**:")
    print(result[["Squad", "PredictedPoints"]])

if __name__ == "__main__":
    main()

