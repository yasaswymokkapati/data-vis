import pandas as pd
import plotly.express as px

sf = pd.read_csv('data.csv')

fig = px.scatter_3d(sf, x = 'Population', y = "Per capita", size = "Percentage", color = 'Country')

fig.show()