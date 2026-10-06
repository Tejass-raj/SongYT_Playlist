import requests
from bs4 import BeautifulSoup

# Ask the user for a date
date = input("Which year do you want to travel to? Type the date in YYYY-MM-DD format: ")

# Build the URL using the Bakeboard tutorial site
URL = f"https://appbrewery.github.io/bakeboard-hot-100/{date}/"

# Include a User-Agent header so the server doesn't block the request
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}

# Make the HTTP request
response = requests.get(URL, headers=header)

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Scrape the top 100 song titles
# Billboard/Bakeboard stores song titles in <h3> tags with a specific class
song_names_spans = soup.select("li ul li h3")

song_names = [song.getText().strip() for song in song_names_spans]

# Print results
print(f"\nTop 100 songs on {date}:\n")
for i, song in enumerate(song_names, start=1):
    print(f"{i}. {song}")