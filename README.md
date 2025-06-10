# Advista 📰🤖

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Gemini AI](https://img.shields.io/badge/AI-Google%20Gemini-red.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

**Advista** is an intelligent news analysis and marketing intelligence tool that combines web scraping, sentiment analysis, and AI-powered keyword extraction to provide actionable insights for businesses and marketers.

## 🚀 Overview

Advista automatically fetches the latest news headlines for any company, analyzes the sentiment of the coverage, and generates relevant marketing keywords using Google's Gemini AI. This powerful combination helps businesses understand their media presence and discover new marketing opportunities.

## ✨ Key Features

- 🔍 **Smart Web Scraping**: Fetches latest news headlines from Bing News with anti-detection measures
- 📊 **Sentiment Analysis**: Uses VADER SentimentIntensityAnalyzer for accurate sentiment scoring
- 🤖 **AI-Powered Insights**: Leverages Google Gemini AI for intelligent keyword extraction
- 📈 **Marketing Intelligence**: Generates actionable marketing keywords from news content
- 💾 **Data Export**: Saves comprehensive results in CSV format for further analysis
- 🛡️ **Robust Scraping**: Implements random User-Agents and error handling

## 🎯 Use Cases

- **Brand Monitoring**: Track sentiment around your company in the news
- **Competitive Analysis**: Monitor competitor news and sentiment trends
- **Marketing Research**: Discover trending keywords and topics in your industry
- **PR Analytics**: Measure the impact of press releases and media coverage
- **Content Strategy**: Identify relevant topics and keywords for content creation
- **Investment Research**: Analyze news sentiment for investment decisions

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- Google Gemini API key
- Stable internet connection

### Setup Instructions

1. **Clone the repository**:
```bash
git clone https://github.com/debraj-m/Advista.git
cd Advista
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Set up Google Gemini API**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create an API key
   - Replace `GEMINI_API_KEY` in the script with your actual API key

## 📦 Dependencies

The project uses the following Python packages:

```
requests>=2.28.0          # HTTP requests and web scraping
pandas>=1.3.0             # Data manipulation and analysis
beautifulsoup4>=4.11.0    # HTML parsing and web scraping
vaderSentiment>=3.3.2     # Sentiment analysis
google-generativeai>=0.3.0  # Google Gemini AI integration
```

## 🚀 Quick Start

### Basic Usage

```bash
python main.py
```

When prompted, enter the company name you want to analyze:

```
Enter company name: Tesla
```

### Example Output

```
Enter company name: Swiggy
Fetching news and analyzing sentiment & keywords for Swiggy...
🔍 Generating marketing keywords using Gemini AI...
🚀 Suggested Marketing Keywords for Swiggy: food delivery, expansion, revenue growth, new partnership
✅ Data saved to company_headlines_with_keywords.csv
✅ Scraping, sentiment analysis, and keyword extraction complete!
```

## 📊 Output Format

### Terminal Output
- Real-time progress updates
- Generated marketing keywords
- Success/error messages

### CSV Export
The generated CSV file contains:

| Column | Description |
|--------|-------------|
| `headline` | News headline text |
| `sentiment_score` | VADER compound sentiment score (-1 to 1) |
| `sentiment_label` | Classified sentiment (Positive/Negative/Neutral) |
| `keywords` | AI-generated marketing keywords |
| `timestamp` | When the analysis was performed |
| `source` | News source (if available) |

## 🔧 Advanced Configuration

### Custom API Configuration

```python
import google.generativeai as genai

# Configure Gemini AI
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel('gemini-pro')
```

### Sentiment Analysis Thresholds

The sentiment classification uses the following thresholds:
- **Positive**: compound score ≥ 0.05
- **Negative**: compound score ≤ -0.05
- **Neutral**: -0.05 < compound score < 0.05

### Scraping Configuration

```python
# User agents for web scraping
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
    # Add more user agents as needed
]
```

## 📈 Sample Analysis Results

### Sentiment Distribution Example
```
Company: Tesla
Total Headlines Analyzed: 25
Positive Sentiment: 60% (15 headlines)
Neutral Sentiment: 24% (6 headlines)
Negative Sentiment: 16% (4 headlines)
Average Sentiment Score: 0.23
```

### Generated Keywords Example
```
Tesla Marketing Keywords:
- electric vehicles
- autonomous driving
- sustainability
- innovation
- stock performance
- market expansion
- technology advancement
```

## 🛡️ Features & Technical Details

### Web Scraping
- **Anti-Detection**: Random User-Agent rotation
- **Error Handling**: Robust exception handling for network issues
- **Rate Limiting**: Built-in delays to respect server resources
- **Multiple Sources**: Extensible to add more news sources

### Sentiment Analysis
- **VADER Algorithm**: Specifically tuned for social media text
- **Lexicon-Based**: Rule-based approach with sentiment intensity
- **Context Awareness**: Handles punctuation, capitalization, and emoticons
- **Real-time Processing**: Fast analysis suitable for large datasets

### AI Integration
- **Google Gemini**: State-of-the-art language model
- **Contextual Understanding**: Generates relevant marketing keywords
- **Customizable Prompts**: Easily modify AI instructions
- **Error Recovery**: Graceful handling of API limitations

## 🔒 Security & Privacy

- **API Key Protection**: Store API keys in environment variables
- **Data Privacy**: No personal data collection
- **Ethical Scraping**: Respects robots.txt and rate limits
- **Local Processing**: All analysis performed locally

## 🧪 Testing

### Running Tests

```bash
# Test with sample data
python test_advista.py

# Test API connectivity
python test_gemini_api.py
```

### Manual Testing

```python
# Test sentiment analysis
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
score = analyzer.polarity_scores("Great quarterly results!")
print(score)  # {'compound': 0.6249, 'pos': 0.778, 'neu': 0.222, 'neg': 0.0}
```

## 🚀 Deployment Options

### Local Development
```bash
python main.py
```

### Scheduled Analysis
```bash
# Add to crontab for daily analysis
0 9 * * * cd /path/to/advista && python main.py < company_list.txt
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

## 🔄 Future Enhancements

### Planned Features
- [ ] **Multi-Source Scraping**: Google News, Reddit, Twitter integration
- [ ] **Historical Analysis**: Trend analysis over time
- [ ] **Visualization Dashboard**: Interactive charts and graphs
- [ ] **API Interface**: RESTful API for programmatic access
- [ ] **Real-time Monitoring**: Live news feed processing
- [ ] **Custom Models**: Fine-tuned sentiment models for specific industries
- [ ] **Competitor Comparison**: Side-by-side analysis of multiple companies
- [ ] **Alert System**: Notifications for significant sentiment changes

### Technical Improvements
- [ ] **Database Integration**: PostgreSQL/MongoDB for data persistence
- [ ] **Caching System**: Redis for improved performance
- [ ] **Async Processing**: Faster concurrent news fetching
- [ ] **Configuration Files**: YAML/JSON configuration management
- [ ] **Logging System**: Comprehensive logging and monitoring
- [ ] **Unit Tests**: Complete test coverage

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Getting Started
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Update documentation
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add docstrings to new functions
- Include unit tests for new features
- Update README for significant changes

### Areas for Contribution
- Additional news sources integration
- Improved sentiment analysis models
- Data visualization features
- Performance optimizations
- Documentation improvements

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

- **Ethical Usage**: This tool is for legitimate business intelligence purposes
- **Rate Limiting**: Respect website terms of service and rate limits
- **API Costs**: Google Gemini API usage may incur costs
- **Data Accuracy**: News sentiment may not reflect actual business performance
- **Legal Compliance**: Ensure compliance with local data protection laws

## 📚 Resources

### Documentation
- [VADER Sentiment Analysis](https://github.com/cjhutto/vaderSentiment)
- [Google Gemini AI Documentation](https://ai.google.dev/docs)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

### Tutorials
- [Web Scraping Best Practices](https://blog.apify.com/web-scraping-best-practices/)
- [Sentiment Analysis Guide](https://monkeylearn.com/sentiment-analysis/)
- [Marketing Intelligence with AI](https://www.marketingevolution.com/marketing-essentials/marketing-intelligence)

## 🙏 Acknowledgments

- **VADER Sentiment**: C.J. Hutto for the excellent sentiment analysis tool
- **Google AI**: For providing access to Gemini AI capabilities
- **Open Source Community**: For the amazing libraries and tools
- **Beta Testers**: For feedback and suggestions

## 📞 Contact & Support

- **Author**: [Debraj M](https://github.com/debraj-m)
- **Project Link**: [https://github.com/debraj-m/Advista](https://github.com/debraj-m/Advista)
- **Issues**: [GitHub Issues](https://github.com/debraj-m/Advista/issues)
- **Discussions**: [GitHub Discussions](https://github.com/debraj-m/Advista/discussions)

---

**📈 Turn News into Actionable Marketing Intelligence with Advista!**

*If this project helped you gain valuable insights, please consider giving it a ⭐!*
