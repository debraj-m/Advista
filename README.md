# Company News Scraper with Sentiment Analysis and Keyword Extraction

This project is a Python-based web scraper that fetches news headlines for a given company using Bing News. It then performs sentiment analysis on the headlines and extracts marketing-related keywords using Google's Gemini AI.

## Features
- **Web Scraping**: Fetches the latest news headlines from Bing News.
- **Sentiment Analysis**: Uses VADER SentimentIntensityAnalyzer to determine if headlines are positive, negative, or neutral.
- **AI-powered Keyword Extraction**: Uses Google Gemini API to generate relevant marketing keywords from news headlines.
- **CSV Export**: Saves the results in a CSV file including sentiment scores and extracted keywords.

## Requirements
Make sure you have Python installed, then install dependencies using:
```bash
pip install -r requirements.txt
```

### Dependencies
- `requests` - For making HTTP requests.
- `pandas` - For handling tabular data.
- `beautifulsoup4` - For parsing HTML content.
- `vaderSentiment` - For sentiment analysis.
- `google-generativeai` - For interacting with Google Gemini AI.

## Usage
1. **Set up your Gemini API Key**
   Replace `GEMINI_API_KEY` in the script with your actual API key from Google.

2. **Run the script**
   ```bash
   python main.py
   ```

3. **Enter the company name**
   The script will fetch and analyze news headlines for the given company.

4. **View results**
   - Suggested marketing keywords will be displayed in the terminal.
   - A CSV file (`company_headlines_with_keywords.csv`) will be generated with all extracted data.

## Example Output
```
Enter company name: Swiggy
Fetching news and analyzing sentiment & keywords for Swiggy...
🔍 Generating marketing keywords using Gemini AI...
🚀 Suggested Marketing Keywords for Swiggy: food delivery, expansion, revenue growth, new partnership
✅ Data saved to company_headlines_with_keywords.csv
✅ Scraping, sentiment analysis, and keyword extraction complete!
```

## Notes
- The script uses random User-Agents to avoid detection while scraping.
- Ensure your API key is valid to use the Google Gemini AI services.

## License
This project is open-source and free to use under the MIT License.

