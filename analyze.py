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
rating_score=[]

# weary_face=emoji.emojize(':Weary Face:')

# neutral_face=emoji.emojize(':Neutral Face:')
# star_struck=emoji.emojize(':Star-Struck')

emos=["😩","😠" ,"😞", "😔" , "😐" ,"🙂" ,"😊", "😄" ,"😁" ,"🤩" ]

for subreddit_name in subreddit_names:
    print(subreddit_name)
    cnt = 0
    total_sum=0
    for comment in get_comments(subreddit_name):
        if cnt == 3:
            avg=total_sum/cnt
            rating_score.append([f'r/{subreddit_name}', avg])
            if avg>=-1 and avg<-0.8:
                rating.append([subreddit_name, emos[0] ])
            elif avg>=-0.8 and avg<-0.6:
                rating.append([subreddit_name, emos[1]])
            elif avg>=-0.6 and avg<-0.4:
                rating.append([subreddit_name, emos[2]])
            elif avg>=-0.4 and avg<-0.2:
                rating.append([subreddit_name, emos[3]])
            elif avg>=-0.2 and avg<0:
                rating.append([subreddit_name, emos[4]])
            elif avg>=0 and avg<0.2:
                rating.append([subreddit_name, emos[5]])
            elif avg>=0.2 and avg<0.4:
                rating.append([subreddit_name, emos[6]])
            elif avg>=0.4 and avg<0.6:
                rating.append([subreddit_name, emos[7]])
            elif avg>=0.6 and avg<0.8:
                rating.append([subreddit_name, emos[8]])
            else:
                rating.append([subreddit_name, emos[9]])

            break
        cnt += 1
        comment_text = comment.body.replace("\n", " ")  # Replace newlines with spaces

        # Analyze sentiment
        sentiment_score = analyze_sentiment(comment_text)
        total_sum+=sentiment_score


        print(f" subrredit_name:{subreddit_name} Sentiment: {sentiment_score}")
df = pd.DataFrame(rating, columns=["subreddit", "mood"])
df_score=pd.DataFrame(rating_score, columns=['subreddit','mood'])

print(df)


