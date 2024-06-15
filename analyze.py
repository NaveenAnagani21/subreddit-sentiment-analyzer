import nltk
import nltk.sentiment.vader as vader
from scrape import get_comments

# Function to analyze sentiment of a comment
def analyze_sentiment(comment_text):
  # Download necessary resources for sentiment analysis (one-time)
  nltk.download('vader_lexicon')
  sentiment_analyzer = vader.SentimentIntensityAnalyzer()
  sentiment = sentiment_analyzer.polarity_scores(comment_text)
  return sentiment['compound']  # Get overall sentiment score


subreddit_name = 'developersindia'

for comment in get_comments(subreddit_name):
  # Process comment text (e.g., remove irrelevant characters)
  comment_text = comment.body.replace('\n', ' ')  # Replace newlines with spaces

  # Analyze sentiment
  sentiment_score = analyze_sentiment(comment_text)

  # Update mood statistics based on sentiment score (positive, negative, neutral)
  # ... your logic to track mood ...

  # Optionally, print results for debugging/monitoring
  print(f'Comment: {comment_text[:50]} Sentiment: {sentiment_score}')
