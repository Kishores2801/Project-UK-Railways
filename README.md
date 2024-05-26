# UK Train Traveling Web Dashboard

This interactive web dashboard is designed to explore traveler behavior and operational performance in UK Railways.

## Packages Used

- **Dash**: Main framework for building the web application.
- **dash-core-components (dcc)**: Components library for building interactive user interfaces.
- **dash-html-components (html)**: Components library for creating HTML elements.
- **dash.dependencies**: Module for defining input and output components in Dash callbacks.
- **pandas (pd)**: Library for data manipulation and analysis.
- **plotly.express (px)**: High-level interface for creating interactive plots with Plotly.
- **folium**: Library for creating interactive maps.


## Select Departure and Arrival Stations

### Departure Station:
Select the Departure Station using the dropdown menu.

### Arrival Station:
Select the Arrival Station using the dropdown menu.

### Day of the Week:
Choose the day of the week for analysis.

## Dashboard Sections

### Map Section
This section displays a map showing the selected departure and arrival stations, along with information about the trip.

### Charts
The dashboard includes various charts to visualize different aspects of train travel data.

- **Line Chart 1:** Ticket Price Paid for the selected route over time.
- **Line Chart 2:** Actual Ticket Price vs Discount for the selected route over time.
- **Bar Chart 1:** Active Hours in the departure station.
- **Sunburst Chart 1:** Distribution of Purchases by Type, Payment Method, and Journey Status.
- **Sunburst Chart 2:** Distribution of Hours by Journey Status.
- **Pie Chart 1:** Journey Status for the selected route.
- **Pie Chart 2:** Reason for delay from the selected departure to arrival.
- **Pie Chart 3:** Ticket Class distribution for the selected route.
- **Bar Chart 2:** Payment Method for the selected route.
- **Bar Chart 3:** Ticket Type for the selected route.
- **Bar Chart 4:** Refund Request for the selected route.

## Usage
To use the dashboard, simply select the desired options from the dropdown menus and observe the visualizations and insights generated based on the selected criteria.

## Hosting
The web dashboard is hosted on Render, a cloud platform that provides an easy and efficient way to deploy web applications.




