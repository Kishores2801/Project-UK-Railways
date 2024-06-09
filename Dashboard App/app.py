# Import necessary libraries
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from flask import Flask
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import folium
import os
# Create a Flask server
server = Flask(__name__)

# Load data
data = pd.read_csv("D:/My Learning/My Projects/Project UK Railways/Dashboard App/Data/Uk-Train Data.csv")

# Create a Dash app
app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Import layout and callbacks from other files
from overall import layout as overall_layout, register_callbacks as register_overall_callbacks
from station import layout as station_layout , register_callbacks as register_station_callbacks
# from prediction import layout as prediction_layout  #, register_callbacks as register_prediction_callbacks
from observation import layout as observation_layout


# Define the app layout
app.layout = html.Div(className='main-container', children=[
    dcc.Location(id='url', refresh=False),
    dcc.Store(id='data-store', data=data.to_dict('records')),  # Store data in dcc.Store
    html.Nav(className='nav-bar', children=[
        html.H1("UK Train Traveling Web Dashboard", style={"text-align": "center","font-size": "40px","padding":"10px"}),
        html.Ul([
            html.Li(dcc.Link('Overall', href='/', className='nav-link', style={"font-size": "20px", "margin-bottom":"15px", "display": "inline-block", "color": "white", "text-decoration": "none", "font-weight":500})),
            html.Li(dcc.Link('Stations', href='/station', className='nav-link', style={"font-size": "20px", "margin-bottom":"15px", "display": "inline-block", "margin-left":"10px", "color": "white", "text-decoration": "none", "font-weight":200})),
            # html.Li(dcc.Link('Prediction', href='/prediction', className='nav-link', style={"font-size": "20px", "margin-bottom":"15px", "margin-left":"10px", "display": "inline-block", "color": "white", "text-decoration": "none", "font-weight":200})),
            html.Li(dcc.Link('Observation', href='/observation', className='nav-link', style={"font-size": "20px", "margin-bottom":"15px", "margin-left":"10px", "display": "inline-block", "color": "white", "text-decoration": "none", "font-weight":200})),
        ], className='nav', style={'justify-content': 'flex-end',  "margin-right":"20px"})
    ], style={"background-color": "#990011", "text-align": "center", "margin-bottom": "10px", "width": "100%", "height": "80%", "list-style-type": "none", "color": "white"}),
    html.Div([], id='page-content', style={'flex': '1', "padding": 0, "font-family": "Arial, sans-serif", "display": "inline-block", "padding":"30px"})
])

# Define callback to update page content based on URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])






def display_page(pathname):
    if pathname == '/station':
        return station_layout
    # elif pathname == '/prediction':
    #     return prediction_layout
    elif pathname == '/observation':
         return observation_layout
    else:
        return overall_layout
# bringing callback
register_overall_callbacks(app)
register_station_callbacks(app)
@app.callback(
    [Output("arr-dropdown", "options"),
     Output("arr-dropdown", "value")],
    [Input("dept-dropdown", "value")]
    )
    
def set_arrival_options(dep_location):
        data_filter = data[data["Departure Station"] == dep_location]
        arrival_options = data_filter["Arrival Destination"].unique()
        options = [{'label': station, 'value': station} for station in arrival_options]
        default_value = arrival_options[0] if arrival_options.size > 0 else None
        return options, default_value



# Run the app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run_server(debug=False, host="0.0.0.0",port=port)
