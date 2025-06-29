def analyze_sentiment(articles):
    scores = {}
    for article in articles:
        source = article["source"]["name"]
        scores[source] = scores.get(source, 0) + 1
    return scores