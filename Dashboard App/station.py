# station.py
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import folium


weekday_order = ["All", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
data = pd.read_csv("D:/My Learning/My Projects/Project UK Railways/Dashboard App/Data/Uk-Train Data.csv")

hour_labels = {
    0: "12 AM", 1: "1 AM", 2: "2 AM", 3: "3 AM", 4: "4 AM",
    5: "5 AM", 6: "6 AM", 7: "7 AM", 8: "8 AM", 9: "9 AM",
    10: "10 AM", 11: "11 AM", 12: "12 PM", 13: "1 PM", 14: "2 PM",
    15: "3 PM", 16: "4 PM", 17: "5 PM", 18: "6 PM", 19: "7 PM",
    20: "8 PM", 21: "9 PM", 22: "10 PM", 23: "11 PM"
}

layout = html.Div(className="station",children=[
    html.Div(
    className="dropdowns",
    style={"display": "flex", "justify-content": "space-between", "width": "100%", "margin-bottom": "10px"},
    children=[
        html.Div(
            style={"width": "500px", "flex": 1, "margin-right": "10px"},
            children=[
                html.H3(
                    "Select the Departure Station:",
                    style={"font-family": "Roboto, sans-serif", "font-size": "18px", "text-align": "left", "margin": "0 0 5px 0"}
                ),
                dcc.Dropdown(
                    id="dept-dropdown",
                    style={"width": "500px"},
                    options=[{'label': station, 'value': station} for station in data["Departure Station"].unique()],
                    value=data["Departure Station"].unique()[0]  # Set a default value
                ),
            ],
        ),
        html.Div(
            style={"width": "500px", "flex": 1, "margin-right": "10px"},
            children=[
                html.H3(
                    "Select the Arrival Station:",
                    style={"font-family": "Roboto, sans-serif", "font-size": "18px", "text-align": "left", "margin": "0 0 5px 0"}
                ),
                dcc.Dropdown(
                    id="arr-dropdown",
                    style={"width": "500px"},
                    options=[]
                ),
            ]
        ),
        html.Div(
            style={"width": "500px", "flex": 1, "margin-right": "10px"},
            children=[
                html.H3(
                    "Select the Day of the Week:",
                    style={"font-family": "Roboto, sans-serif", "font-size": "18px", "text-align": "left", "margin": "0 0 5px 0"}
                ),
                dcc.Dropdown(
                    id="week-dropdown",
                    style={"width": "500px"},
                    options=[{'label': day, 'value': day} for day in weekday_order],
                    value="All"
                ),
            ]
        ),
    ]
    ),

    html.Br(),



    html.Div(className="station-output-container-1", style={"width": "90%", "height": "500px"},
             children=[
                 html.Div(className="station-map-section", style={"display": "flex", "justify-content": "space-between", "height": "480px",
                           "background-color": "#f8f9fa", "overflow": "hidden"},
                           children=[
                               html.Div(className="station-map",  id="station-map-id", children=[],
                                        style={"height": "480px", "width": "65%", "overflow": "hidden", "border-radius": "20px", "margin-right": "5px" ,"box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"}),
                                html.Div(className="station-trip-info", id='station-trip-info', children=[],
                                         style={"width": "35%", "padding": "20px", "display": "flex","background-color": "#f8f9fa",
                                                "flex-direction": "column", "height": "100%", "line-height": "16px",
                                                "margin-left": "10px", "border-radius": "20px", "box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"})        

                           ]),
                           html.Br(),
                           html.P(id="station-text-id", className="text-class-1", children=""),
            ],
            ),
            html.Br(),   
            html.Br(),              
            html.Div(
            className="station-output-container-1",
            style={"width": "90%", "height": "620px", "margin-top": "20px", "display": "flex", "align-items": "stretch",
                   "justify-content": "space-between", "margin-left": "10px", "padding": "5px"},
            children=[
                html.Div(
                    className="dash-graph",
                    style={"flex": 1, "text-align": "center", "width": "40%","border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "10px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"},
                    children=[
                        dcc.Graph(id="station-line-chart-1"),
                    ]
                ),
                html.Div(
                    className="dash-graph",
                    style={"flex": 1, "text-align": "center", "width": "50%","border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "5px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"},
                    children=[
                        dcc.Graph(id="station-line-chart-2"),
                    ]
                ),
            ]
        ),
        
        html.Div(
            className="station-time-container",
            style={"width": "88%", "height": "620px", "margin-top": "20px", "display": "flex", "align-items": "stretch",
                   "justify-content": "space-between", "margin-left": "20px", "padding": "5px"},
            children=[
                html.Div(className="station-departure-time",  # Unique class name
                         style={"width": "65%","flex": 1, "text-align": "center", "border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "10px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"},  
                         children=[dcc.Graph(id='station-departure-id'),]),
                html.Div(className="station-arrival-time",  
                         style={"width": "65%","flex": 1, "text-align": "center", "border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "10px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"},  
                         children=[dcc.Graph(id='station-arrival-id'),]),
            ]
        ),

        html.Div(className="output-container-3", 
                 style={"width": "90%", "height": "500px", "margin-top": "20px", "display": "flex", "align-items": "stretch",
                   "justify-content": "space-between", "margin-left": "40px", "padding": "15px"},
                   children=[
            html.Div(className="dash-graph", style={"width": "25%","flex": 1, "text-align": "center", "border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "5px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"} ,children=[
                dcc.Graph(id="station-sb-chart-1"),
            ]),
            html.Div(className="dash-graph", style={"width": "25%","flex": 1, "text-align": "center", "border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "5px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"} , children=[
                dcc.Graph(id="station-sb-chart-2"),
            ]),
            html.Div(className="dash-graph", style={"width": "25%","flex": 1, "text-align": "center", "border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "5px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"} , children=[
                dcc.Graph(id="station-sb-chart-3"),
            ]),
        ]),


        html.Div(className="output-container-4", 
                 style={"width": "90%", "height": "500px", "margin-top": "20px", "display": "flex", "align-items": "stretch",
                   "justify-content": "space-between", "margin-left": "40px", "padding": "15px"},
                   children=[
            html.Div(className="dash-graph", style={"width": "30%","flex": 1, "text-align": "center", "border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "5px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"} ,children=[
                dcc.Graph(id="station-pie-chart-1"),
            ]),
            html.Div(className="dash-graph", style={"width": "30%","flex": 1, "text-align": "center", "border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "5px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"} , children=[
                dcc.Graph(id="station-pie-chart-2"),
            ]),
            html.Div(className="dash-graph", style={"width": "30%","flex": 1, "text-align": "center", "border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "5px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"} , children=[
                dcc.Graph(id="station-pie-chart-3"),
            ]),
        ]),

        html.Div(className="output-container-5", 
                 style={"width": "90%", "height": "500px", "margin-top": "20px", "display": "flex", "align-items": "stretch",
                   "justify-content": "space-between", "margin-left": "40px", "padding": "15px"},
                   children=[
            html.Div(className="dash-graph", style={"width": "30%","flex": 1, "text-align": "center", "border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "5px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"} ,children=[
                dcc.Graph(id="station-bar-chart-1"),
            ]),
            html.Div(className="dash-graph", style={"width": "30%","flex": 1, "text-align": "center", "border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "5px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"} , children=[
                dcc.Graph(id="station-bar-chart-2"),
            ]),
            html.Div(className="dash-graph", style={"width": "30%","flex": 1, "text-align": "center", "border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "5px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"} , children=[
                dcc.Graph(id="station-bar-chart-3"),
            ]),
        ]),




])

df = pd.DataFrame(data)

def register_callbacks(app):
    @app.callback(
        [Output("station-map-id", "children"),
         Output("station-trip-info", "children"),
         Output("station-text-id", "children"),
         Output("station-line-chart-1", "figure"),
         Output("station-line-chart-2", "figure"),
         Output("station-departure-id", "figure"),
         Output("station-arrival-id", "figure"),
         Output("station-sb-chart-1", "figure"),
         Output("station-sb-chart-2", "figure"),
         Output("station-sb-chart-3", "figure"),
         Output("station-pie-chart-1", "figure"),
         Output("station-pie-chart-2", "figure"),
         Output("station-pie-chart-3", "figure"),
         Output("station-bar-chart-1", "figure"),
         Output("station-bar-chart-2", "figure"),
         Output("station-bar-chart-3", "figure"),
         ],
        [Input("dept-dropdown", "value"),
         Input("arr-dropdown", "value"),
         Input("week-dropdown", "value")]
    )
    def update_charts(dep_location, arr_location, weekday):
        if not dep_location or not arr_location:
            return "", [], "Please select both departure and arrival stations."
        
        data_filter = df[(df["Departure Station"] == dep_location) & (df["Arrival Destination"] == arr_location)]
        
        if data_filter.empty:
            return "", [], "No data available for the selected route."
        
        first_row = data_filter.iloc[0]
        departure_coords = [first_row["Departure Latitude"], first_row["Departure Longitude"]]
        arrival_coords = [first_row["Arrival Latitude"], first_row["Arrival Longitude"]]
        travel_distance = first_row["Distance"].astype(int)
        coordinates = [51.5072, 0.1276]  # Example coordinates (London)

        site_map = folium.Map(location=coordinates, prefer_canvas=True, zoom_start=5, min_zoom=5, max_zoom=5,width='100%', height='100%')
        folium.Marker(departure_coords, popup=dep_location, icon=folium.Icon(color='red')).add_to(site_map)
        folium.Marker(arrival_coords, popup=arr_location, icon=folium.Icon(color='green')).add_to(site_map)
        folium.PolyLine(locations=[departure_coords, arrival_coords], popup=f"Estimated Distance Covered: {travel_distance} km", weight=3).add_to(site_map)
        map_html = site_map._repr_html_()
        map_html = html.Iframe(srcDoc=map_html, width='99%', height='550px')

        if weekday == "All":
            data_filter = df[(df["Departure Station"] == dep_location) & (df["Arrival Destination"] == arr_location)]
        else:
            data_filter = df[(df["Departure Station"] == dep_location) & (df["Arrival Destination"] == arr_location) & (df["Day of week"] == weekday)]

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
            html.H4("Trip Overview", style={"font-weight": "bold","font-size": "22px", "text-align": "center", "margin-bottom": "15px"}),
            html.P([html.B("Departure Destination: "), str(dep_location)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px", "padding":"5px"}),
            html.P([html.B("Arrival Destination: "), str(arr_location)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px", "padding":"5px"}),
            html.P([html.B("Number of Travels: "), str(no_of_travel)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px", "padding":"5px"}),
            html.P([html.B("Distance Covered: "), f"{distance} km"], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px", "padding":"5px"}),
            html.P([html.B("Average Spend: "), f"£{average_spend}"], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px", "padding":"5px"}),
            html.P([html.B("Refund Requests: "), str(refunded)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px", "padding":"5px"}),
            html.P([html.B("On Time Journeys: "), str(on_time)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px", "padding":"5px"}),
            html.P([html.B("Delayed Journeys: "), str(delayed)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px", "padding":"5px"}),
            html.P([html.B("Cancelled Journeys: "), str(cancelled)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px", "padding":"5px"}),
            html.P([html.B("First Class Tickets: "), str(first_class)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px", "padding":"5px"}),
            html.P([html.B("Standard Tickets: "), str(standard)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px", "padding":"5px"})
        ]

        text_info = f"The markers on the map identify stations by their latitude and longitude coordinates. The red marker denotes the departure station, while the green marker signifies the arrival destination. The line connecting these markers represents a potential route, with the distance estimated based on the approximate distance between two points on Earth's surface. For instance, the estimated distance between {dep_location} and {arr_location} is {distance} km."

        # Second Container
        # First Line Chart
        grouped_data_price = data_filter.groupby('Date of Purchase')['Price'].sum().cumsum().reset_index()
        fig1 = px.line(grouped_data_price, x="Date of Purchase", y="Price", title=f"<b>Overall Cumulative UK Train Ticket Revenue.</b>")
        fig1.update_yaxes(range=[0, max(grouped_data_price['Price']) * 1.1])
        fig1.update_layout(
            xaxis_title="Date of Purchase",
            yaxis_title="Ticket Price Paid in pounds (£)",
            title_x=0.5,
            title_y=0.90,
            title_font_size=18,
            font_size=14,
            width=920,  # Set the width of the figure
            height=600,  # Set the height of the figure
            paper_bgcolor = 'rgba(0,0,0,0)',
            plot_bgcolor = 'rgba(0,0,0,0)',
        )
        # Second Line Chart
        grouped_data_price = data_filter.sort_values(by="Date of Purchase")
        grouped_data_cumsum = df.groupby('Date of Purchase')[['Actual Price', 'Discount']].sum().cumsum().reset_index()
        grouped_data_cumsum = grouped_data_cumsum.reset_index()
        fig2 = px.line(grouped_data_cumsum, 
                x="Date of Purchase", 
                y=["Actual Price", "Discount"],
                title="<b>Overall UK Train Ticket Actual Prices and Discounts given</b>",
                labels={"value": "Amount in pounds (£)", 
                        "variable": "Metrics", 
                        "Date of Purchase": "Date"})
        
        fig2.update_yaxes(range=[0, max(grouped_data_cumsum['Actual Price']) * 1.1])
        fig2.update_layout(
                xaxis_title="Date of Purchase",
                title_x=0.5,
                title_y=0.90,
                title_font_size=18,
                font_size=14,
                width= 920,  # Set the width of the figure
                height=600,  # Set the height of the figure
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=0.95,
                    xanchor="right",
                    x=0.7,  # Adjust the x position to make space for the charts
                    bgcolor='rgba(255,255,255,0.5)',  # Set legend background color with transparency
                    bordercolor='rgba(0,0,0,0)'  # Set legend border color to transparent
            )
        )
        # Third Charts Sections
        # Departure Time Chart
        all_hours = pd.DataFrame({"Hour of Departure": list(hour_labels.keys())})
        bar_group =  data_filter["Hour of Departure"].value_counts().reset_index().sort_values(by="Hour of Departure")
        bar_group.columns = ["Hour of Departure", "count"]
        bar_group = all_hours.merge(bar_group, on="Hour of Departure", how="left").fillna(0)
        bar_group['Hour of Departure'] = bar_group['Hour of Departure'].map(hour_labels)
        fig3 = px.bar(bar_group, x="Hour of Departure", y="count", title=f"<b>Overall Departure Hours</b>")
        fig3.update_xaxes(range=[0, 23],
                      tickmode='linear',  # Set tick mode to linear
                      tick0=0,  # Start ticks from 0
                      dtick=1,  # Set the step size between ticks to 1
                      showticklabels=True)
        fig3.update_layout(
                xaxis_title="Hour of Departure",
                yaxis_title= "Count of Travelers",
                title_x=0.50,
                title_y=0.95,
                title_font_size=18,
                font_size=14,
                width=920,
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
        # Arrival Bar Chart
        all_hours = pd.DataFrame({"Hour of Arrival": list(hour_labels.keys())})
        bar_group =  data_filter["Hour of Arrival"].value_counts().reset_index().sort_values(by="Hour of Arrival")
        bar_group.columns = ["Hour of Arrival", "count"]
        bar_group = all_hours.merge(bar_group, on="Hour of Arrival", how="left").fillna(0)
        bar_group['Hour of Arrival'] = bar_group['Hour of Arrival'].map(hour_labels)
        fig4 = px.bar(bar_group, x="Hour of Arrival", y="count", title=f"<b>Overall Arrival Hours</b>")
        fig4.update_xaxes(range=[0, 23],
                      tickmode='linear',  # Set tick mode to linear
                      tick0=0,  # Start ticks from 0
                      dtick=1,  # Set the step size between ticks to 1
                      showticklabels=True)
        fig4.update_layout(
                xaxis_title="Hour of Arrival",
                yaxis_title= "Count of Travelers",
                title_x=0.50,
                title_y=0.95,
                title_font_size=18,
                font_size=14,
                width=920,
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


        # Fourth Containers
        # Sub Burst Chart 1
        sb = data_filter.groupby(["Purchase Type", "Payment Method", "Journey Status"])["Journey Status"].value_counts().reset_index()
        fig5 = px.sunburst(sb, path=["Purchase Type", "Payment Method", "Journey Status"], values="count", color_continuous_scale='Blues', color="Journey Status", title="<b>Overall Distribution of Purchases by <br>Type, Payment Method, and Journey Status</b>")
        fig5.update_layout(
            title_x=0.55,
            title_y=0.93,
            title_font_size=18,
            font_size=14,
            width=500,
            height=500,
            paper_bgcolor = 'rgba(0,0,0,0)',
            plot_bgcolor = 'rgba(0,0,0,0)',
        )
        # Sunburst
        if sb.empty:
            fig5.add_annotation(
                text="No Valid data points available",
                showarrow=False,
                font=dict(size=18),
                x=0.55,
                y=0.5)

        # Sub Burst Chart 2
        data_filter['Hour of Arrival Label'] = data_filter['Hour of Arrival'].map(hour_labels)
        sb = data_filter.groupby(["Hour of Arrival Label", "Journey Status"])["Journey Status"].value_counts().reset_index()
        fig6 = px.sunburst(sb, path=["Hour of Arrival Label", "Journey Status"], values="count", color="Journey Status", color_continuous_scale='Blues', title="<b>Overall Distribution Arrival Hours by <br> Journey Status</b>")
        fig6.update_layout(
            title_x=0.55,
            title_y=0.93,
            title_font_size=18,
            font_size=14,
            width=500,
            height=500,
            paper_bgcolor = 'rgba(0,0,0,0)',
            plot_bgcolor = 'rgba(0,0,0,0)',
        )


        # Sunburst
        if sb.empty:
            fig6.add_annotation(
                text="No Valid data points available",
                showarrow=False,
                font=dict(size=18),
                x=0.55,
                y=0.5)

        # Sun-burst-chart-3
        sb = data_filter.groupby(["Purchase Type", "Payment Method", "Ticket Class", "Ticket Type"])["Ticket Class"].value_counts().reset_index()
        fig7 = px.sunburst(sb, path=["Purchase Type", "Payment Method", "Ticket Type", "Ticket Class"], values="count", color="Ticket Class",color_continuous_scale='Blues', title="<b>Overall Distribution Arrival Hours by <br> Journey Status</b>")
        fig7.update_layout(
            title_x=0.55,
            title_y=0.93,
            title_font_size=18,
            font_size=14,
            width=500,
            height=500,
            paper_bgcolor = 'rgba(0,0,0,0)',
            plot_bgcolor = 'rgba(0,0,0,0)',
        )

        # Sunburst
        if sb.empty:
            fig7.add_annotation(
                text="No Valid data points available",
                showarrow=False,
                font=dict(size=18),
                x=0.55,
                y=0.5)

        # Fifth Containers
        # Pie Chart 1
        pie_1 = data_filter.groupby("Journey Status")["Journey Status"].value_counts().reset_index()
        fig8 = px.pie(pie_1, values='count', names="Journey Status", title=f"<b>Overall Journey Status Breakdown</b>", hole=0.35)
        fig8.update_layout(
            title_x=0.50,
            title_y=0.95,
            title_font_size=18,
            font_size=14,
            width=500,
            height=500,
            paper_bgcolor = 'rgba(0,0,0,0)',
            plot_bgcolor = 'rgba(0,0,0,0)',
        )
        # Check if the pie chart is empty
        if pie_1.empty:
            fig8.add_annotation(
                text="No Valid data points available",
                showarrow=False,
                font=dict(size=18),
                x=0.55,
                y=0.5)

        

        # Pie Chart 2
        pie_2 = data_filter.groupby("Ticket Class")["Ticket Class"].value_counts().reset_index()
        fig9 = px.pie(pie_2, values='count', names="Ticket Class", title=f"<b>Overall Ticket Class Breakdown</b>", hole=0.35)
        fig9.update_layout(
            title_x=0.50,
            title_y=0.95,
            title_font_size=16,
            width=500,
            height=500,
            paper_bgcolor = 'rgba(0,0,0,0)',
            plot_bgcolor = 'rgba(0,0,0,0)',
        )
        # Check if the pie chart is empty
        if pie_2.empty:
            fig9.add_annotation(
                text="No Valid data points available",
                showarrow=False,
                font=dict(size=18),
                x=0.55,
                y=0.5)


        pie_3 = data_filter.groupby("Refund Request")["Refund Request"].value_counts().reset_index()
        fig10 = px.pie(pie_3, values='count', names="Refund Request", title=f"<b>Overall Refund Request Breakdown</b>", hole=0.35)
        fig10.update_layout(
            title_x=0.50,
            title_y=0.95,
            title_font_size=16,
            width=500,
            height=500,
            paper_bgcolor = 'rgba(0,0,0,0)',
            plot_bgcolor = 'rgba(0,0,0,0)',
        )

        if pie_3.empty:
            fig10.add_annotation(
                text="No Valid data points available",
                showarrow=False,
                font=dict(size=18),
                x=0.55,
                y=0.5)
            
        # Sixth Containers
        bar_1 = data_filter.groupby("Payment Method")["Payment Method"].value_counts().reset_index()
        fig11 = px.bar(bar_1, x="Payment Method", y="count", title="<b>Overall Payment Method</b>")
        fig11.update_layout(
            title_x=0.50,
            title_y=0.95,
            yaxis_title= "Count of Payments made",
            title_font_size=16,
            width=500,
            height=500,
            paper_bgcolor = 'rgba(0,0,0,0)',
            plot_bgcolor = 'rgba(0,0,0,0)',
        )

        if bar_1.empty:
            fig11.add_annotation(
                text="No Valid data points available",
                showarrow=False,
                font=dict(size=18),
                x=0.55,
                y=0.5)

        bar_2 = data_filter.groupby("Ticket Type")["Ticket Type"].value_counts().reset_index()
        fig12 = px.bar(bar_2, x="Ticket Type", y="count", title="<b>Overall Ticket Type</b>")
        fig12.update_layout(
            title_x=0.50,
            title_y=0.95,
            yaxis_title= "Count of Ticket Type",
            title_font_size=16,
            width=500,
            height=500,
            paper_bgcolor = 'rgba(0,0,0,0)',
            plot_bgcolor = 'rgba(0,0,0,0)',
        )
        if bar_2.empty:
            fig12.add_annotation(
                text="No Valid data points available",
                showarrow=False,
                font=dict(size=18),
                x=0.55,
                y=0.5)
        
        bar_3 = data_filter.groupby("Railcard")["Railcard"].value_counts().reset_index()
        fig13 = px.bar(bar_3, x="Railcard", y="count", title="<b>Overall Railcard Usage</b>")
        fig13.update_layout(
            title_x=0.50,
            title_y=0.95,
            yaxis_title= "Count of Railcard used",
            title_font_size=16,
            width=500,
            height=500,
            paper_bgcolor = 'rgba(0,0,0,0)',
            plot_bgcolor = 'rgba(0,0,0,0)',
    )
        if bar_3.empty:
            fig13.add_annotation(
                text="No Valid data points available",
                showarrow=False,
                font=dict(size=18),
                x=0.55,
                y=0.5)




        # Return all Functions
        return map_html, info, text_info, fig1,fig2, fig3,fig4, fig5, fig6, fig7, fig8, fig9, fig10, fig11, fig12, fig13