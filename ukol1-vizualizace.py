import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

source_file = "vystup.txt"

dataset = pd.read_csv(source_file)

fig = px.line(
    dataset,
    x="date_time",
    y="temperature",
    color="elevation",
    title="Mountains temperature over time in Q1 2026",
)
fig.show()