from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd
from datetime import date

app = Dash(__name__)

dataframe = pd.read_csv("dataset_september.csv")
timestamp = dataframe['Timestamp']
dataframe['Dates'] = pd.to_datetime(timestamp).dt.date 
dataframe['Time'] = pd.to_datetime(timestamp).dt.time

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    
    dcc.DatePickerRange(
        id='my-date-picker-range',
        start_date=date(2022,9,1),
        end_date=date(2022,9,30),
        min_date_allowed=dataframe['Timestamp'].min(),
        max_date_allowed=dataframe['Timestamp'].max()
    ),

    dcc.Dropdown(
        options=['Temperature', 'Humidity'],
        value='Temperature',
        id='dropdown',
        multi=True
    ),

    dcc.Graph(
        id='example-graph',
    )
])

@app.callback(
    Output('example-graph','figure'),
    Input("my-date-picker-range", "start_date"),
    Input("my-date-picker-range", "end_date"),
    Input("dropdown", "value"),)
def update_output(tarikh_start, tarikh_habis,pilihan):
    start_date_object = date.fromisoformat(tarikh_start)
    end_date_object = date.fromisoformat(tarikh_habis)
    date_specify = (dataframe['Dates']>=start_date_object) & (dataframe['Dates']<=end_date_object)
    fig = px.line(dataframe.loc[date_specify], x="Timestamp", y=pilihan)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)