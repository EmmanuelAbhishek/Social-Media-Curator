import pandas as pd
import sqlite3
from transformers import pipeline

# Load the sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(content):
    result = sentiment_analyzer(content)
    sentiment = result[0]['label']
    score = result[0]['score']
    return sentiment, score

def analyze_feedback():
    # Connect to SQLite database
    conn = sqlite3.connect('engagement_data.db')
    
    # Read engagement data into DataFrame
    data = pd.read_sql_query('SELECT * FROM engagement', conn)
    
    conn.close()
    
    if data.empty:
        print("No engagement data available for analysis.")
        return
    
    print("Engagement data loaded successfully:")
    print(data)
    
    # Analyze feedback sentiment
    for index, row in data.iterrows():
        # Generate feedback based on likes
        if row['likes'] > 50:  # Example condition for positive feedback
            feedback = "Great job! Keep using this tone to engage your audience."
        else:
            feedback = "Consider adjusting the tone for better engagement."
        
        # Analyze sentiment of the feedback
        sentiment, score = analyze_sentiment(feedback)
        print(f"Feedback on {row['timestamp']}: \"{feedback}\" => Sentiment: {sentiment}, Score: {score:.2f}")

if __name__ == "__main__":
    analyze_feedback()
