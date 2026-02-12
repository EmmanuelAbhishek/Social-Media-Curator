import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.widgets import Cursor

# Sample DataFrame structure for demonstration
data = {
    "hour": [0, 1, 2, 3, 0, 1, 2, 3],
    "platform": ["Twitter", "Twitter", "Instagram", "Instagram", "Facebook", "Facebook", "Twitter", "Instagram"],
    "likes": [20, 15, 40, 30, 25, 35, 50, 45],
    "comments": [5, 2, 7, 6, 3, 4, 6, 5],
    "shares": [10, 12, 20, 15, 11, 13, 22, 18]
}

df = pd.DataFrame(data)

# Aggregation function for multi-platform comparison
def prepare_data(df):
    df["engagement"] = df["likes"] + df["comments"] + df["shares"]
    return df.groupby(["hour", "platform"]).sum().reset_index()

# Enhanced visualization function
def visualize_engagement(df):
    aggregated_data = prepare_data(df)

    plt.figure(figsize=(12, 6))

    # Multi-platform comparison
    sns.barplot(
        data=aggregated_data,
        x="hour",
        y="engagement",
        hue="platform",
        palette="viridis"
    )

    # Engagement type segmentation overlay
    for platform in aggregated_data["platform"].unique():
        platform_data = aggregated_data[aggregated_data["platform"] == platform]
        sns.lineplot(
            data=platform_data,
            x="hour",
            y="engagement",
            label=f"Trend - {platform}",
            linestyle="--",
            linewidth=1.5
        )

    # Add hover interactivity (not available in static matplotlib)
    # For advanced hover, libraries like Plotly or Bokeh can be used instead.

    plt.title("Engagement Trends by Hour and Platform")
    plt.xlabel("Hour of Day")
    plt.ylabel("Total Engagement (Likes + Comments + Shares)")
    plt.legend(title="Platform")
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Save and export
    plt.savefig("engagement_trends.png", dpi=300)
    plt.show()

# Call the function to visualize the data
visualize_engagement(df)
