import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import folium


data = pd.read_csv("D:/My Learning/My Projects/Project UK Railways/Dashboard App/Data/Uk-Train Data.csv")

hour_labels = {
    0: "12 AM", 1: "1 AM", 2: "2 AM", 3: "3 AM", 4: "4 AM",
    5: "5 AM", 6: "6 AM", 7: "7 AM", 8: "8 AM", 9: "9 AM",
    10: "10 AM", 11: "11 AM", 12: "12 PM", 13: "1 PM", 14: "2 PM",
    15: "3 PM", 16: "4 PM", 17: "5 PM", 18: "6 PM", 19: "7 PM",
    20: "8 PM", 21: "9 PM", 22: "10 PM", 23: "11 PM"
}


layout = html.Div(
    className="overall",
    children=[
        html.P(
            "This interactive web dashboard is designed to explore traveler behavior and operational performance in UK Railways., Discover the comprehensive overview of UK railway transport here, encompassing various aspects and insights.",
            style={"font-family": "Roboto, sans-serif", "font-size": "20px", "margin-left": "10px", "overflow": "hidden"}
        ),
        html.Br(),
        html.Div(
            className="overall-output-container-1",
            style={"width": "95%", "height": "520px"},
            children=[
                html.Div(
                    className="overall-Map-section",
                    style={"display": "flex", "justify-content": "space-between", "height": "480px",
                           "background-color": "#f8f9fa", "overflow": "hidden"},
                    children=[
                        html.Div(
                            className="overall-Map",
                            id='overall-map-id',
                            children=[],
                            style={"height": "480px", "width": "65%", "overflow": "hidden", "border-radius": "20px", "box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"}
                        ),
                        html.Div(
                            className="overall-trip-info",
                            id='overall-trip-id',
                            children=[],
                            style={"width": "40%", "padding": "20px", "display": "flex","background-color": "#f8f9fa",
                                   "flex-direction": "column", "height": "100%", "line-height": "16px",
                                   "margin-left": "10px", "border-radius": "20px", "box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"}
                        ),
                    ]
                ),
                html.P(
                    id="overall-text-id-1",
                    className="text-class-1",
                    children="Each dot represents a major railway station, and the lines illustrate all unique rail routes connecting these main stations in the UK rail network.",
                    style={"font-size": "18px", "padding": "10px", "margin-left": "20px"}
                )
            ]
        ),
        html.Br(),
        html.Div(
            className="output-container-1",
            style={"width": "90%", "height": "620px", "margin-top": "20px", "display": "flex", "align-items": "stretch",
                   "justify-content": "space-between", "margin-left": "10px", "padding": "5px"},
            children=[
                html.Div(
                    className="dash-graph",
                    style={"flex": 1, "text-align": "center", "width": "50%","border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "10px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"},
                    children=[
                        dcc.Graph(id="line-chart-1"),
                    ]
                ),
                html.Div(
                    className="dash-graph",
                    style={"flex": 1, "text-align": "center", "width": "50%","border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "5px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"},
                    children=[
                        dcc.Graph(id="line-chart-2"),
                    ]
                ),
            ]
        ),
        html.Div(
            className="overall-time-container",
            style={"width": "90%", "height": "620px", "margin-top": "20px", "display": "flex", "align-items": "stretch",
                   "justify-content": "space-between", "margin-left": "10px", "padding": "5px"},
            children=[
                html.Div(className="overall-departure-time",  # Unique class name
                         style={"width": "50%","flex": 1, "text-align": "center", "border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "10px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"},  
                         children=[dcc.Graph(id='overall-departure-id'),]),
                html.Div(className="overall-arrival-time",  
                         style={"width": "50%","flex": 1, "text-align": "center", "border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "10px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"},  
                         children=[dcc.Graph(id='overall-arrival-id'),]),
            ]
        ),


        html.Div(className="output-container-3", 
                 style={"width": "90%", "height": "500px", "margin-top": "20px", "display": "flex", "align-items": "stretch",
                   "justify-content": "space-between", "margin-left": "40px", "padding": "15px"},
                   children=[
            html.Div(className="dash-graph", style={"width": "30%","flex": 1, "text-align": "center", "border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "5px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"} ,children=[
                dcc.Graph(id="sb-chart-1"),
            ]),
            html.Div(className="dash-graph", style={"width": "30%","flex": 1, "text-align": "center", "border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "5px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"} , children=[
                dcc.Graph(id="sb-chart-2"),
            ]),
            html.Div(className="dash-graph", style={"width": "30%","flex": 1, "text-align": "center", "border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "5px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"} , children=[
                dcc.Graph(id="sb-chart-3"),
            ]),
        ]),

        html.Div(className="output-container-4", 
                 style={"width": "90%", "height": "500px", "margin-top": "20px", "display": "flex", "align-items": "stretch",
                   "justify-content": "space-between", "margin-left": "40px", "padding": "15px"},
                   children=[
            html.Div(className="dash-graph", style={"width": "30%","flex": 1, "text-align": "center", "border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "5px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"} ,children=[
                dcc.Graph(id="pie-chart-1"),
            ]),
            html.Div(className="dash-graph", style={"width": "30%","flex": 1, "text-align": "center", "border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "5px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"} , children=[
                dcc.Graph(id="pie-chart-2"),
            ]),
            html.Div(className="dash-graph", style={"width": "30%","flex": 1, "text-align": "center", "border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "5px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"} , children=[
                dcc.Graph(id="pie-chart-3"),
            ]),
        ]),


        html.Div(className="output-container-5", 
                 style={"width": "90%", "height": "500px", "margin-top": "20px", "display": "flex", "align-items": "stretch",
                   "justify-content": "space-between", "margin-left": "40px", "padding": "15px"},
                   children=[
            html.Div(className="dash-graph", style={"width": "30%","flex": 1, "text-align": "center", "border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "5px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"} ,children=[
                dcc.Graph(id="bar-chart-1"),
            ]),
            html.Div(className="dash-graph", style={"width": "30%","flex": 1, "text-align": "center", "border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "5px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"} , children=[
                dcc.Graph(id="bar-chart-2"),
            ]),
            html.Div(className="dash-graph", style={"width": "30%","flex": 1, "text-align": "center", "border-radius": "15px", "height": "100%", "margin-right": "4%", "padding-left": "5px","box-shadow": "0 0 10px rgba(0, 0, 0, 0.1)"} , children=[
                dcc.Graph(id="bar-chart-3"),
            ]),
        ]),
    ]
)


def register_callbacks(app):
    @app.callback(
        [Output("overall-map-id", "children"),
         Output("overall-trip-id", "children"),
         Output("line-chart-1", "figure"),
         Output("line-chart-2", "figure"),
         Output("overall-departure-id", "figure"),
         Output("overall-arrival-id", "figure"),
         Output("sb-chart-1", "figure"),
         Output("sb-chart-2", "figure"),
         Output("sb-chart-3", "figure"),
         Output("pie-chart-1", "figure"),
         Output("pie-chart-2", "figure"),
         Output("pie-chart-3", "figure"),
         Output("bar-chart-1", "figure"),
         Output("bar-chart-2", "figure"),
         Output("bar-chart-3", "figure"),],
        [Input('data-store', 'data')]
    )
    def update_chart(data):
        # Convert data to DataFrame if it's not already one
        df = pd.DataFrame(data)
        
        # Filter the necessary columns for the map
        data_filter = df[["Departure Station", "Arrival Destination", "Departure Latitude", "Departure Longitude", 
            "Arrival Latitude", "Arrival Longitude"]].drop_duplicates()
        coordinates = [51.5072, -0.1276]
        site_map = folium.Map(location=coordinates, prefer_canvas=True, zoom_start=5, min_zoom=5, 
            max_zoom=5, width='100%', height='100%')

        for _, row in data_filter.iterrows():
            departure_coords = [row["Departure Latitude"], row["Departure Longitude"]]
            arrival_coords = [row["Arrival Latitude"], row["Arrival Longitude"]]
            Departure_stations = row["Departure Station"]
            Arrival_stations = row["Arrival Destination"]

            folium.CircleMarker(
                location=departure_coords,
                radius=3,
                color='blue',
                fill=True,
                fill_color='blue',
                fill_opacity=0.6,
                popup=Departure_stations
            ).add_to(site_map)
            folium.CircleMarker(
                location=arrival_coords,
                radius=3,
                color='blue',
                fill=True,
                fill_color='blue',
                fill_opacity=0.6,
                popup=Arrival_stations
            ).add_to(site_map)

            folium.PolyLine(
                locations=[departure_coords, arrival_coords],
                color='blue',
                weight=2
            ).add_to(site_map)
        
        map_html = site_map._repr_html_()
        map_html = html.Iframe(srcDoc=map_html, style={"width": "100%", "height": "100%", "border": "none"})

        # Calculate the statistics
        no_of_travel = len(df)
        distance = df["Distance"].mean().round(2).astype(str)
        Departure_stations_counts = len(df["Departure Station"].unique())
        Arrival_stations_counts = len(df["Arrival Destination"].unique())
        average_spend = df["Price"].mean().round(2)
        refunded = df[df["Refund Request"] == "Yes"]["Refund Request"].count()
        on_time = df[df["Journey Status"] == "On Time"]["Journey Status"].count()
        delayed = df[df["Journey Status"] == "Delayed"]["Journey Status"].count()
        cancelled = df[df["Journey Status"] == "Cancelled"]["Journey Status"].count()
        first_class = df[df["Ticket Class"] == "First Class"]["Ticket Class"].count()
        standard = df[df["Ticket Class"] == "Standard"]["Ticket Class"].count()
    
        info = [
            html.H4("Overall Trip Overview", style={"font-weight": "bold","font-size": "22px", "text-align": "center", "margin-bottom": "15px"}),
            html.P([html.B("Number of Travels Made: "), str(no_of_travel)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px", "padding":"5px"}),
            html.P([html.B("Number of Departure Destinations: "), str(Departure_stations_counts)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px", "padding":"5px"}),
            html.P([html.B("Number of Arrival Destinations: "), f"{str(Arrival_stations_counts)}"], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px", "padding":"5px"}),
            html.P([html.B("Most Busiest Departure Station: "), "Manchester Piccadilly"], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px", "padding":"5px"}),
            html.P([html.B("Most Busiest Arrival Station: "), "Birmingham New Street"], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px", "padding":"5px"}),
            html.P([html.B("Average Distance Covered: "), f"{str(distance)} km"], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px", "padding":"5px"}),
            html.P([html.B("Average Spend: "), f"£{str(average_spend)}"], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px", "padding":"5px"}),
            html.P([html.B("Refund Requests: "), str(refunded)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px", "padding":"5px"}),
            html.P([html.B("On Time Journeys: "), str(on_time)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px", "padding":"5px"}),
            html.P([html.B("Delayed Journeys: "), str(delayed)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px", "padding":"5px"}),
            html.P([html.B("Cancelled Journeys: "), str(cancelled)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px", "padding":"5px"}),
            html.P([html.B("First Class Tickets: "), str(first_class)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px", "padding":"5px"}),
            html.P([html.B("Standard Tickets: "), str(standard)], style={"font-size": "18px", "text-align": "left", "margin-bottom": "5px", "padding":"5px"})
        ]
    
        # Second Charts
        grouped_data_price = df.groupby('Date of Purchase')['Price'].sum().cumsum().reset_index()
        fig1 = px.line(grouped_data_price, x="Date of Purchase", y="Price", title=f"<b>Overall Cumulative UK Train Ticket Revenue.</b>")
        fig1.update_yaxes(range=[0, max(grouped_data_price['Price']) * 1.1])
        fig1.update_layout(
            xaxis_title="Date of Purchase",
            yaxis_title="Ticket Price Paid in pounds (£)",
            title_x=0.5,
            title_y=0.90,
            title_font_size=18,
            font_size=14,
            width=900,  # Set the width of the figure
            height=600,  # Set the height of the figure
            paper_bgcolor = 'rgba(0,0,0,0)',
            plot_bgcolor = 'rgba(0,0,0,0)',
        )
        grouped_data_price = df.sort_values(by="Date of Purchase")
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
                width= 900,  # Set the width of the figure
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
        bar_group =  df["Hour of Departure"].value_counts().reset_index().sort_values(by="Hour of Departure")
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
                width=900,
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

        bar_group =  df["Hour of Arrival"].value_counts().reset_index().sort_values(by="Hour of Arrival")
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
                width=900,
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
        sb = df.groupby(["Purchase Type", "Payment Method", "Journey Status"])["Journey Status"].value_counts().reset_index()
        fig5 = px.sunburst(sb, path=["Purchase Type", "Payment Method", "Journey Status"], values="count", color_continuous_scale='Blues', color="Journey Status", title="<b>Overall Distribution of Purchases by <br>Type, Payment Method, and Journey Status</b>")
        fig5.update_layout(
            title_x=0.5,
            title_y=0.93,
            title_font_size=18,
            font_size=14,
            width=500,
            height=500,
            paper_bgcolor = 'rgba(0,0,0,0)',
            plot_bgcolor = 'rgba(0,0,0,0)',
        )

        # Sub Burst Chart 2
        df['Hour of Arrival Label'] = df['Hour of Arrival'].map(hour_labels)
        sb = df.groupby(["Hour of Arrival Label", "Journey Status"])["Journey Status"].value_counts().reset_index()
        fig6 = px.sunburst(sb, path=["Hour of Arrival Label", "Journey Status"], values="count", color="Journey Status", color_continuous_scale='Blues', title="<b>Overall Distribution Arrival Hours by <br> Journey Status</b>")
        fig6.update_layout(
            title_x=0.5,
            title_y=0.93,
            title_font_size=18,
            font_size=14,
            width=500,
            height=500,
            paper_bgcolor = 'rgba(0,0,0,0)',
            plot_bgcolor = 'rgba(0,0,0,0)',
        )

        # Sun-burst-chart-3
        sb = df.groupby(["Purchase Type", "Payment Method", "Ticket Class", "Ticket Type"])["Ticket Class"].value_counts().reset_index()
        fig7 = px.sunburst(sb, path=["Purchase Type", "Payment Method", "Ticket Type", "Ticket Class"], values="count", color="Ticket Class",color_continuous_scale='Blues', title="<b>Overall Distribution Arrival Hours by <br> Journey Status</b>")
        fig7.update_layout(
            title_x=0.5,
            title_y=0.93,
            title_font_size=18,
            font_size=14,
            width=500,
            height=500,
            paper_bgcolor = 'rgba(0,0,0,0)',
            plot_bgcolor = 'rgba(0,0,0,0)',
        )

        # Fifth Containers
        # Pie Chart 1
        pie_1 = df.groupby("Journey Status")["Journey Status"].value_counts().reset_index()
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

        # Pie Chart 2
        pie_2 = df.groupby("Ticket Class")["Ticket Class"].value_counts().reset_index()
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

        pie_3 = df.groupby("Refund Request")["Refund Request"].value_counts().reset_index()
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
    
        # Sixth Containers
        bar_1 = df.groupby("Payment Method")["Payment Method"].value_counts().reset_index()
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


        bar_2 = df.groupby("Ticket Type")["Ticket Type"].value_counts().reset_index()
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
        
        bar_3 = df.groupby("Railcard")["Railcard"].value_counts().reset_index()
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

        



        return map_html, info, fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9, fig10, fig11, fig12, fig13




