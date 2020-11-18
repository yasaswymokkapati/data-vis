import pandas as pd
import plotly.express as px

bc = pd.read_csv('data.csv')

fig = px.bar(bc, x = 'Country', y = "InternetUsers")

fig.show()