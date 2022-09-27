from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd
from datetime import date

app = Dash(__name__)

dataframe = pd.read_csv("dataset_september.csv")
timestamp = dataframe['Timestamp']
dataframe['Dates'] = pd.to_datetime(timestamp).dt.date 
dataframe['Time'] = pd.to_datetime(timestamp).dt.time
date_specify = dataframe[dataframe['Dates']==date(2022,9,30)]

fig = px.line(date_specify, x="Timestamp", y="Temperature")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig,
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)