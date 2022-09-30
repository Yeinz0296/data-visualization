import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from datetime import date
from dash import Dash, html, dcc, Output, Input
from dash_bootstrap_templates import load_figure_template

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY, dbc_css])

load_figure_template('darkly')

dataframe = pd.read_csv("dataset_september.csv")
timestamp = dataframe['Timestamp']
dataframe['Dates'] = pd.to_datetime(timestamp).dt.date 
dataframe['Time'] = pd.to_datetime(timestamp).dt.time

All = ['Temperature','Humidity']

app.layout = html.Div(
    children=[
        html.H1(children='Dashboard',className="m-2"),

        html.Div(children='''
            Python Data Visualization
        ''',
        className="m-2"),

        html.Div(children=[
        dcc.DatePickerRange(
            id='my-date-picker-range',
            start_date=date(2022,9,1),
            end_date=date(2022,9,2),
            min_date_allowed=dataframe['Timestamp'].min(),
            max_date_allowed=dataframe['Timestamp'].max(),
            className="m-2",
        ),

        dcc.Dropdown(
            options=['Temperature', 'Humidity'],
            id='dropdown',
            multi=True,
            className="m-2",
        ),

        dcc.Graph(
            id='example-graph',
            className="m-2",
        ),],
        id='master_plot'),
    
    ],

    className="dbc", 
)

@app.callback(
    Output('example-graph','figure'),
    Input("my-date-picker-range", "start_date"),
    Input("my-date-picker-range", "end_date"),
    Input("dropdown", "value"),)
def update_plot(tarikh_start, tarikh_habis,pilihan):
    start_date_object = date.fromisoformat(tarikh_start)
    end_date_object = date.fromisoformat(tarikh_habis)
    date_specify = (dataframe['Dates']>=start_date_object) & (dataframe['Dates']<=end_date_object)
    fig = px.line(dataframe.loc[date_specify], x="Timestamp", y=pilihan, template="darkly")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)