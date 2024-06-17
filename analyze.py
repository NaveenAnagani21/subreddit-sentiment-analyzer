import nltk
import nltk.sentiment.vader as vader
from scrape import get_comments
import pandas as pd
import emoji


# Function to analyze sentiment of a comment
def analyze_sentiment(comment_text):
    # Download necessary resources for sentiment analysis (one-time)
    nltk.download("vader_lexicon")
    sentiment_analyzer = vader.SentimentIntensityAnalyzer()
    sentiment = sentiment_analyzer.polarity_scores(comment_text)
    return sentiment["compound"]  # Get overall sentiment score


subreddit_names = ["aitah", "mildlyinfuriating",'depression', 'aww','developersindia','indianfashionaddicts', 'twoxindia','doomer','india']
rating = []

weary_face=emoji.emojize(':Weary Face:')

neutral_face=emoji.emojize(':Neutral Face:')
star_struck=emoji.emojize(':Star-Struck')

for subreddit_name in subreddit_names:
    print(subreddit_name)
    cnt = 0
    total_sum=0
    for comment in get_comments(subreddit_name):
        # Process comment text (e.g., remove irrelevant characters)
        if cnt == 3:
            avg=total_sum//cnt
            if avg>=-1 and avg<-0.5:
                rating.append([subreddit_name, "😩" ])
            elif avg>=-0.5 and avg<0.5:
                rating.append([subreddit_name,"😐"])
            elif avg>=0.5 and avg<=1:
                rating.append([subreddit_name,"🤩"])
            break
        cnt += 1
        comment_text = comment.body.replace("\n", " ")  # Replace newlines with spaces

        # Analyze sentiment
        sentiment_score = analyze_sentiment(comment_text)
        total_sum+=sentiment_score


        # Update mood statistics based on sentiment score (positive, negative, neutral)
        # ... your logic to track mood ...

        # Optionally, print results for debugging/monitoring
        print(f" subrredit_name:{subreddit_name} Sentiment: {sentiment_score}")
df = pd.DataFrame(rating, columns=["r/subreddit", "mood"])

print(df)
