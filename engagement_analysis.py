import pandas as pd
import sqlite3

class EngagementAnalyzer:
    def __init__(self, db_path='engagement_data.db'):
        self.db_path = db_path

    def connect_to_database(self):
        """Connect to the SQLite database and return the connection object."""
        try:
            conn = sqlite3.connect(self.db_path)
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def fetch_engagement_data(self, conn):
        """Fetch engagement data from the database into a DataFrame."""
        try:
            query = 'SELECT * FROM engagement'
            data = pd.read_sql_query(query, conn)
            return data
        except pd.io.sql.DatabaseError as e:
            print(f"Error fetching data: {e}")
            return pd.DataFrame()

    def analyze_engagement(self):
        """Perform analysis on engagement data."""
        conn = self.connect_to_database()
        if not conn:
            print("Unable to establish database connection. Exiting analysis.")
            return

        data = self.fetch_engagement_data(conn)
        conn.close()

        if data.empty:
            print("No engagement data available for analysis.")
            return

        print("Engagement data loaded successfully:")
        print(data.head())

        try:
            # Calculate total and average engagement
            data['total_engagement'] = data['likes'] + data['shares'] + data['comments']
            average_engagement = data['total_engagement'].mean()

            print(f"Average Engagement per Post: {average_engagement:.2f}")

            # Additional insights
            max_engagement = data['total_engagement'].max()
            min_engagement = data['total_engagement'].min()
            most_engaged_post = data.loc[data['total_engagement'].idxmax()]

            print(f"Maximum Engagement: {max_engagement}")
            print(f"Minimum Engagement: {min_engagement}")
            print("Most Engaged Post:")
            print(most_engaged_post)
        except KeyError as e:
            print(f"Error during analysis: Missing column {e}")
        except Exception as e:
            print(f"Unexpected error during analysis: {e}")

if __name__ == "__main__":
    analyzer = EngagementAnalyzer()
    analyzer.analyze_engagement()
