import dash
from dash import dcc, html

layout =html.Div(
    className="Observation",
    style={"border-radius": "10px", "background-color": "white", "margin":0,
           "box-shadow": "0 0 20px rgba(0, 0, 0, 0.1)", "margin-top": "20px",
           "margin-bottom": "5px", "padding": "40px"},
           children=[
               html.Div(
    className="map-Overview", 
    style={"border-radius": "10px", "background-color": "lightgray", 
           "box-shadow": "0 0 20px rgba(0, 0, 0, 0.1)", "margin-top": "20px",
           "margin-bottom": "5px", "padding": "18px"},
    children=[
        html.H4("Map Overview", style={"font-size": "24px", "margin-bottom": "6px", "margin-top": "20px", "text-align": "center", "font-weight": "bold"}),
        html.Ul([
            html.Li("There are 32 stations available in the Dataset, with 36,167 trips between these stations from January to April.", 
                    style={"padding-left": "20px", "font-size": "18px", "margin-bottom": "4px", "list-style-type": "none"}),
            html.Li([
                "The Most Busiest Departure Station is ", 
                html.B("Manchester Piccadilly"), 
                ", The Most Busiest Arrival Station is ", 
                html.B("Birmingham New Street"), 
                ", The Most common railway route is ", 
                html.B("Manchester Piccadilly to Liverpool Lime Street.")
            ], 
                style={"padding-left": "18px", "font-size": "18px", "margin-bottom": "4px", "list-style-type": "none"}),
            html.Li("Average spend by travelers is around £22.66 per trip, with a median spend of around £13.00 per trip.", 
                    style={"padding-left": "18px", "font-size": "18px", "margin-bottom": "4px", "list-style-type": "none"}),
            html.Li("The Average distance covered in each trip is 126 km, with a median distance of 80 km.", 
                    style={"padding-left": "18px", "font-size": "18px", "margin-bottom": "4px", "list-style-type": "none"})
        ]),
        html.Br(),
        html.Br(),
        html.Div([
            html.H4("Revenue Overview", style={"font-size": "24px", "margin-bottom": "6px", "margin-top": "20px", "text-align": "center", "font-weight": "bold"}),
            html.Ul([
                html.Li("Revenue Generated from Ticket sales within the last 3 months is £819,628, with an average of £6,403.34 revenue generated through tickets daily.", 
                        style={"padding-left": "20px", "font-size": "18px", "margin-bottom": "4px", "list-style-type": "none"}),
                html.Li("Travelers receive discounts based on the type of ticket purchased and if they use a railcard.", 
                        style={"padding-left": "20px", "font-size": "18px", "margin-bottom": "4px", "list-style-type": "none"}),
                html.Li("Travelers were offered discounts totaling £1,016,909, with an average of £7,944.60 discounts offered daily.", 
                        style={"padding-left": "20px", "font-size": "18px", "margin-bottom": "4px", "list-style-type": "none"})
            ])
        ]),
        html.Br(),
        html.Div([
            html.H4("Other Observations", style={"font-size": "24px", "margin-bottom": "6px", "margin-top": "20px", "text-align": "center", "font-weight": "bold"}),
            html.Ul([
                html.Li([
                    "The number of tickets purchased ", html.B("online"), " is 21,455, and 14,712 tickets were bought at stations."
                ], style={"padding-left": "20px", "font-size": "18px", "margin-bottom": "4px", "list-style-type": "none"}),
                html.Li([
                    "The most common payment method was ", html.B("Credit Card"), ", with 21,778 transactions, followed by Contactless with 12,292 transactions, and Debit Card with 2,097 transactions."
                ], style={"padding-left": "20px", "font-size": "18px", "margin-bottom": "4px", "list-style-type": "none"}),
                html.Li([
                    "The majority of tickets were for ", html.B("Standard class"), ", totaling 32,654, whereas First Class tickets amounted to 3,513."
                ], style={"padding-left": "20px", "font-size": "18px", "margin-bottom": "4px", "list-style-type": "none"}),
                html.Li([
                    "The most frequently purchased ticket type was ", html.B("Advance"), ", with 20,023 tickets sold, followed by Off-Peak with 10,067 tickets, and Anytime with 6,077 tickets."
                ], style={"padding-left": "20px", "font-size": "18px", "margin-bottom": "4px", "list-style-type": "none"}),
                html.Li([
                    "The majority of journeys were ", html.B("On Time"), ", totaling 31,611. There were 2,358 Delayed journeys and 2,198 Cancelled journeys."
                ], style={"padding-left": "20px", "font-size": "18px", "margin-bottom": "4px", "list-style-type": "none"}),
                html.Li([
                    "The highest number of departures occurred at ", html.B("8 AM"), ", with secondary peaks at 4 PM and 7 PM."
                ], style={"padding-left": "20px", "font-size": "18px", "margin-bottom": "4px", "list-style-type": "none"}),
                html.Li([
                    "The busiest day for departures is ", html.B("Sunday"), " with 5,335 trips, followed closely by Wednesday with 5,275 trips and Friday with 5,263 trips. Other notable days include Saturday with 5,133 trips, Tuesday and Monday each with 5,079 trips, and Thursday with 5,003 trips."
                ], style={"padding-left": "20px", "font-size": "18px", "margin-bottom": "4px", "list-style-type": "none"}),
                html.Li([
                    "Reasons for delays in train journeys include ", html.B("bad weather conditions"), ", technical issues, signal failures, staff shortages, and traffic. These factors can disrupt the normal operation of train services and lead to delays in arrivals or departures."
                ], style={"padding-left": "20px", "font-size": "18px", "margin-bottom": "4px", "list-style-type": "none"})
            ])
        ])
    ]
)
               
           ]

) 

