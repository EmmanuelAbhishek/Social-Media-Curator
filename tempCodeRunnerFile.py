# feedback_loop.py
import pandas as pd

def load_engagement_data():
    """Load engagement data from the SQLite database."""
    connection = sqlite3.connect('engagement_data.db')
    query = "SELECT * FROM engagement"
    return pd.read_sql(query, connection)

def analyze_feedback_loop(data):
    """Analyze past engagement data and suggest future content strategies."""
    if data.empty:
        print("No engagement data available for analysis.")
        return

    positive_engagement = data[data['sentiment'] == 'POSITIVE']
    negative_engagement = data[data['sentiment'] == 'NEGATIVE']

    avg_positive_engagement = positive_engagement[['likes', 'shares', 'comments']].mean()
    avg_negative_engagement = negative_engagement[['likes', 'shares', 'comments']].mean()

    if avg_positive_engagement['likes'] > avg_negative_engagement['likes']:
        print("Consider creating more positive content like:", avg_positive_engagement)
    else:
        print("Consider adjusting the tone of negative content like:", avg_negative_engagement)

if __name__ == "__main__":
    engagement_data = load_engagement_data()
    analyze_feedback_loop(engagement_data)
