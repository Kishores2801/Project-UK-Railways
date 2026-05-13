# 🚂 UK Railways — Interactive Travel Analytics Dashboard

[![Python](https://img.shields.io/badge/Python-3.12.2-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Dash](https://img.shields.io/badge/Dash-2.17.0-008DE4?style=for-the-badge&logo=plotly&logoColor=white)](https://dash.plotly.com/)
[![Plotly](https://img.shields.io/badge/Plotly-5.22.0-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![GCP](https://img.shields.io/badge/Google_Cloud_Run-Deployed-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)](https://cloud.google.com/run)

> **An interactive web dashboard for exploring traveler behavior and operational performance across UK Railways — with route-level filtering, predictive analysis, and live deployment on Google Cloud Run.**

🌐 **Live Demo:** [https://dash-app-7iiwvq76yq-uc.a.run.app/](https://dash-app-7iiwvq76yq-uc.a.run.app/)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Dashboard Sections](#dashboard-sections)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Getting Started (Local)](#getting-started-local)
- [Docker Setup](#docker-setup)
- [Deployment on Google Cloud Run](#deployment-on-google-cloud-run)
- [Data](#data)
- [Analysis & Prediction](#analysis--prediction)
- [License](#license)

---

## 🧭 Overview

This project is a **full-stack data analytics dashboard** built with Python Dash and Plotly, designed to analyze UK Railways travel data. Users can interactively filter by **departure station**, **arrival station**, and **day of the week** to explore key metrics like:

- Ticket pricing trends over time
- Journey delay reasons and rates
- Passenger behavior (purchase type, payment method, ticket class)
- Station-level active hours
- Refund request patterns

The app is **containerized with Docker** and deployed on **Google Cloud Run** for scalable, serverless hosting.

---

## ✨ Features

- 🗺️ **Interactive Map** — Visualizes the selected departure and arrival stations geographically using Folium
- 📊 **11 Visualizations** — A rich set of charts (line, bar, sunburst, pie) covering all angles of rail travel data
- 🔍 **Dynamic Filtering** — Filter all charts simultaneously by route and day of week
- 📈 **Analysis & Prediction Notebooks** — Jupyter Notebooks for deeper EDA and ML-based delay prediction
- 🐳 **Dockerized** — Fully containerized for consistent local and cloud deployment
- ☁️ **Cloud-hosted** — Deployed on Google Cloud Run with public access

---

## 📊 Dashboard Sections

### 🎛️ Controls
| Filter | Description |
|---|---|
| **Departure Station** | Dropdown to select the origin station |
| **Arrival Station** | Dropdown to select the destination station |
| **Day of the Week** | Dropdown to filter by a specific day |

### 🗺️ Map Section
Displays the geographical route between selected departure and arrival stations with trip summary information.

### 📈 Charts

| # | Chart Type | Metric |
|---|---|---|
| 1 | **Line Chart** | Ticket Price Paid for the selected route over time |
| 2 | **Line Chart** | Actual Ticket Price vs Discount over time |
| 3 | **Bar Chart** | Active Hours at the departure station |
| 4 | **Sunburst Chart** | Distribution of Purchases by Type, Payment Method & Journey Status |
| 5 | **Sunburst Chart** | Distribution of Hours by Journey Status |
| 6 | **Pie Chart** | Journey Status breakdown for the selected route |
| 7 | **Pie Chart** | Reasons for Delay (departure → arrival) |
| 8 | **Pie Chart** | Ticket Class distribution for the selected route |
| 9 | **Bar Chart** | Payment Method breakdown |
| 10 | **Bar Chart** | Ticket Type breakdown |
| 11 | **Bar Chart** | Refund Requests for the selected route |

---

## 📁 Project Structure

```
Project-UK-Railways/
├── Analysis & Prediction/      # Jupyter Notebooks for EDA & ML prediction
├── Dashboard App/              # Main Dash application code
│   └── app.py                  # Entry point for the Dash web app
├── Data/                       # Raw and processed datasets
├── Other files/                # Supplementary files
├── assets/                     # Static assets (CSS, images)
├── Dockerfile                  # Docker container configuration
├── .dockerignore               # Files excluded from Docker build
├── requirements.txt            # Python dependencies
└── README.md
```

---

## 🛠️ Tech Stack

| Category | Technology | Version |
|---|---|---|
| **Language** | Python | 3.12.2 |
| **Web Framework** | Dash | 2.17.0 |
| **UI Components** | Dash Bootstrap Components | 1.6.0 |
| **UI Components** | Dash Mantine Components | 0.12.0 |
| **Icons** | Dash Iconify | 0.1.2 |
| **Visualization** | Plotly Express | 5.22.0 |
| **Mapping** | Folium | latest |
| **Data Manipulation** | Pandas | 2.2.2 |
| **Numerical Computing** | NumPy | 1.26.4 |
| **Containerization** | Docker | latest |
| **Cloud Hosting** | Google Cloud Run | managed |

---

## ✅ Prerequisites

- Python **3.12+**
- `pip` package manager
- Docker (for containerized setup)
- Google Cloud SDK `gcloud` (for deployment only)

---

## 🚀 Getting Started (Local)

### 1. Clone the Repository

```bash
git clone https://github.com/Kishores2801/Project-UK-Railways.git
cd Project-UK-Railways
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
cd "Dashboard App"
python app.py
```

Open your browser at **[http://localhost:8080](http://localhost:8080)** to view the dashboard.

---

## 🐳 Docker Setup

Build and run the app locally using Docker:

```bash
# Build the Docker image
docker build -t uk-railways-dash .

# Run the container
docker run -p 8080:8080 uk-railways-dash
```

Open **[http://localhost:8080](http://localhost:8080)** in your browser.

---

## ☁️ Deployment on Google Cloud Run

This project is deployed on **Google Cloud Run** using a containerized workflow. Follow these steps to deploy your own instance:

### Step 1 — Build & Push the Docker Image

```bash
docker build -t gcr.io/<YOUR_PROJECT_ID>/dash-app .
docker push gcr.io/<YOUR_PROJECT_ID>/dash-app
```

### Step 2 — Create a Service Account & Key

```bash
gcloud iam service-accounts keys create key.json \
  --iam-account <YOUR_SERVICE_ACCOUNT>@<YOUR_PROJECT_ID>.iam.gserviceaccount.com
```

### Step 3 — Grant Artifact Registry Permissions

```bash
gcloud projects add-iam-policy-binding <YOUR_PROJECT_ID> \
  --member="serviceAccount:<YOUR_SERVICE_ACCOUNT>@<YOUR_PROJECT_ID>.iam.gserviceaccount.com" \
  --role="roles/artifactregistry.writer"
```

### Step 4 — Deploy to Cloud Run

```bash
gcloud run deploy dash-app \
  --image gcr.io/<YOUR_PROJECT_ID>/dash-app \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

> ✅ Once deployed, Cloud Run will provide a public URL for your app.

---

## 📂 Data

The `Data/` directory contains the UK Railways travel dataset used to power the dashboard. It includes fields such as:

- Departure & Arrival Station
- Journey Date & Time
- Ticket Type & Class
- Ticket Price & Discounts
- Payment Method
- Journey Status (on time / delayed / cancelled)
- Delay Reason
- Refund Request Status

---

## 🔬 Analysis & Prediction

The `Analysis & Prediction/` folder contains **Jupyter Notebooks** covering:

- **Exploratory Data Analysis (EDA)** — Statistical summaries, distribution plots, and correlation analysis across travel features
- **Delay Prediction** — Machine learning models to predict journey delays based on route, time, and ticket attributes
- **Pricing Analysis** — Trends in ticket prices and discount patterns by route and ticket class

To run the notebooks:

```bash
pip install jupyter
jupyter notebook "Analysis & Prediction/"
```

---

## 📄 License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

<div align="center">

Built with 🐍 Python · 📊 Plotly Dash · ☁️ Google Cloud Run

**[🌐 View Live Dashboard](https://dash-app-7iiwvq76yq-uc.a.run.app/)**

</div>
