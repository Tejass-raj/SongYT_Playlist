# 🎵 Billboard Top 100 Songs Web Scraper

A Python web scraping project that allows you to enter a specific date and retrieve the **Top 100 songs** from the Billboard/Bakeboard Hot 100 chart for that date.

The project uses **Requests** to access the webpage and **BeautifulSoup** to parse the HTML and extract the song titles. The results are then displayed in the terminal along with their rankings.

---

## 📖 About the Project

Music charts change every week, with different songs moving up and down the rankings over time.

This project was created to practice **web scraping with Python** by building a simple program that can retrieve the Top 100 songs for a specific date.

The program asks the user to enter a date in the following format:

```text
YYYY-MM-DD
---


### 🎯 Project Objective
The main objective of this project is to understand how Python can be used to collect information from webpages and process the extracted data.
Through this project, I practiced:
- Taking user input
- Working with dates as strings
- Creating dynamic URLs
- Sending HTTP requests
- Using request headers
- Parsing HTML using BeautifulSoup
- Selecting elements using CSS selectors
- Extracting text from HTML elements
- Using list comprehensions

---

✨ Features
- 🎵 Fetches Top 100 songs for a selected date
- 📅 Takes the date from the user
- 🌐 Creates a dynamic webpage URL based on the date
- 🕸️ Uses web scraping to collect song titles
- 🥣 Uses BeautifulSoup for HTML parsing
- 🔎 Uses CSS selectors to locate song elements
- 🛡️ Includes a User-Agent header in the request
- 📋 Displays songs with their rankings
- 💻 Simple command-line interface
- 🐍 Built completely with Python
- Using loops and enumerate()
- Displaying structured data in the terminal


Project Structure

Billboard-Top-100-Scraper/
│
├── main.py
│
└── README.md
