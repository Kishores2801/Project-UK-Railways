# Import 
import os
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import folium


# Load the dataset
data = pd.read_csv("https://raw.githubusercontent.com/Kishores2801/Project-UK-Railways/main/Data/Uk-Train%20Data.csv")
weekday_order = ["All", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]



# Initialize the Dash app
app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True



app.layout = html.Div(className='main-container', children=[
    dcc.Location(id='url', refresh=False),
    html.Nav(className='nav-bar', children=[
        html.H1("UK Train Traveling Web Dashboard", style={"text-align": "center","font-size": "30px"}),
        html.Ul([
            html.Li(dcc.Link('Overall', href='/'), style={"font-size": "18px", "margin-bottom":"18px"}),
            html.Li(dcc.Link('Stations', href='/Station'), style={"font-size": "18px", "margin-bottom":"18px"}),
            html.Li(dcc.Link('Prediction', href='/Prediction'), style={"font-size": "18px", "margin-bottom":"18px"}),]),
            
        
    ], style={"background-color": "#990011","font-family": "Roboto, sans-serif", "color": "white",
              "text-align": "center", "margin-bottom": "10px", "width": "98%", "height":"80%"}),
    html.Div(id='page-content', style={'flex': '1'})

])


overall_layout = html.Div(
    className="Overall",
    children = [
        html.P(
            "This interactive web dashboard is designed to explore traveler behavior and operational performance in UK Railways.",
            style={"font-family": "Roboto, sans-serif", "font-size": "20px", "margin-bottom": "20px", "margin-left": "20px"}
        ),
        html.Br(),

        html.Div(
            className="overall-output-container-1",
            style={"padding": "20px", "width": "95%", "height": "600px", "overflow": "hidden", "margin-top": "20px"},
            children=[
                html.Div(
                    className="overall-Map-section",
                    style={"display": "flex", "justify-content": "space-between", "height": "500px", "overflow": "hidden"},
                    children=[
                        html.Div(
                            className="overall-Map",
                            id='overall-map-id',
                            children=[],
                            style={"height": "100%", "width": "65%", "margin": "0 10px 0 30px"}
                        ),
                        html.Div(
                            className="overall-trip-info",
                            id='overall-trip-id',
                            children=[],
                            style={"width": "40%", "padding": "5px", "display": "flex", "flex-direction": "column", "height": "100%", "line-height":"8px", "margin-left":"20px"}
                        ),
                    ]
                ),
                html.P(
                    id="overall-text-id-1",
                    className="text-class-1",
                    children="",
                    style={"font-size": "16px", "padding": "15px", "margin-left": "30px"}
                ),
            ]
        ),

    ]
)


station_layout = html.Div(
    className="station",
    children=[
        html.P(
            "This interactive web dashboard is designed to explore traveler behavior and operational performance in UK Railways.",
            style={"font-family": "Roboto, sans-serif", "font-size": "20px", "margin-bottom": "20px"}
        ),
        html.Br(),
        html.Div(
            className="dropdowns",
            style={"display": "flex", "justify-content": "space-between", "width": "100%", "margin-bottom": "20px"},
            children=[
                html.Div(
                    className="dropdown",
                    style={"width": "33%", "flex": 1, "margin-right": "20px"},
                    children=[
                        html.H3(
                            "Select the Departure Station:",
                            style={"font-family": "Roboto, sans-serif", "font-size": "18px", "text-align": "left", "margin": "0 0 5px 0"}
                        ),
                        dcc.Dropdown(
                            id="dept-dropdown",
                            style={"width": "100%"},
                            options=[{'label': station, 'value': station} for station in data["Departure Station"].unique()],
                            value=data["Departure Station"].unique()[0]  # Set a default value
                        ),
                    ]
                ),
                html.Div(
                    style={"width": "33%", "flex": 1, "margin-right": "20px"},
                    children=[
                        html.H3(
                            "Select the Arrival Station:",
                            style={"font-family": "Roboto, sans-serif", "font-size": "18px", "text-align": "left", "margin": "0 0 5px 0"}
                        ),
                        dcc.Dropdown(
                            id="arr-dropdown",
                            style={"width": "100%"},
                            options=[]
                        ),
                    ]
                ),
                html.Div(
                    style={"width": "33%", "flex": 1, "margin-right": "20px"},
                    children=[
                        html.H3(
                            "Select the day:",
                            style={"font-family": "Roboto, sans-serif", "font-size": "18px", "text-align": "left", "margin": "0 0 5px 0"}
                        ),
                        dcc.Dropdown(
                            id="week-dropdown",
                            style={"width": "100%"},
                            options=[{'label': day, 'value': day} for day in weekday_order],
                            value="All"
                        ),
                    ]
                ),
            ]
        ),
        html.Br(),
        
        html.Div(
            className="output-container-1",
            style={"padding": "20px", "width": "95%", "height": "600px", "overflow": "hidden", "margin-top": "20px"},
            children=[
                html.Div(
                    className="Map-section",
                    style={"display": "flex", "justify-content": "space-between", "height": "500px", "overflow": "hidden"},
                    children=[
                        html.Div(
                            className="Map",
                            id='map-id',
                            children=[],
                            style={"height": "100%", "width": "65%", "margin": "0 10px 0 30px"}
                        ),
                        html.Div(
                            className="trip-info",
                            id='trip-id',
                            children=[],
                            style={"width": "40%", "padding": "5px", "display": "flex", "flex-direction": "column", "height": "100%", "line-height":"8px", "margin-left":"20px"}
                        ),
                    ]
                ),
                html.P(
                    id="text-id-1",
                    className="text-class-1",
                    children="",
                    style={"font-size": "16px", "padding": "15px", "margin-left": "30px"}
                ),
            ]
        ),
        html.Br(),
        html.Br(),
        html.Div(
            className="output-container-1",
            style={"width": "90%", "height": "550px", "margin-top": "20px", "display": "flex", "align-items": "stretch", "justify-content": "space-between", "margin-left": "20px", "padding": "10px"},
            children=[
                html.Div(
                    className="dash-graph",
                    style={"flex": 1, "text-align": "center", "height": "100%", "margin-right": "4%", "padding-left": "10px"},
                    children=[
                        dcc.Graph(id="line-chart-1"),
                    ]),
                    html.Div(className="dash-graph", 
                             style={"flex": 1, "text-align": "center", "height": "100%", "margin-right": "4%", "padding-left": "10px"}, children=[
                            dcc.Graph(id="line-chart-2"),
                    ]),
                
            ]
        ),

        html.Div(className="output-container-2", 
                 style={"padding": "20px", "width": "90%", "height": "550px", "overflow": "hidden", "margin-top": "10px"}, children=[
            html.Div(className="dash-graph",
                     style={"flex": 1, "text-align": "center", "height": "90%", "margin-right": "4%", "padding-left": "10px"},  children=[
                dcc.Graph(id="bar-chart-1"),
            ]),
        ]),


        html.P(
            className="text-class-2",
            style={'font-size': '18px', "padding": "10px", "margin-left": "20px"},
            children=(
                "This chart depicts the busiest hours at each departure station, showcasing the distribution of departure times. "
                "It reveals a recurring pattern commonly seen in railway stations, with notable spikes in passenger traffic occurring "
                "at approximately 8:00 AM and 8:00 PM. This pattern suggests a consistent 12-hour cycle of activity throughout the day."
            )
        ),

        html.Div(className="output-container-3", style={"padding": "20px", "width": "90%", "height": "550px", "overflow": "hidden", "margin-top": "10px"}, children=[
            html.Div(className="dash-graph", style={"flex": 1, "text-align": "center", "height": "90%", "margin-right": "4%", "padding-left": "10px"}, children=[
                dcc.Graph(id="sb-chart-1"),
            ]),
            html.Div(className="dash-graph", style={"flex": 1, "text-align": "center", "height": "90%", "margin-right": "4%", "padding-left": "10px"}, children=[
                dcc.Graph(id="sb-chart-2"),
            ]),
        ]),

        html.Div(className="output-container-4", style={"padding": "20px", "width": "90%", "height": "550px", "overflow": "hidden", "margin-top": "10px"}, children=[
            html.Div(className="dash-graph", style={"flex": 1, "text-align": "center", "height": "90%", "margin-right": "4%", "padding-left": "10px"}, children=[
                dcc.Graph(id="pie-chart-1"),
            ]),
            html.Div(className="dash-graph", style={"flex": 1, "text-align": "center", "height": "90%", "margin-right": "4%", "padding-left": "10px"}, children=[
                dcc.Graph(id="pie-chart-2"),
            ]),
            html.Div(className="dash-graph", style={"flex": 1, "text-align": "center", "height": "90%", "margin-right": "4%", "padding-left": "10px"}, children=[
                dcc.Graph(id="pie-chart-3"),
            ]),
        ]),
        html.Div(className="output-container-5", style={"padding": "20px", "width": "90%", "height": "550px", "overflow": "hidden", "margin-top": "10px"}, children=[
            html.Div(className="dash-graph", style={"flex": 1, "text-align": "center", "height": "90%", "margin-right": "4%", "padding-left": "10px"}, children=[
                dcc.Graph(id="bar-chart-2"),
            ]),
            html.Div(className="dash-graph", style={"flex": 1, "text-align": "center", "height": "90%", "margin-right": "4%", "padding-left": "10px"},  children=[
                dcc.Graph(id="bar-chart-3"),
            ]),
            html.Div(className="dash-graph", style={"flex": 1, "text-align": "center", "height": "90%", "margin-right": "4%", "padding-left": "10px"}, children=[
                dcc.Graph(id="bar-chart-4"),
            ]),
        ]),
        
    ]
)



prediction_layout = html.Div([
    html.H1("Welcome Prediction Section here we will predict the price of !!")
])


# Callback to update the page content based on the URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/Prediction':
        return prediction_layout
    elif pathname =='/Station':
        return station_layout
    else:
        return overall_layout
    

@app.callback(
    [Output("overall-map-id", "children"),
     Output("overall-trip-id", "children"),
     Output("overall-text-id-1", "children")],
    [Input("dummy-input", "dummy-data")]
)
def update_chart(dummy_data):
    # Assuming data is accessible within the function or defined globally
    # Map Chart
    coordinates = [51.5072, 0.1276]
    site_map = folium.Map(location=coordinates, prefer_canvas=True, zoom_start=5, min_zoom=5, max_zoom=5)
    
    data_filter = data[["Departure Station", "Arrival Destination", "Departure Latitude", "Departure Longitude", "Arrival Latitude", "Arrival Longitude"]].drop_duplicates()

    # Creating a loop to mark all the locations
    for _, row in data_filter.iterrows():
        departure_coords = [row["Departure Latitude"], row["Departure Longitude"]]
        arrival_coords = [row["Arrival Latitude"], row["Arrival Longitude"]]
        
        folium.Marker(departure_coords, popup="Departure").add_to(site_map)
        folium.Marker(arrival_coords, popup="Arrival").add_to(site_map)

        folium.PolyLine(
            locations=[departure_coords, arrival_coords],
            weight=2
        ).add_to(site_map)
        
    map_html = site_map._repr_html_()
    map_html = html.Iframe(srcDoc=map_html, width='100%', height='550px')

    # Trip Info
    no_of_travel = len(data)
    distance = data["Distance"].mean().astype(int)
    average_spend = data["Price"].mean().round(2)
    refunded = data[data["Refund Request"] == "Yes"]["Refund Request"].count()
    on_time = data[data["Journey Status"] == "On Time"]["Journey Status"].count()
    delayed = data[data["Journey Status"] == "Delayed"]["Journey Status"].count()
    cancelled = data[data["Journey Status"] == "Cancelled"]["Journey Status"].count()
    first_class = data[data["Ticket Class"] == "First Class"]["Ticket Class"].count()
    standard = data[data["Ticket Class"] == "Standard"]["Ticket Class"].count()

    info = [
        html.H4("Overall Trip Overview", style={"font-size": "22px", "text-align": "center", "margin-bottom": "10px"}),
        html.P([html.B("Number of Travels: "), str(no_of_travel)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px"}),
        html.P([html.B("Distance Covered: "), f"{distance} km"], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px"}),
        html.P([html.B("Average Spend: "), f"£{average_spend}"], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px"}),
        html.P([html.B("Refund Requests: "), str(refunded)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px"}),
        html.P([html.B("On Time Journeys: "), str(on_time)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px"}),
        html.P([html.B("Delayed Journeys: "), str(delayed)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px"}),
        html.P([html.B("Cancelled Journeys: "), str(cancelled)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px"}),
        html.P([html.B("First Class Tickets: "), str(first_class)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px"}),
        html.P([html.B("Standard Tickets: "), str(standard)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px"})
    ]

    text_info = f"These lines represent all unique combinations of rail routes for Main Stations in UK Railways"

    return map_html, info, text_info



# Callback to update arrival stations based on the selected departure station
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

# Create a callback to update map data
@app.callback(
    [Output("map-id", "children"),
     Output("trip-id", "children"),
     Output("text-id-1", "children")],
    [Input("dept-dropdown", "value"),
     Input("arr-dropdown", "value"),
     Input("week-dropdown", "value")]
)
def update_map_and_info(dep_location, arr_location, week_day):
    if not dep_location or not arr_location:
        return "", [], "Please select both departure and arrival stations."

    data_filter = data[(data["Departure Station"] == dep_location) & (data["Arrival Destination"] == arr_location)]
    if data_filter.empty:
        return "", [], "No data available for the selected route."

    first_row = data_filter.iloc[0]
    departure_coords = [first_row["Departure Latitude"], first_row["Departure Longitude"]]
    arrival_coords = [first_row["Arrival Latitude"], first_row["Arrival Longitude"]]
    travel_distance = first_row["Distance"].astype(int)
    coordinates = [51.5072, 0.1276]

    site_map = folium.Map(location=coordinates, prefer_canvas=True, zoom_start=5, min_zoom=5, max_zoom=5)
    folium.Marker(departure_coords, popup=dep_location, icon=folium.Icon(color='red')).add_to(site_map)
    folium.Marker(arrival_coords, popup=arr_location, icon=folium.Icon(color='green')).add_to(site_map)
    folium.PolyLine(locations=[departure_coords, arrival_coords], popup=f"Estimated Distance Covered: {travel_distance} km", weight=3).add_to(site_map)
    map_html = site_map._repr_html_()
    map_html = html.Iframe(srcDoc=map_html, width='100%', height='550px')

    if week_day == "All":
        data_filter = data[(data["Departure Station"] == dep_location) & (data["Arrival Destination"] == arr_location)]
    else:
        data_filter = data[(data["Departure Station"] == dep_location) & (data["Arrival Destination"] == arr_location) & (data["Day of week"] == week_day)]

    no_of_travel = len(data_filter)
    distance = data_filter["Distance"].mean().astype(int)
    average_spend = data_filter["Price"].mean().round(2)
    refunded = data_filter[data_filter["Refund Request"] == "Yes"]["Refund Request"].count()
    on_time = data_filter[data_filter["Journey Status"] == "On Time"]["Journey Status"].count()
    delayed = data_filter[data_filter["Journey Status"] == "Delayed"]["Journey Status"].count()
    cancelled = data_filter[data_filter["Journey Status"] == "Cancelled"]["Journey Status"].count()
    first_class = data_filter[data_filter["Ticket Class"] == "First Class"]["Ticket Class"].count()
    standard = data_filter[data_filter["Ticket Class"] == "Standard"]["Ticket Class"].count()

    info = [
    html.H4("Trip Overview", style={"font-size": "22px", "text-align": "center", "margin-bottom": "10px"}),
    html.P([html.B("Departure Destination: "), str(dep_location)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px"}),
    html.P([html.B("Arrival Destination: "), str(arr_location)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px"}),
    html.P([html.B("Number of Travels: "), str(no_of_travel)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px"}),
    html.P([html.B("Distance Covered: "), f"{distance} km"], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px"}),
    html.P([html.B("Average Spend: "), f"£{average_spend}"], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px"}),
    html.P([html.B("Refund Requests: "), str(refunded)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px"}),
    html.P([html.B("On Time Journeys: "), str(on_time)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px"}),
    html.P([html.B("Delayed Journeys: "), str(delayed)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px"}),
    html.P([html.B("Cancelled Journeys: "), str(cancelled)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px"}),
    html.P([html.B("First Class Tickets: "), str(first_class)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px"}),
    html.P([html.B("Standard Tickets: "), str(standard)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px"})
]


    text_info = f"The markers on the map identify stations by their latitude and longitude coordinates. The red marker denotes the departure station, while the green marker signifies the arrival destination. The line connecting these markers represents a potential route, with the distance estimated based on the approximate distance between two points on Earth's surface. For instance, the estimated distance between {dep_location} and {arr_location} is {distance} km."

    return map_html, info, text_info

# Callback to update charts
@app.callback(
    [Output("line-chart-1", "figure"),
     Output("line-chart-2", "figure")],
    [Input("dept-dropdown", "value"),
     Input("arr-dropdown", "value")]
)
def update_charts(dep_location, arr_location):
    if not dep_location or not arr_location:
        return {}, {}, "Please select both departure and arrival stations."

    data_filter = data[(data["Departure Station"] == dep_location) & (data["Arrival Destination"] == arr_location)]
    if data_filter.empty:
        return {}, {}, "No data available for the selected route."

    # Chart 1
    grouped_data_price = data_filter.groupby('c')['Price'].sum().cumsum().reset_index()
    fig1 = px.line(grouped_data_price, x="Date of Purchase", y="Price", title=f"<b>Ticket Price Paid for <br>{dep_location} to {arr_location}</b>")
    fig1.update_yaxes(range=[0, max(grouped_data_price['Price']) * 1.2])
    fig1.update_layout(
        xaxis_title="Date of Purchase",
        yaxis_title="Ticket Price Paid in pounds (£)",
        title_x=0.5,
        title_y=0.90,
        title_font_size=18,
        font_size=14,
        width=750,  # Set the width of the figure
        height=600,  # Set the height of the figure
        paper_bgcolor = 'rgba(0,0,0,0)',
        plot_bgcolor = 'rgba(0,0,0,0)',
    )
    

    # Chart 2
    data_filter = data_filter.sort_values(by="Date of Purchase")
    grouped_data_cumsum = data_filter.groupby('Date of Purchase')[['Actual Price', 'Discount']].sum().cumsum().reset_index()
    grouped_data_cumsum = grouped_data_cumsum.reset_index()

    fig2 = px.line(grouped_data_cumsum, x="Date of Purchase", y=["Actual Price", "Discount"],
                   title=f"<b>Actual Ticket Price vs Discount for <br>{dep_location} to {arr_location}</b>",
                   labels={"value": "Amount in pounds (£)", "variable": "Metrics", "Date of Purchase": "Date"})
    fig2.update_yaxes(range=[0, max(grouped_data_cumsum['Actual Price']) * 1.2])
    fig2.update_layout(
        xaxis_title="Date of Purchase",
        title_x=0.5,
        title_y=0.90,
        title_font_size=18,
        font_size=14,
        width=750,  # Set the width of the figure
        height=600,  # Set the height of the figure
        paper_bgcolor = 'rgba(0,0,0,0)',
        plot_bgcolor = 'rgba(0,0,0,0)',
        
    )
    return fig1, fig2




# Third Call back
@app.callback(
    [Output("bar-chart-1", "figure"),],
    [Input("dept-dropdown", "value"),
     Input("week-dropdown", "value")]
)


def bar_graph(dep_location, weekday):
    if weekday == "All":
        data_filter = data[(data["Departure Station"] == dep_location)]
    else:
        data_filter = data[(data["Departure Station"] == dep_location) & (data["Day of week"] == weekday)]
    
    bar_group = data_filter.groupby("Day of week")["Hour of Departure"].value_counts().reset_index()
    fig3 = px.bar(bar_group, x="Hour of Departure", y="count", title=f"<b>Active Hours in {dep_location} station</b>")
    fig3.update_xaxes(range=[0, 23],
                      tickmode='linear',  # Set tick mode to linear
                      tick0=0,  # Start ticks from 0
                      dtick=1,  # Set the step size between ticks to 1
                      showticklabels=True)
    
    fig3.update_layout(
        xaxis_title="Hour of Departure",
        yaxis_title= "Count of Travelers",
        title_x=0.55,
        title_y=0.98,
        title_font_size=18,
        font_size=14,
        width=1750,
        height=600,
        paper_bgcolor = 'rgba(0,0,0,0)',
        plot_bgcolor = 'rgba(0,0,0,0)',
        margin=dict(
        l=80,  # Left margin
        r=80,  # Right margin
        t=80,  # Top margin
        b=80,  # Bottom margin
        pad=10  # Padding between plot area and axis lines
        )
    )

    return [fig3]


# Fourth Call Back
@app.callback(
    [Output("sb-chart-1", "figure"),
     Output("sb-chart-2", "figure")],
    [Input("dept-dropdown", "value"),
     Input("arr-dropdown", "value"),
     Input("week-dropdown", "value")]
)

def graphs(dep_location, arr_location,weekday):
    if weekday == "All":
        data_filter = data[(data["Departure Station"] == dep_location) & (data["Arrival Destination"] == arr_location)]
    else:
        data_filter = data[(data["Departure Station"] == dep_location) & (data["Arrival Destination"] == arr_location) & (data["Day of week"] == weekday)]

    # First Chart Create a SunBurst Chart
    sb = data_filter.groupby(["Purchase Type", "Payment Method", "Journey Status"])["Journey Status"].value_counts().reset_index()
    fig4 = px.sunburst(sb, path=["Purchase Type", "Payment Method", "Journey Status"], values="count", color="Journey Status", title="<b>Distribution of Purchases by Type, Payment Method, and Journey Status</b>")
    fig4.update_layout(
        title_x=0.55,
        title_y=0.98,
        title_font_size=16,
        width=600,
        height=600,
        paper_bgcolor = 'rgba(0,0,0,0)',
        plot_bgcolor = 'rgba(0,0,0,0)',

    )


    # Second Chart Create a SunBurst Chart
    sb = data_filter.groupby(["Hour of Departure", "Journey Status"])["Journey Status"].value_counts().reset_index()
    fig5 = px.sunburst(sb, path=["Hour of Departure", "Journey Status"], values="count", color="Journey Status", title="<b>Distribution Hours by Journey Status</b>")
    fig5.update_layout(
        title_x=0.55,
        title_y=0.98,
        title_font_size=16,
        width=600,
        height=600,
        paper_bgcolor = 'rgba(0,0,0,0)',
        plot_bgcolor = 'rgba(0,0,0,0)',
    )

    # Third Chart to Horizontal Bar Chart
    return fig4, fig5
    

# fifth  Call Back

@app.callback(
    [Output("pie-chart-1", "figure"),
     Output("pie-chart-2", "figure"),
     Output("pie-chart-3", "figure"),
     Output("bar-chart-2", "figure"),
     Output("bar-chart-3", "figure"),
     Output("bar-chart-4", "figure"),
     ],
    [Input("dept-dropdown", "value"),
     Input("arr-dropdown", "value"),
     Input("week-dropdown", "value")]
)
def charts(dep_location, arr_location, weekday):
    if weekday == "All":
        data_filter = data[(data["Departure Station"] == dep_location) & (data["Arrival Destination"] == arr_location)]
    else:
        data_filter = data[(data["Departure Station"] == dep_location) & (data["Arrival Destination"] == arr_location) & (data["Day of week"] == weekday)]

    # First Chart: Journey Status Pie Chart
    pie_1 = data_filter.groupby("Journey Status")["Journey Status"].value_counts().reset_index()
    fig5 = px.pie(pie_1, values='count', names="Journey Status", title=f"<b>               Journey Status for <br>{dep_location} to {arr_location}</b>", hole=0.35)
    fig5.update_layout(
        title_x=0.15,
        title_y=0.95,
        title_font_size=16,
        width=600,
        height=600,
        paper_bgcolor = 'rgba(0,0,0,0)',
        plot_bgcolor = 'rgba(0,0,0,0)',
    )
    # Check if the pie chart is empty
    if pie_1.empty:
        fig5.add_annotation(
            text="No Valid data points available",
            showarrow=False,
            font=dict(size=18),
            x=0.55,
            y=0.5)

    # Second Chart: Reason for Delay Pie Chart
    pie_2 = data_filter.groupby("Reason for Delay")["Reason for Delay"].value_counts().reset_index()
    fig6 = px.pie(pie_2, values='count', names="Reason for Delay", title=f"<b>              Reason for delay from <br>{dep_location} to {arr_location}</b>", hole=0.35)
    fig6.update_layout(
            title_x=0.15,
            title_y=0.95,
            title_font_size=16,
            width=600,
            height=600,
            paper_bgcolor = 'rgba(0,0,0,0)',
            plot_bgcolor = 'rgba(0,0,0,0)',
           
        )
    
    # Check if the pie chart is empty
    if pie_2.empty:
        fig6.add_annotation(
            text="No Valid data points available",
            showarrow=False,
            font=dict(size=16),
            x=0.55,
            y=0.5)
    

    # Third Chart: Journey Status Pie Chart (Again?)
    pie_3 = data_filter.groupby("Ticket Class")["Ticket Class"].value_counts().reset_index()
    fig7 = px.pie(pie_3, values='count', names="Ticket Class", title=f"<b>                Ticket Class from <br>{dep_location} to {arr_location}</b>", hole=0.35)
    fig7.update_layout(
        title_x=0.15,
        title_y=0.95,
        title_font_size=16,
        width=600,
        height=600,
        paper_bgcolor = 'rgba(0,0,0,0)',
        plot_bgcolor = 'rgba(0,0,0,0)',
    )

    # Check if the pie chart is empty
    if pie_3.empty:
        fig7.add_annotation(
            text="No data available",
            showarrow=False,
            font=dict(size=16),
            x=0.55,
            y=0.5)
        


    # Bar Graph - 1
    bar_1 = data_filter.groupby("Payment Method")["Payment Method"].value_counts().reset_index()
    fig8 = px.bar(bar_1, x="Payment Method", y="count", title=f"<b>Payment Method for <br>{dep_location} to {arr_location}</b></b>")
    fig8.update_layout(
        title_x=0.15,
        title_y=0.95,
        title_font_size=16,
        width=600,
        height=600,
        paper_bgcolor = 'rgba(0,0,0,0)',
        plot_bgcolor = 'rgba(0,0,0,0)',
    )

    if bar_1.empty:
        fig8.add_annotation(
            text="No data available",
            showarrow=False,
            font=dict(size=16),
            x=0.55,
            y=0.5)
        
    # Bar Graph - 2
    bar_2 = data_filter.groupby("Ticket Type")["Ticket Type"].value_counts().reset_index()
    fig9 = px.bar(bar_2, x="Ticket Type", y="count", title=f"<b>Ticket Type for <br>{dep_location} to {arr_location}</b></b>")
    fig9.update_layout(
        title_x=0.15,
        title_y=0.95,
        title_font_size=16,
        width=600,
        height=600,
        paper_bgcolor = 'rgba(0,0,0,0)',
        plot_bgcolor = 'rgba(0,0,0,0)',
    )

    if bar_2.empty:
        fig9.add_annotation(
            text="No data available",
            showarrow=False,
            font=dict(size=16),
            x=0.55,
            y=0.5)
        
    bar_3 = data_filter.groupby("Refund Request")["Refund Request"].value_counts().reset_index()
    fig10 = px.bar(bar_3, x="Refund Request", y="count", title=f"<b>Refund Request for <br>{dep_location} to {arr_location}</b></b>")
    fig10.update_layout(
        title_x=0.15,
        title_y=0.95,
        title_font_size=16,
        width=600,
        height=600,
        paper_bgcolor = 'rgba(0,0,0,0)',
        plot_bgcolor = 'rgba(0,0,0,0)',
    )

    if bar_3.empty:
        fig10.add_annotation(
            text="No data available",
            showarrow=False,
            font=dict(size=16),
            x=0.55,
            y=0.5)

 
    return fig5, fig7, fig6, fig8, fig9, fig10



# Run the app 
if __name__ == "__main__":
    app.run(debug=True)