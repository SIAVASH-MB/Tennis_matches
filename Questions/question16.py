import pandas as pd

# Load data
df_home = pd.read_csv("MatchHomeTeamInfo.csv")
df_away = pd.read_csv("MatchAwayTeamInfo.csv")
df_match = pd.read_csv("MatchEventInfo.csv")

# Label teams
df_home = df_home[['match_id', 'player_id', 'current_rank']].copy()
df_home['team'] = 'home'

df_away = df_away[['match_id', 'player_id', 'current_rank']].copy()
df_away['team'] = 'away'

# Combine players
players = pd.concat([df_home, df_away], ignore_index=True)

# Identify top 10 players (lowest ranks)
top10_players = (
    players.dropna(subset=['current_rank'])
           .drop_duplicates('player_id')
           .sort_values('current_rank')
           .head(10)['player_id']
           .tolist()
)

# Merge to create full match info with both players
df_home.columns = ['match_id', 'home_id', 'home_rank', 'team']
df_away.columns = ['match_id', 'away_id', 'away_rank', 'team']
df_matches = pd.merge(df_home[['match_id', 'home_id', 'home_rank']], 
                      df_away[['match_id', 'away_id', 'away_rank']], 
                      on='match_id')
df_matches = pd.merge(df_matches, df_match[['match_id', 'winner_code']], on='match_id')

# Filter matches where only one player is in top 10
def opponent_is_top10(row):
    h_top10 = row['home_id'] in top10_players
    a_top10 = row['away_id'] in top10_players
    return (h_top10 and not a_top10) or (not h_top10 and a_top10)

df_matches = df_matches[df_matches.apply(opponent_is_top10, axis=1)]

# Determine which player is non-top10 and whether they won
def label_row(row):
    if row['home_id'] in top10_players:
        return pd.Series({'non_top10_id': row['away_id'], 'won': row['winner_code'] == 2})
    else:
        return pd.Series({'non_top10_id': row['home_id'], 'won': row['winner_code'] == 1})

df_matches[['non_top10_id', 'won']] = df_matches.apply(label_row, axis=1)

# Group by non-top10 player
summary = df_matches.groupby('non_top10_id').agg(
    matches_vs_top10=('won', 'count'),
    wins_vs_top10=('won', 'sum')
).reset_index()
summary['win_percentage'] = summary['wins_vs_top10'] / summary['matches_vs_top10']

# Find top performer
top_vs_top10 = summary.sort_values('win_percentage', ascending=False).head(1)

print("Player with highest win % vs top 10 opponents:")
print(top_vs_top10)