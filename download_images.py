import requests

url = "https://cdn.britannica.com/39/7139-050-A88818BB/Himalayan-chocolate-point.jpg"

response = requests.get(url)
with open("image.jpg", "wb") as file:
    file.write(response.content)
