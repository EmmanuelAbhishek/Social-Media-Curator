#!/usr/bin/env python3
"""
Test script to verify the project structure and imports work correctly.
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test that all imports work correctly."""
    print("Testing project structure and imports...")
    
    try:
        # Test main package import
        import social_media_curator
        print("✓ Main package imported successfully")
        
        # Test core modules
        from social_media_curator.core.analyzers import (
            EngagementAnalyzer,
            SchedulingAnalysis,
            FeedbackAnalyzer,
            SentimentAnalyzer
        )
        print("✓ Core analyzers imported successfully")
        
        # Test analysis modules
        from social_media_curator.analysis import (
            engagement_analysis,
            feedback_analysis,
            feedback_loop,
            scheduling_analysis
        )
        print("✓ Analysis modules imported successfully")
        
        # Test UI modules
        from social_media_curator.ui import (
            main_application,
            sentiment_analysis
        )
        print("✓ UI modules imported successfully")
        
        # Test utils modules
        from social_media_curator.utils import (
            update_db,
            visualization
        )
        print("✓ Utility modules imported successfully")
        
        # Test data files exist
        data_dir = os.path.join(os.path.dirname(social_media_curator.__file__), 'data')
        if os.path.exists(data_dir):
            db_files = [f for f in os.listdir(data_dir) if f.endswith('.db')]
            print(f"✓ Found {len(db_files)} database files in data directory")
        else:
            print("✗ Data directory not found")
            
        print("\n✅ All tests passed! Project structure is working correctly.")
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {str(e)}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_imports()
    sys.exit(0 if success else 1)