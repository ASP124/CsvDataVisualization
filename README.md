# Data Analysis Project

## Overview

This Django-based web application allows users to upload CSV files, perform data analysis, and visualize the results. The application utilizes popular libraries such as `pandas` for data manipulation and `seaborn` for creating visualizations.

## Features

- **File Upload**: Upload CSV files for analysis.
- **Data Analysis**: Automatically handle missing values and provide basic data statistics.
- **Visualizations**: Generate and display histograms for numerical columns in the dataset.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

## Setup Instructions

1. **Clone the Repository:**

   - git clone {repository-url}
   - cd {repository-directory}

2. **Install Dependencies:**
    pip install -r requirements.txt

3. **Apply Migrations:**
    python manage.py migrate

4. **Run the Development Server:**
    python manage.py runserver

5. **Access the Application:**
    Open your web browser and go to http://127.0.0.1:8000/ to use the application.

## Usage
**Upload Data File:** Navigate to the homepage and upload a CSV file using the provided form.
**View Results:** After uploading, you will be redirected to a results page showing basic statistics and a preview of the data.
**Visualizations:** Click on the “View Visualizations” button to see generated histograms for the numerical columns in your dataset.
