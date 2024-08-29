import requests
from Email import send_email

topic = "business"
api_key = "50b3073cb6704175b00a0bb9f2a8b494"
url = "https://newsapi.org/v2/top-headlines?" \
      "country=us" \
      f"&category={topic}&" \
      "apiKey=50b3073cb6704175b00a0bb9f2a8b494&" \
      "language=en"""
# Make a request
r = requests.get(url)

# Get a dictionary with data
content = r.json()
mensaje = ""
# Acces the article titles and description
for article in content["articles"][:20]:
    mensaje = "Subject: Newsletter" + "\n" +\
              mensaje + f"""{article["title"]}
      {article["description"]}""" \
              + "\n" + article["url"] + 2 * "\n"


send_email(mensaje)
