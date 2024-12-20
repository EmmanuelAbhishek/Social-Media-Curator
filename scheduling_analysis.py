import sqlite3
import pandas as pd
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np


class SchedulingAnalysis:
    def __init__(self, db_path="engagement_data.db"):
        self.db_path = db_path

    def connect_database(self):
        """Establish a connection to the SQLite database."""
        try:
            conn = sqlite3.connect(self.db_path)
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def fetch_data(self):
        """Fetch timestamped engagement data from the database."""
        conn = self.connect_database()
        if conn is None:
            return None

        try:
            query = "SELECT timestamp, likes, shares, comments FROM engagement_data"
            data = pd.read_sql_query(query, conn)
            conn.close()
            data['timestamp'] = pd.to_datetime(data['timestamp'])  # Ensure timestamps are datetime objects
            return data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

    def analyze_hourly_trends(self, data):
        """Perform granular hourly trend analysis."""
        data['hour'] = data['timestamp'].dt.hour
        data['total_engagement'] = data['likes'] + data['shares'] + data['comments']
        hourly_trends = data.groupby('hour')['total_engagement'].mean().reset_index()

        # Find the best hour to post
        best_hour = hourly_trends.loc[hourly_trends['total_engagement'].idxmax()]['hour']
        return hourly_trends, int(best_hour)

    def analyze_platform_specific_trends(self, data, platform):
        """
        Placeholder for platform-specific analysis.
        Currently treats all data as one platform but can be expanded to include platform data.
        """
        print(f"Analyzing trends for {platform} (platform-specific analysis can be added later).")
        return self.analyze_hourly_trends(data)

    def predict_future_trends(self, data):
        """Predict future engagement trends using Linear Regression."""
        data['day'] = data['timestamp'].dt.day
        daily_trends = data.groupby('day')['total_engagement'].sum().reset_index()

        # Prepare data for Linear Regression
        X = daily_trends['day'].values.reshape(-1, 1)
        y = daily_trends['total_engagement'].values

        model = LinearRegression()
        model.fit(X, y)

        # Predict engagement for the next 7 days
        future_days = np.array([max(X) + i for i in range(1, 8)]).reshape(-1, 1)
        predictions = model.predict(future_days)

        return future_days.flatten(), predictions

    def analyze_custom_period(self, data, start_date, end_date):
        """Allow users to define custom time periods for analysis."""
        mask = (data['timestamp'] >= pd.to_datetime(start_date)) & (data['timestamp'] <= pd.to_datetime(end_date))
        custom_period_data = data.loc[mask]

        if custom_period_data.empty:
            print("No data available for the specified period.")
            return None

        hourly_trends, best_hour = self.analyze_hourly_trends(custom_period_data)
        return hourly_trends, best_hour

    def visualize_trends(self, hourly_trends):
        """Visualize hourly trends using a bar chart."""
        plt.bar(hourly_trends['hour'], hourly_trends['total_engagement'], color='skyblue')
        plt.xlabel('Hour of the Day')
        plt.ylabel('Average Engagement')
        plt.title('Hourly Engagement Trends')
        plt.xticks(range(0, 24))
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

    def run_analysis(self, platform="General", custom_period=None):
        """Main method to execute the analysis."""
        data = self.fetch_data()
        if data is None:
            print("Unable to fetch data. Exiting analysis.")
            return

        if custom_period:
            start_date, end_date = custom_period
            hourly_trends, best_hour = self.analyze_custom_period(data, start_date, end_date)
        else:
            hourly_trends, best_hour = self.analyze_platform_specific_trends(data, platform)

        if hourly_trends is not None:
            print(f"Hourly Trends:\n{hourly_trends}")
            print(f"Best hour to post: {best_hour}:00")

            self.visualize_trends(hourly_trends)

            # Predict future trends
            future_days, predictions = self.predict_future_trends(data)
            print("Predicted Engagement for the next 7 days:")
            for day, pred in zip(future_days, predictions):
                print(f"Day {int(day)}: {int(pred)} engagements")


if __name__ == "__main__":
    analysis = SchedulingAnalysis()
    analysis.run_analysis(
        platform="Instagram",
        custom_period=("2024-12-01", "2024-12-15")
    )
