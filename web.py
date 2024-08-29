import streamlit as st
import requests

# Todo lo relacionado al lin y la API KEY
apikey = "UffW3Sb7Ik5gHmbzNDiE9za8beliWMGnIWgMQdde"
url = f"https://api.nasa.gov/planetary/apod?api_key={apikey}"
r = requests.get(url)
content = r.json()
image_url = content["url"]
r2 = requests.get(image_url)
# Descargar la imagen y guardarlar
image_filepath = "img.png"
with open(image_filepath, "wb") as file:
    file.write(r2.content)
# Acomodar todo en streamlit
st.title(content["title"])
st.image(image_filepath)
st.write(content["explanation"])




