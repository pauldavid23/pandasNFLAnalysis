import pandas as pd

df = pd.read_csv("team_stats_2003_2023.csv")

mean=df.groupby('team')['wins'].sum().sort_values(ascending=False)
print(mean)


