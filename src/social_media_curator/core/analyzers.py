"""
Core Analyzers Module

Contains all the core analysis classes for engagement, scheduling, feedback, and sentiment analysis.
"""

import logging
import traceback
import pandas as pd
import sqlite3
import numpy as np
from sklearn.linear_model import LinearRegression
from transformers import pipeline

# Set up logging
logger = logging.getLogger('SocialMediaCurator.analyzers')

class SentimentAnalyzer:
    """Sentiment analysis using Hugging Face transformers."""
    
    def __init__(self):
        try:
            self.analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
            logger.info("Sentiment analyzer initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize sentiment analyzer: {str(e)}")
            raise

    def analyze_text(self, text):
        """Analyze sentiment of a single text."""
        try:
            result = self.analyzer(text)
            label = result[0]['label']
            score = result[0]['score']
            return label, round(score * 100, 2)
        except Exception as e:
            logger.error(f"Sentiment analysis error: {str(e)}")
            return f"Error: {str(e)}", 0.0

    def analyze_batch(self, texts):
        """Analyze sentiment of multiple texts."""
        results = []
        for text in texts:
            label, score = self.analyze_text(text)
            results.append((text, label, score))
        return results

class EngagementAnalyzer:
    """Engagement data analysis from SQLite database."""
    
    def __init__(self, db_path='engagement_data.db'):
        self.db_path = db_path

    def connect_to_database(self):
        """Connect to the SQLite database."""
        try:
            conn = sqlite3.connect(self.db_path)
            logger.info(f"Connected to database: {self.db_path}")
            return conn
        except sqlite3.Error as e:
            logger.error(f"Database connection error: {str(e)}")
            return None

    def fetch_engagement_data(self, conn):
        """Fetch engagement data from database."""
        try:
            query = 'SELECT * FROM engagement'
            data = pd.read_sql_query(query, conn)
            logger.info(f"Fetched {len(data)} engagement records")
            return data
        except pd.io.sql.DatabaseError as e:
            logger.error(f"Data fetch error: {str(e)}")
            return pd.DataFrame()

    def analyze_engagement(self):
        """Perform comprehensive engagement analysis."""
        conn = self.connect_to_database()
        if not conn:
            logger.error("Database connection failed")
            return None, "Unable to establish database connection"

        data = self.fetch_engagement_data(conn)
        conn.close()

        if data.empty:
            logger.warning("No engagement data available")
            return None, "No engagement data available for analysis"

        try:
            data['total_engagement'] = data['likes'] + data['shares'] + data['comments']
            average_engagement = data['total_engagement'].mean()
            max_engagement = data['total_engagement'].max()
            min_engagement = data['total_engagement'].min()
            most_engaged_post = data.loc[data['total_engagement'].idxmax()]

            results = {
                'average_engagement': round(average_engagement, 2),
                'max_engagement': int(max_engagement),
                'min_engagement': int(min_engagement),
                'most_engaged_post': most_engaged_post.to_dict(),
                'all_data': data
            }
            
            logger.info("Engagement analysis completed successfully")
            return results, None
        except Exception as e:
            logger.error(f"Analysis error: {str(e)}")
            return None, f"Error during analysis: {str(e)}"

class SchedulingAnalysis:
    """Scheduling and trend analysis."""
    
    def __init__(self, db_path="engagement_data.db"):
        self.db_path = db_path

    def connect_database(self):
        """Connect to database for scheduling analysis."""
        try:
            conn = sqlite3.connect(self.db_path)
            logger.info(f"Connected to database for scheduling analysis: {self.db_path}")
            return conn
        except sqlite3.Error as e:
            logger.error(f"Scheduling database connection error: {str(e)}")
            return None

    def fetch_data(self):
        """Fetch data for scheduling analysis."""
        conn = self.connect_database()
        if conn is None:
            return None

        try:
            query = "SELECT timestamp, likes, shares, comments FROM engagement"
            data = pd.read_sql_query(query, conn)
            conn.close()
            data['timestamp'] = pd.to_datetime(data['timestamp'])
            logger.info(f"Fetched {len(data)} records for scheduling analysis")
            return data
        except Exception as e:
            logger.error(f"Scheduling data fetch error: {str(e)}")
            return None

    def analyze_hourly_trends(self, data):
        """Analyze hourly engagement trends."""
        try:
            data['hour'] = data['timestamp'].dt.hour
            data['total_engagement'] = data['likes'] + data['shares'] + data['comments']
            hourly_trends = data.groupby('hour')['total_engagement'].mean().reset_index()
            best_hour = hourly_trends.loc[hourly_trends['total_engagement'].idxmax()]['hour']
            
            logger.info(f"Hourly trends analysis completed. Best hour: {best_hour}")
            return hourly_trends, int(best_hour)
        except Exception as e:
            logger.error(f"Hourly trends analysis error: {str(e)}")
            return None, None

    def predict_future_trends(self, data):
        """Predict future engagement trends using linear regression."""
        try:
            data['day'] = data['timestamp'].dt.day
            daily_trends = data.groupby('day')['total_engagement'].sum().reset_index()

            X = daily_trends['day'].values.reshape(-1, 1)
            y = daily_trends['total_engagement'].values

            model = LinearRegression()
            model.fit(X, y)

            future_days = np.array([max(X) + i for i in range(1, 8)]).reshape(-1, 1)
            predictions = model.predict(future_days)

            logger.info("Future trends prediction completed")
            return future_days.flatten(), predictions
        except Exception as e:
            logger.error(f"Future trends prediction error: {str(e)}")
            return None, None

class FeedbackAnalyzer:
    """Feedback generation and analysis."""
    
    def __init__(self):
        self.sentiment_analyzer = pipeline("sentiment-analysis")

    def analyze_feedback(self):
        """Generate and analyze feedback for engagement data."""
        try:
            conn = sqlite3.connect('engagement_data.db')
            data = pd.read_sql_query('SELECT * FROM engagement', conn)
            conn.close()

            if data.empty:
                logger.warning("No data for feedback analysis")
                return None, "No engagement data available for analysis"

            results = []
            for index, row in data.iterrows():
                if row['likes'] > 50:
                    feedback = "Great job! Keep using this tone to engage your audience."
                else:
                    feedback = "Consider adjusting the tone for better engagement."
                
                sentiment_result = self.sentiment_analyzer(feedback)
                sentiment = sentiment_result[0]['label']
                score = sentiment_result[0]['score']
                
                results.append({
                    'timestamp': row['timestamp'],
                    'feedback': feedback,
                    'sentiment': sentiment,
                    'score': round(score, 2)
                })

            logger.info(f"Feedback analysis completed for {len(results)} records")
            return results, None
        except Exception as e:
            logger.error(f"Feedback analysis error: {str(e)}")
            return None, f"Error during feedback analysis: {str(e)}"