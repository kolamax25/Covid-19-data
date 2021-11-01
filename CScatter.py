import pandas as pd
import plotly.express as px

convert = pd.read_csv("coviD.csv")

fig = px.scatter(convert, x = "date", y = "cases", color = "country")
fig.show()