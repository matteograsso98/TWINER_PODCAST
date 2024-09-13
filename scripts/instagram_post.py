
import requests
from PIL import Image, ImageDraw, ImageFont
import textwrap

#STEP 1 - LOOK FOR TENNIS NEWS FROM newsAPI
def fetch_tennis_news(api_key):
    url = f'https://newsapi.org/v2/everything?q=tennis OR "davis cup" OR "US Open" OR "Sinner"&from=2024-09-6&to=2024-09-13&language=it&apiKey={api_key}'
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
    articles = news.get('articles', [])
    return articles[:3]

#STEP 2 
#colors of the podcast: 
#Lime Green (#A8E44C) – Primary color to evoke the excitement of tennis.
#Royal Blue (#1D3AB8) – For a professional look and to relate to the sport.
#Sunset Orange (#FF6E1F) – For warmth and energy.
#White (#FFFFFF) 
#Light Gray (#D1D1D1) – For balance and background.

def update_template(articles):
    # Create a blank image for the template
    image_width, image_height = 1024, 1024
    template = Image.new('RGB', (image_width, image_height), color='#1D3AB8')
    # Create a drawing context
    draw = ImageDraw.Draw(template)

    # Load font (make sure you have a TTF file, you can download free fonts from Google Fonts)
    # Load font (make sure you have a TTF file, you can download free fonts from Google Fonts)
    font_path_title = "Poppins/Poppins-Bold.ttf"
    font_path_text = "Poppins/Poppins-regular.ttf"  
    font_title = ImageFont.truetype(font_path_title, 86)
    font_text = ImageFont.truetype(font_path_text, 15)

    # Define colors
    title_color = '#D1D1D1' # Dlight grey 
    text_color = '#FFFFFF' # white

    # Add a title to the template (e.g., "Tennis News")
    draw.text((50, 50), "Tennis News", font=font_title, fill=title_color)

    # Dynamically add articles
    y_position = 150
    for article in articles:
        headline = article['title'] or "No title available"
        description = article['description'] or "No description available"

        # Wrap the title and description text to fit within the image (e.g., 40 characters per line)
        wrapped_title = textwrap.fill(headline, width=40)
        wrapped_description = textwrap.fill(description, width=50)

        # Draw the wrapped text on the image
        draw.text((50, y_position), wrapped_title, font=font_text, fill=text_color)
        y_position += 80  # Adjust spacing between title and description
        draw.text((50, y_position), wrapped_description, font=font_text, fill=text_color)
        y_position += 150  # Adjust spacing between articles
    
    #Save the final image
    template.save("tennis_news_post.png")
    print("Template updated and saved as tennis_news_post.png")

# Main Program
if __name__ == "__main__":
    # Replace with your NewsAPI key
    api_key = 'c937b62b20b04efb8eac3618743a0f85'
    #Fetch tennis news
    articles = fetch_tennis_news(api_key)
    # Update the template with fetched news
    update_template(articles)
