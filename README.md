# Social Media Curator

A comprehensive Python application for analyzing and improving social media content using engagement metrics and NLP sentiment analysis.

## Features

- **Engagement Analysis**: Analyze likes, shares, and comments metrics
- **Scheduling Optimization**: Find optimal posting times based on historical data
- **Sentiment Analysis**: NLP-powered sentiment analysis using Hugging Face transformers
- **Feedback Generation**: Automated feedback based on engagement performance
- **Trend Prediction**: Machine learning-based future engagement forecasting
- **Modern UI**: Liquid glass effect with claymorphism buttons
- **Comprehensive Logging**: Real-time debugging and error tracking

## Installation

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git

### Setup

```bash
# Clone the repository
git clone https://github.com/your-repo/social-media-curator.git
cd social-media-curator

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install PyQt5 system dependencies (Linux)
sudo apt-get install -y libgl1 libglx0 libgl1-mesa-dev libxcb-xinerama0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-render-util0 libxcb-shape0 libxcb-randr0
```

## Usage

### Running the Application

```bash
# Run the main application
python main.py

# For headless environments
python main.py --headless
```

### Command Line Interface

```bash
# Analyze engagement data
python -m social_media_curator.analysis.engagement_analysis

# Run sentiment analysis
python -m social_media_curator.ui.sentiment_analysis

# Generate feedback
python -m social_media_curator.analysis.feedback_analysis
```

## Project Structure

```
social-media-curator/
├── src/
│   └── social_media_curator/
│       ├── __init__.py               # Main package entry point
│       ├── core/
│       │   └── analyzers.py         # Core analysis classes
│       ├── analysis/
│       │   ├── engagement_analysis.py
│       │   ├── feedback_analysis.py
│       │   ├── feedback_loop.py
│       │   └── scheduling_analysis.py
│       ├── ui/
│       │   ├── main_application.py  # Main GUI application
│       │   └── sentiment_analysis.py # Sentiment analysis GUI
│       ├── utils/
│       │   ├── update_db.py          # Database utilities
│       │   └── visualization.py      # Visualization tools
│       └── data/
│           ├── engagement.db        # Sample database
│           ├── engagement_data.db
│           ├── engagement_data.csv
│           ├── engagement_over_time.png
│           └── engagement_trends.png
├── tests/                            # Test files
├── docs/                             # Documentation
├── main.py                           # Main entry point
├── requirements.txt                  # Dependencies
├── README.md                         # This file
└── .gitignore                         # Git ignore rules
```

## Architecture

The application follows a modular architecture:

- **Core**: Contains the main analysis classes and business logic
- **Analysis**: Individual analysis modules for different metrics
- **UI**: User interface components including the main application
- **Utils**: Utility functions and helper classes
- **Data**: Sample data files and databases

## Configuration

The application uses SQLite databases by default. You can configure the database path in the individual analyzer classes.

## Development

### Running Tests

```bash
pytest tests/
```

### Code Formatting

```bash
black src/
isort src/
```

### Linting

```bash
flake8 src/
mypy src/
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please open an issue on GitHub.