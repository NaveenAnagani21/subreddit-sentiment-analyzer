import nltk
import nltk.sentiment.vader as vader
from scrape import get_comments
import pandas as pd

# Function to analyze sentiment of a comment
def analyze_sentiment(comment_text):
  # Download necessary resources for sentiment analysis (one-time)
  nltk.download('vader_lexicon')
  sentiment_analyzer = vader.SentimentIntensityAnalyzer()
  sentiment = sentiment_analyzer.polarity_scores(comment_text)
  return sentiment['compound']  # Get overall sentiment score


subreddit_names = ['aitah','mildlyinfuriating']
rating=[]


for subreddit_name in subreddit_names:
    print(subreddit_name)
    cnt=0
    for comment in get_comments(subreddit_name):
    # Process comment text (e.g., remove irrelevant characters)
        if cnt==10:
           break
        cnt+=1
        comment_text = comment.body.replace('\n', ' ')  # Replace newlines with spaces

    # Analyze sentiment
        sentiment_score = analyze_sentiment(comment_text)

    # Update mood statistics based on sentiment score (positive, negative, neutral)
    # ... your logic to track mood ...

    # Optionally, print results for debugging/monitoring
        rating.append([subreddit_name,comment_text,sentiment_score])
        print(f' subrredit_name:{subreddit_name} Comment: {comment_text[:50]} Sentiment: {sentiment_score}')
df=pd.DataFrame(rating, columns=['subreddit_name', 'comment', 'sentiment_score'])



