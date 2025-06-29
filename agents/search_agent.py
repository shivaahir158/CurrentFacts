import requests
from config import NEWS_API_KEY

def search_news(claim):
    url = "https://newsapi.org/v2/everything"
    params = {"q": claim, "language": "en", "apiKey": NEWS_API_KEY}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("articles", [])
    return []