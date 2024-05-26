# Loading python Libraries
import pandas as pd # loading the Dataframe
import numpy as np # loading the numpy library
import folium # mapping libraries
import streamlit as st
import streamlit.components.v1 as components
import warnings
import plotly.express as px
import plotly.graph_objects as go
warnings.filterwarnings("ignore")
st.set_page_config(page_title="UK Train Web Dashboard",layout="wide")



# Creating a Streamlit app
st.title("UK Train Traveling Web Dashboard")
st.markdown("This is an Exploratory Web Dashboard to analyze Traveler behavior and Operating performance.")


maintab1, maintab2 = st.tabs(["Web Dashboard", "Prediction"])


# ============================================= Train Dashboard ================================================== #

with maintab1:
    st.header("UK Train Web Dashboard")

    # Loading the Dataset
    data = pd.read_csv("Data/Uk-Train Data.csv")
    # Order of Chart
    weekday_order = ["All","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # columns 3
    col1, col2, col3 = st.columns(3)
    with col1:
        # Creating a dropdown Departure Station
        departure_station = st.selectbox("Select the Departure Station", data["Departure Station"].unique())
    
    with col2:
        # Creating a dropdown arrival Station
        data_filtered = data[data["Departure Station"]==departure_station]
        arrival_station = st.selectbox("Select the Arrival Station", data_filtered["Arrival Destination"].unique())
    
    with col3:
        # Creating a Dropdown for weekday order
        weekday = st.selectbox("Select the Weekday", weekday_order)


    # filtered data
    if weekday == "All":
        data_filtered = data_filtered[(data_filtered["Arrival Destination"]==arrival_station)]
    else:
        data_filtered = data_filtered[(data_filtered["Arrival Destination"]==arrival_station) & (data_filtered["Day of week"]==weekday)]

    
    col1, col2 =st.columns(2)

    with col1:
    # Mapping file
        first_row = data_filtered.iloc[0]
        departure_coords = [first_row["Departure Latitude"], first_row["Departure Longitude"]]
        arrival_coords = [first_row["Arrival Latitude"], first_row["Arrival Longitude"]]
        travel_distance = first_row["Distance"].astype(int)
        coordinates = [51.5072, 0.1276]
        site_map = folium.Map(location=coordinates, prefer_canvas=True,  zoom_start=6, min_zoom=6, max_zoom=6)
        # Coordinates Data
        folium.Marker(departure_coords, popup=departure_station, icon=folium.Icon(color='red')).add_to(site_map)
        folium.Marker(arrival_coords, popup=arrival_station, icon=folium.Icon(color='green')).add_to(site_map)
        # Add polyline for the route
        folium.PolyLine(locations=[departure_coords, arrival_coords], popup=f"Estimated Distance Covered: {travel_distance} km", weight=3).add_to(site_map)
        # Convert the map to HTML
        map_html = site_map._repr_html_()
        
        # HTML styling for the map container
        styled_html = f"""
        <div style='border: 2px solid #ccc; border-radius: 10px; overflow: hidden; padding-bottom: 60%; '>
            {map_html}
        </div>
        """

        # Render the HTML with components.html
        components.html(styled_html, height=600)


    with col2:
        no_of_travel = data_filtered["Transaction ID"].count()
        average_spend = data_filtered["Price"].mean()
        refunded = data_filtered[data_filtered["Refund Request"]=="Yes"]["Refund Request"].count()
        On_time = data_filtered[data_filtered["Journey Status"]=="On Time"]["Journey Status"].count()
        Delayed = data_filtered[data_filtered["Journey Status"]=="Delayed"]["Journey Status"].count()
        Cancelled = data_filtered[data_filtered["Journey Status"]=="Cancelled"]["Journey Status"].count()
        first_class = data_filtered[data_filtered["Ticket Class"]=="First Class"]["Ticket Class"].count()
        standard = data_filtered[data_filtered["Ticket Class"]=="Standard"]["Ticket Class"].count()



        # Centering the text using HTML
        # Centering the text with adjusted font size using HTML and CSS
        st.markdown(f"""
    <style>
        /* Media query for screens smaller than 600px */
        @media only screen and (max-width: 600px) {{
            .trip-overview-container {{
                display: flex;
                flex-direction: column;
                gap: 10px;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 10px;
                width: 100%;
            }}
            .trip-overview-container div {{
                text-align: left;
                font-size: 18px;
            }}
            .trip-overview-container div.title {{
                font-size: 24px;
                font-weight: bold;
            }}
        }}
        /* Default styles */
        .trip-overview-container {{
            display: flex;
            flex-direction: column;
            gap: 13px;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
        }}
        .trip-overview-container div {{
            text-align: left;
            font-size: 24px;
        }}
        .trip-overview-container div.title {{
            font-size: 36px;
            font-weight: bold;
        }}
    </style>
    <div class="trip-overview-container">
        <div class="title">Trip Overview</div>
        <div><b>Departure Destination:</b> {departure_station} Station</div>
        <div><b>Arrival Destination:</b> {arrival_station} Station</div> 
        <div><b>Distance Covered:</b> {travel_distance} Km</div>
        <div><b>Number of Passengers Traveled:</b> {no_of_travel}</div>
        <div><b>Average Spend Per Travel:</b> £{average_spend:.2f}</div>
        <div><b>On Time Journey:</b> {On_time}</div>
        <div><b>Delayed Journey:</b> {Delayed}</div>
        <div><b>Cancelled Journey:</b> {Cancelled}</div>
        <div><b>Ticket Classes:</b> {first_class} First Class, {standard} Standard Passengers</div>
        <div><b>Number of Refund Requests:</b> {refunded}</div>
    </div>
    <br/>
""", unsafe_allow_html=True)
        

        
    
    s = f"<p style='font-size:22px;'>The markers on the map identify stations by their latitude and longitude coordinates. The red marker denotes the departure station, while the green marker signifies the arrival destination. The line connecting these markers represents a potential route, with the distance estimated based on the approximate distance between two points on Earth's surface. For instance, the estimated distance between {departure_station} and {arrival_station} is {travel_distance} km.</p>"
    st.markdown(s, unsafe_allow_html=True)
    ### Second Row
    col1, col2 = st.columns(2)
    data_filtered1 = data[data["Departure Station"] == departure_station]
    data_filtered2 = data_filtered1[data_filtered1["Arrival Destination"] == arrival_station]

    # Calculate cumulative sum for 'Price' column
    grouped_data_price = data_filtered2.groupby('Date of Purchase')['Price'].sum().cumsum().reset_index()

    # Column 1
    with col1:
        fig = px.line(grouped_data_price, x="Date of Purchase", y="Price", title=f"Ticket Price Paid for {departure_station} to {arrival_station}")
        fig.update_yaxes(range=[0, max(grouped_data_price['Price']) * 1.2])
        fig.update_layout(
            xaxis_title="Date of Purchase",
            yaxis_title="Ticket Price Paid (£)",
            title_x=0.25,
            title_y=0.9,
            title_font_size=24,
            font_size=14,
            width=800,  # Set the width of the figure
            height=700,  # Set the height of the figure
        )
        st.plotly_chart(fig, use_container_width=True)

    # Column 2
    with col2:
        data_filtered2 = data_filtered2.sort_values(by="Date of Purchase")

        # Calculate cumulative sum for 'Actual Price' and 'Discount' columns
        grouped_data_cumsum = data_filtered2.groupby('Date of Purchase')[['Actual Price', 'Discount']].sum().cumsum().reset_index()
        grouped_data_cumsum = grouped_data_cumsum.reset_index()

        fig = px.line(grouped_data_cumsum, x="Date of Purchase", y=["Actual Price", "Discount"],
                    title=f"Actual Ticket Price vs Discount for {departure_station} to {arrival_station}",
                    labels={"value": "Amount in £", "variable": "Metrics", "Date of Purchase": "Date"},
                    )
        fig.update_yaxes(range=[0, max(grouped_data_cumsum['Actual Price']) * 1.2])
        fig.update_layout(
            title_x=0.13,
            title_y=0.9,
            title_font_size=24,
            font_size=14,
            width=800,  # Set the width of the figure
            height=700,  # Set the height of the figure
        )
        st.plotly_chart(fig, use_container_width=True)




    s = f"<p style='font-size:22px;'>These charts shows a cumulative sum of Actual Price, Discounted Price and Paid Price over the period of time. We calculated the Actual price of Tickets after reverting discounts made for railcards and Advance or Off Peak Ticket Type, Discounts calculated after deducting Actual price to Final price.</p>"
    st.markdown(s, unsafe_allow_html=True)
    # Third Row
    # Bar Chart for Peak Hours
    g1 = data_filtered1.groupby("Day of week")["Hour"].value_counts().reset_index()

    fig = px.bar(g1, x="Hour", y="count", title=f"Active Hours in {departure_station} station")
    fig.update_xaxes(range=[0, 23],showticklabels=True)
    fig.update_layout(
        xaxis_title="Hours",
        yaxis_title="Count of Travelers",
        title_x=0.4,
        title_y=0.9,
        title_font_size=24,
        font_size=14,
        width=800,
        height=700
    )
    st.plotly_chart(fig, use_container_width=True)

    
    s = f"<p style='font-size:22px;'>This chart illustrates the peak hours at each departure station based on departure times. A common trend observed in railway stations indicates a significant increase in passenger numbers around 8:00 AM, followed by a second surge around 8:00 PM, reflecting a 12-hour cycle.<br> 
            Manchester Piccadilly is the Most busiest Train Station</p>"
    st.markdown(s, unsafe_allow_html=True)
    



    # Fourth Row
    col1, col2, col3 = st.columns(3)

    with col1:
        g6 =  data_filtered.groupby("Journey Status")["Journey Status"].value_counts().reset_index()
        if not g6.empty:
            fig = px.pie(g6, values='count', names="Journey Status", title=f"Journey Status for {departure_station} to {arrival_station}", hole=0.5)
            fig.update_layout(
                title_x=0.2,
                title_y=0.95,
                title_font_size=20,
                width=600,
                height=600
            )
            st.plotly_chart(fig, use_container_width=True)

    with col2:
        g7 =  data_filtered.groupby("Reason for Delay")["Reason for Delay"].value_counts().reset_index()
        if not g7.empty:
            fig = px.pie(g7, values='count', names="Reason for Delay", title=f"Reason for Delay from {departure_station} to {arrival_station}", hole=0.5)
            fig.update_layout(
                title_x=0.2,
                title_y=0.95,
                title_font_size=20,
                width=600,
                height=600
            )
            st.plotly_chart(fig, use_container_width=True)

    with col3:
        g7 =  data_filtered.groupby("Refund Request")["Refund Request"].value_counts().reset_index()
        if not g7.empty:
            fig = px.pie(g7, values='count', names="Refund Request", title=f"Refund Requested on Journey from {departure_station} to {arrival_station}", hole=0.5)
            fig.update_layout(
                title_x=0.2,
                title_y=0.95,
                title_font_size=20,
                width=600,
                height=600
            )
            st.plotly_chart(fig, use_container_width=True)

    # Fifth Row
    col1, col2, col3, col4= st.columns(4)

    with col1:
        g2 =  data_filtered.groupby("Purchase Type")["Purchase Type"].value_counts().reset_index()
        if not g2.empty:
            fig = px.pie(g2, values='count', names="Purchase Type", title="Method of Ticket Purchase", hole=0.5)
            fig.update_layout(
                title_x=0.2,
                title_y=0.95,
                title_font_size=20,
                width=600,
                height=600
            )
            st.plotly_chart(fig, use_container_width=True)

    with col2:
        g3 =  data_filtered.groupby("Payment Method")["Payment Method"].value_counts().reset_index()
        if not g3.empty:
            fig = px.pie(g3, values='count', names="Payment Method", title="Payment Method for Ticket Purchase", hole=0.5)
            fig.update_layout(
                title_x=0.2,
                title_y=0.95,
                title_font_size=20,
                width=600,
                height=600
            )
            st.plotly_chart(fig, use_container_width=True)

    with col3:
        g4 =  data_filtered.groupby("Railcard")["Railcard"].value_counts().reset_index()
        if not g4.empty:
            fig = px.pie(g4, values='count', names="Railcard", title="Railcard Usage for Ticket Purchase", hole=0.5)
            fig.update_layout(
                title_x=0.2,
                title_y=0.95,
                title_font_size=20,
                width=600,
                height=600
            )
            st.plotly_chart(fig, use_container_width=True)

    with col4:
        g5 =  data_filtered.groupby("Ticket Type")["Ticket Type"].value_counts().reset_index()
        if not g5.empty:
            fig = px.pie(g5, values='count', names="Ticket Type", title="Railcard Usage for Ticket Purchase", hole=0.5)
            fig.update_layout(
                title_x=0.2,
                title_y=0.95,
                title_font_size=20,
                width=600,
                height=600
            )
            st.plotly_chart(fig, use_container_width=True)









# ============================================= Prediction ================================================== #

with maintab2:
    st.header("UK Train Prediction")
    st.write("bidsjcbkcdnk")



