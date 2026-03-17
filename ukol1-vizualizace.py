import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

source_file = "vystup.txt"

dataset = pd.read_csv(source_file)

dataset['date_time'] = pd.to_datetime(dataset['date_time'])
dataset['month'] = dataset['date_time'].dt.month

fig = px.line(
    dataset,
    x="date_time",
    y="temperature",
    color="elevation",
    title="Mountains temperature over time in Q1 2026",
)
fig.show()


plt.figure(figsize=(8, 6))
glue = dataset.pivot_table(index="elevation", columns="month", values="temperature", aggfunc="mean")
sns.heatmap(glue, annot=True, cmap="coolwarm")
plt.title("Mountains temperature over time in Q1 2026")
#plt.show()


plt.figure(figsize=(8, 6))
sns.scatterplot(data=dataset, x="date_time", y="temperature", hue="elevation", palette="Spectral")
plt.title("Mountains temperature over time in Q1 2026")
plt.show()