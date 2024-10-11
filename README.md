# NASA email sender

This project fetches the latest news articles from a specified category and downloads images related to the content using the News API and NASA's Astronomy Picture of the Day (APOD) API. It also features a simple web interface built with Streamlit to display the APOD content.
Features

    Fetch top news articles based on a specified category (e.g., business).
    Send a newsletter with article titles and descriptions.
    Download images from a given URL.
    Display NASA's Astronomy Picture of the Day on a web page with an explanation.

Prerequisites

Before running the application, ensure you have the following installed:

    Python 3.x
    requests library
    streamlit library

Installation

You can install the necessary Python libraries using pip:

bash

pip install requests streamlit

Files
1. main.py

This file contains the main functionality for fetching news articles and sending the newsletter.
Key Functions:

    Fetches top headlines based on a specified category from the News API.
    Constructs a message with article titles, descriptions, and URLs.
    Sends the constructed message via email (requires a separate send_email function).

2. download_images.py

This file contains functionality to download images from a specified URL.
Key Functions:

    Fetches an image from a given URL and saves it locally as image.jpg.

3. webpage.py

This file uses Streamlit to display the NASA Astronomy Picture of the Day.
Key Functions:

    Fetches the APOD content from NASA's API.
    Downloads the image and displays it on the Streamlit web app.
    Shows the title and explanation of the image.

Configuration

    API Keys:
        Replace api_key in main.py with your News API key.
        Replace apikey in webpage.py with your NASA API key.

    Email Sending:
        Ensure you have a function named send_email in a separate module named Email.py to handle email sending.

Running the Application
To Fetch News and Send Email

    Run the main script:

    bash

    python main.py

To Download an Image

    Run the download image script:

    bash

    python download_images.py

To Display NASA's Astronomy Picture of the Day

    Run the Streamlit app:

    bash

    streamlit run webpage.py

    Open your browser and go to the URL provided by Streamlit (usually http://localhost:8501).

Example Output

    The main script will generate an email newsletter with the latest news articles.
    The image download script will save an image as image.jpg in the current directory.
    The Streamlit app will display the Astronomy Picture of the Day along with its explanation.
