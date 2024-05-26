import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import folium


# Load the dataset
data = pd.read_csv("https://raw.githubusercontent.com/Kishores2801/Uk-Train-Dash-app/main/Data/Uk-Train%20Data.csv")
weekday_order = ["All", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]





# Initialize the Dash app
app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True

# Define the layout for the main app
app.layout = html.Div(className='main-container', children=[
    html.Div(
    className="home",
    children=[
        html.Div(className="nav-bar", children=[html.H1("UK Train Traveling Web Dashboard")]),
        html.P("This interactive web dashboard is designed to explore traveler behavior and operational performance in UK Railways."),
        html.Br(),
        # Building the Dropdown Divs
        html.Div(className="full-dropdowns", children=[
            html.Div(className="departure-station", children=[
                html.H3("Select the Departure Station: "),
                dcc.Dropdown(
                    id="dept-dropdown",
                    options=[{'label': station, 'value': station} for station in data["Departure Station"].unique()],
                    value=data["Departure Station"].unique()[0]  # Set a default value
                ),
            ]),
            html.Div(className="arrival-station", children=[
                html.H3("Select the Arrival Station: "),
                dcc.Dropdown(id="arr-dropdown", options=[], value=None),
            ]),
            html.Div(className="weekday", children=[
                html.H3("Select the day: "),
                dcc.Dropdown(id="week-dropdown",
                             options=[{'label': day, 'value': day} for day in weekday_order],
                             value="All")
            ]),
            
            html.Br(),
            html.Br(),
        ]),
        html.Div(className="output-container-1", children=[
            html.Div(className="Map-section", children=[
                html.Div(className="Map", id='map-id', children=[]),
                html.Div(className="trip-info", id='trip-id', children=[]),
            ]),
            html.P(id="text-id-1", className="text-class-1", children=""),
        ]),
        html.Div(className="output-container-2", children=[
            html.Div(className="dash-graph", children=[
                dcc.Graph(id="line-chart-1"),
            ]),
            
            html.Div(className="dash-graph", children=[
                dcc.Graph(id="line-chart-2"),
            ]),
            
        ]),
        html.P(className="text-class-1", children="These charts display the cumulative sum of Actual Price, Discounted Price, and Paid Price over time. The Actual Price of Tickets was calculated after reverting discounts applied for railcards and Advance or Off-Peak Ticket Types. Discounts were calculated by subtracting the Actual Price from the Final Price."),


        html.Div(className="output-container-2", children=[
            html.Div(className="dash-graph", children=[
                dcc.Graph(id="bar-chart-1"),
            ]),
        ]),
        html.P(className="text-class-2", children="This chart depicts the busiest hours at each departure station, showcasing the distribution of departure times. It reveals a recurring pattern commonly seen in railway stations, with notable spikes in passenger traffic occurring at approximately 8:00 AM and 8:00 PM. This pattern suggests a consistent 12-hour cycle of activity throughout the day."),

        html.Div(className="output-container-3", children=[
            html.Div(className="dash-graph", children=[
                dcc.Graph(id="sb-chart-1"),
            ]),
            html.Div(className="dash-graph", children=[
                dcc.Graph(id="sb-chart-2"),
            ]),
        ]),

        html.Div(className="output-container-4", children=[
            html.Div(className="dash-graph", children=[
                dcc.Graph(id="pie-chart-1"),
            ]),
            html.Div(className="dash-graph", children=[
                dcc.Graph(id="pie-chart-2"),
            ]),
            html.Div(className="dash-graph", children=[
                dcc.Graph(id="pie-chart-3"),
            ]),
        ]),
        html.Div(className="output-container-5", children=[
            html.Div(className="dash-graph", children=[
                dcc.Graph(id="bar-chart-2"),
            ]),
            html.Div(className="dash-graph", children=[
                dcc.Graph(id="bar-chart-3"),
            ]),
            html.Div(className="dash-graph", children=[
                dcc.Graph(id="bar-chart-4"),
            ]),
        ]),
    ]
)

])



# # Callback to update the page content based on the URL
# @app.callback(Output('page-content', 'children'),
#               [Input('url', 'pathname')])
# def display_page(pathname):
#     if pathname == '/Prediction':
#         return prediction_layout
#     else:
#         return home_layout

# prediction_layout = html.Div(className="prediction", children=[
#     html.H1("Predicting the UK Train Ticket Price"),
#     html.Div(className="dropdown-full", children=[
#         html.Div(className="departure-station", children=[
#             html.H3("Select the Departure Station: "),
#             dcc.Dropdown(
#                 id="dept-dropdown",
#                 options=[{'label': station, 'value': station} for station in data["Departure Station"].unique()],
#                 value=data["Departure Station"].unique()[0]  # Set a default value
#             ),
#         ]),
#         html.Div(className="arrival-station", children=[
#             html.H3("Select the Arrival Station: "),
#             dcc.Dropdown(id="arr-dropdown", options=[], value=None),
#         ]),
#         html.Div(className="ticket-class", children=[
#             html.H3("Select the Ticket Class: "),
#             dcc.Dropdown(
#                 id="class-dropdown",
#                 options=[{'label': 'Standard', 'value': 'Standard'},
#                          {'label': 'First Class', 'value': 'First Class'}],
#                 value="Standard"
#             )
#         ]),
#         html.Div(className="purchase-type", children=[
#             html.H3("Select the Purchase Type: "),
#             dcc.Dropdown(
#                 id="type-dropdown",
#                 options=[{'label': 'Online', 'value': 'Online'},
#                          {'label': 'Station', 'value': 'Station'}],
#                 value="Online"
#             )
#         ]),
#         html.Div(className="payment-method", children=[
#             html.H3("Select the Payment Method: "),
#             dcc.Dropdown(
#                 id="payment-dropdown",
#                 options=[{'label': 'Debit Card', 'value': 'Debit Card'},
#                          {'label': 'Credit Card', 'value': 'Credit Card'},
#                          {'label': 'Contactless', 'value': 'Contactless'}],
#                 value="Debit Card"
#             )
#         ]),
#         html.Div(className="hour", children=[
#             html.H3("Select the Hour: "),
#             dcc.Dropdown(
#                 id="hour-dropdown",
#                 options=[{'label': f'{i}.00 am', 'value': str(i)} if i < 12 else {'label': f'{i}.00 pm', 'value': str(i)} for i in range(24)],
#                 value='0'  # Set a default value
#             )
#         ]),
#         html.Div(className="weekday", children=[
#             html.H3("Select the day: "),
#             dcc.Dropdown(
#                 id="week-dropdown",
#                 options=[{'label': day, 'value': day} for day in weekday_order],
#                 value="Monday"
#             ),
#         ]),
#         html.Div(className="railcard", children=[
#             html.H3("Select the RailCard: "),
#             dcc.Dropdown(
#                 id="railcard-dropdown",
#                 options=[{'label': 'Adult', 'value': 'Adult'},
#                          {'label': 'Disabled', 'value': 'Disabled'},
#                          {'label': 'Senior', 'value': 'Senior'},
#                          {'label': 'None', 'value': ''}],
#                 value=""
#             ),
#         ]),
#         html.Div(className="ticket-type", children=[
#             html.H3("Select the Ticket Type: "),
#             dcc.Dropdown(
#                 id="ticket-type-dropdown",
#                 options=[{'label': 'Anytime', 'value': 'Anytime'},
#                          {'label': 'Advance', 'value': 'Advance'},
#                          {'label': 'Off-Peak', 'value': 'Off-Peak'}],
#                 value="Anytime"
#             ),
#         ]),
#         html.Br(),
#         html.Button('Predict', id='predict-button', n_clicks=0),
#         html.Div(id='prediction-output')
#     ])
# ])

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
        html.H4("Trip Overview"),
        html.P([html.B("Departure Destination: "), str(dep_location)]),
        html.P([html.B("Arrival Destination: "), str(arr_location)]),
        html.P([html.B("Number of Travels: "), str(no_of_travel)]),
        html.P([html.B("Distance Covered: "), f"{distance} km"]),
        html.P([html.B("Average Spend: "), f"£{average_spend}"]),
        html.P([html.B("Refund Requests: "), str(refunded)]),
        html.P([html.B("On Time Journeys: "), str(on_time)]),
        html.P([html.B("Delayed Journeys: "), str(delayed)]),
        html.P([html.B("Cancelled Journeys: "), str(cancelled)]),
        html.P([html.B("First Class Tickets: "), str(first_class)]),
        html.P([html.B("Standard Tickets: "), str(standard)])
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
    grouped_data_price = data_filter.groupby('Date of Purchase')['Price'].sum().cumsum().reset_index()
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
    
    bar_group = data_filter.groupby("Day of week")["Hour"].value_counts().reset_index()
    fig3 = px.bar(bar_group, x="Hour", y="count", title=f"<b>Active Hours in {dep_location} station</b>")
    fig3.update_xaxes(range=[0, 23],
                      tickmode='linear',  # Set tick mode to linear
                      tick0=0,  # Start ticks from 0
                      dtick=1,  # Set the step size between ticks to 1
                      showticklabels=True)
    
    fig3.update_layout(
        xaxis_title="Hours",
        yaxis_title= "Count of Travelers",
        title_x=0.55,
        title_y=0.98,
        title_font_size=18,
        font_size=14,
        width=1500,
        height=700,
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
    sb = data_filter.groupby(["Hour", "Journey Status"])["Journey Status"].value_counts().reset_index()
    fig5 = px.sunburst(sb, path=["Hour", "Journey Status"], values="count", color="Journey Status", title="<b>Distribution Hours by Journey Status</b>")
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
     Output("bar-chart-4", "figure"),],
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

# Link your external stylesheet
app.css.append_css({
    'external_url': 'assets/styles.css'
})


if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port=8080)

