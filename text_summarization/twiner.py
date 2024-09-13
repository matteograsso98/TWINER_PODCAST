import requests


# STEP 1 - LOOK FOR TENNIS NEWS FROM newsAPI
def fetch_tennis_news(api_key):
    url = f'https://newsapi.org/v2/everything?q=tennis OR "davis cup" OR "US Open" OR "Sinner"&from=2024-09-6&to=2024-09-13&language=it&apiKey={API_KEY}'
    # to get more specific news, change the query q=tennis with, e.g., q=Sinner, q=US Open, etc.
    # You can modify the query to sort articles by:
    ######## Relevancy: Articles that match the search term most closely.
    ######## Popularity: Articles from popular sources and those shared frequently.
    ######## PublishedAt: The most recent articles first.
    #Examples: 
    #look at the most recent news first:
    #url = f'https://newsapi.org/v2/everything?q=tennis&sortBy=publishedAt&apiKey={API_KEY}'
    #Specify a date range:
    #url = f'https://newsapi.org/v2/everything?q=tennis&from=2024-09-01&to=2024-09-10&apiKey={API_KEY}'
    #Specify a language:
    #url = f'https://newsapi.org/v2/everything?q=tennis&language=en&apiKey={API_KEY}'
    #Specify the SOURCES (e.g., BBC Sport, ESPN, Ubitennis, etc.)
    #url = f'https://newsapi.org/v2/everything?q=tennis&sources=bbc-sport,espn&apiKey={API_KEY}'

    response = requests.get(url)
    news = response.json()
    #Create a set to store unique titles
    unique_titles = set()
    #Loop through the articles and print only unique ones
    for i, article in enumerate(news['articles'][:5], start=1):
        title = article['title']
    
        if title not in unique_titles:  # Check if title is already in the set
            unique_titles.add(title)  # Add the title to the set to track it
            return i, title, article['description'], article['url']
            #print(f"\nArticle {i}:")
            #print(f"Title: {title}")
            #print(f"Description: {article['description']}")
            #print(f"URL: {article['url']}")

API_KEY = 'c937b62b20b04efb8eac3618743a0f85'
fetch_tennis_news(API_KEY)
