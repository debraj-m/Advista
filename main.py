import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import google.generativeai as genai
import time
import random

# Replace with your Gemini API key
GEMINI_API_KEY = "Enter your Gemini API key here"

# Initialize Google Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

# Initialize Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# List of User-Agents to avoid detection
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.110 Safari/537.36"
]

def get_keywords_gemini(headlines):
    """Uses Gemini API to generate marketing keywords based on headlines."""
    if not headlines:
        return "No headlines found"

    prompt = f"""
    You are a marketing expert. Extract the most relevant and trending marketing keywords 
    from the following news headlines about a company. Provide keywords in a comma-separated list.

    Headlines:
    {headlines}
    
    Example Output:
    quick commerce, stock decline, market growth, new acquisition
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"❌ Gemini API Error: {e}")
        return "Error generating keywords"

def get_news(company):
    """Fetches news headlines for a given company using Bing News."""
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    search_url = f"https://www.bing.com/news/search?q={company}+news"

    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"❌ Bing News Fetch Error: {e}")
        return [], "No keywords generated"

    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.select("a.title")  # Bing News headline selector

    news_data = []
    all_headlines = []

    if not articles:
        print("⚠️ No news articles found!")
        return [], "No headlines found"

    for article in articles[:10]:  # Get the first 10 headlines
        title = article.text.strip()
        link = article['href']

        # Get sentiment score
        sentiment_score = analyzer.polarity_scores(title)['compound']
        
        # Classify sentiment
        if sentiment_score >= 0.05:
            sentiment = "Positive"
        elif sentiment_score <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        all_headlines.append(title)

        news_data.append({
            'Company': company,
            'Headline': title,
            'Sentiment': sentiment,
            'Sentiment Score': sentiment_score,
            'URL': link,
            'Date': datetime.today().strftime('%Y-%m-%d')
        })

    # Generate marketing keywords using Gemini
    print("🔍 Generating marketing keywords using Gemini AI...")
    marketing_keywords = get_keywords_gemini("\n".join(all_headlines))

    return news_data, marketing_keywords

def save_to_csv(data, marketing_keywords, filename="company_headlines_with_keywords.csv"):
    """Saves the scraped data to a CSV file with sentiment analysis and extracted keywords."""
    df = pd.DataFrame(data)
    
    # Add a new column for extracted marketing keywords
    df["Marketing Keywords"] = marketing_keywords

    df.to_csv(filename, index=False)
    print(f"✅ Data saved to {filename}")

if __name__ == "__main__":
    company_name = input("Enter company name: ")  # Example: 'Swiggy'
    print(f"Fetching news and analyzing sentiment & keywords for {company_name}...")
    
    news_data, marketing_keywords = get_news(company_name)
    
    print(f"🚀 Suggested Marketing Keywords for {company_name}: {marketing_keywords}")
    
    save_to_csv(news_data, marketing_keywords)

    print("✅ Scraping, sentiment analysis, and keyword extraction complete!")
