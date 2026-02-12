"""
Social Media Curator - Main Package

A comprehensive tool for analyzing and improving social media content
using engagement metrics and NLP sentiment analysis.
"""

from .core.analyzers import (
    EngagementAnalyzer,
    SchedulingAnalysis,
    FeedbackAnalyzer,
    SentimentAnalyzer
)
from .ui.main_application import MainApplication

__version__ = "1.0.0"
__author__ = "Social Media Curator Team"
__license__ = "MIT"

# Main application entry point
def run_app():
    """Run the main application with GUI."""
    import sys
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtCore import QTimer
    import os
    
    # Set Qt platform to offscreen for headless environments
    os.environ['QT_QPA_PLATFORM'] = 'offscreen'
    
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    window = MainApplication()
    window.show()
    
    # Load quick stats on startup
    QTimer.singleShot(100, window.load_quick_stats)
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_app()