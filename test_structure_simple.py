#!/usr/bin/env python3
"""
Simple test script to verify the project structure without external dependencies.
"""

import sys
import os

def test_structure():
    """Test that the project structure is correct."""
    print("Testing project structure...")
    
    # Check main files exist
    main_files = [
        'main.py',
        'README.md',
        'requirements.txt',
        'setup.py',
        '.gitignore'
    ]
    
    for file in main_files:
        if os.path.exists(file):
            print(f"✓ {file} exists")
        else:
            print(f"✗ {file} missing")
            return False
    
    # Check src directory structure
    src_dir = 'src/social_media_curator'
    expected_dirs = [
        'core',
        'analysis',
        'ui',
        'utils',
        'data'
    ]
    
    for dir_name in expected_dirs:
        full_path = os.path.join(src_dir, dir_name)
        if os.path.exists(full_path) and os.path.isdir(full_path):
            print(f"✓ {full_path} exists")
        else:
            print(f"✗ {full_path} missing")
            return False
    
    # Check key Python files exist
    expected_files = {
        'src/social_media_curator/__init__.py': 'Main package init',
        'src/social_media_curator/core/analyzers.py': 'Core analyzers',
        'src/social_media_curator/ui/main_application.py': 'Main UI (should fail)',
        'src/social_media_curator/analysis/engagement_analysis.py': 'Engagement analysis',
        'src/social_media_curator/ui/sentiment_analysis.py': 'Sentiment analysis UI',
        'src/social_media_curator/utils/visualization.py': 'Visualization utils',
        'src/social_media_curator/utils/update_db.py': 'Database utils'
    }
    
    for file_path, description in expected_files.items():
        if os.path.exists(file_path):
            print(f"✓ {description} found")
        else:
            print(f"✗ {description} missing: {file_path}")
            # Don't fail for main_application.py as it might not exist yet
            if 'main_application.py' not in file_path:
                return False
    
    # Check data files
    data_dir = 'src/social_media_curator/data'
    if os.path.exists(data_dir):
        data_files = os.listdir(data_dir)
        db_files = [f for f in data_files if f.endswith('.db')]
        csv_files = [f for f in data_files if f.endswith('.csv')]
        png_files = [f for f in data_files if f.endswith('.png')]
        
        print(f"✓ Data directory contains:")
        print(f"  - {len(db_files)} database files")
        print(f"  - {len(csv_files)} CSV files")
        print(f"  - {len(png_files)} image files")
    else:
        print("✗ Data directory not found")
        return False
    
    # Check tests and docs directories
    for dir_name in ['tests', 'docs']:
        if os.path.exists(dir_name) and os.path.isdir(dir_name):
            print(f"✓ {dir_name}/ directory exists")
        else:
            print(f"✗ {dir_name}/ directory missing")
            return False
    
    print("\n✅ Project structure verification completed successfully!")
    print("\nProject structure:")
    print("social-media-curator/")
    print("├── src/")
    print("│   └── social_media_curator/")
    print("│       ├── __init__.py")
    print("│       ├── core/")
    print("│       ├── analysis/")
    print("│       ├── ui/")
    print("│       ├── utils/")
    print("│       └── data/")
    print("├── tests/")
    print("├── docs/")
    print("├── main.py")
    print("├── README.md")
    print("├── requirements.txt")
    print("├── setup.py")
    print("└── .gitignore")
    
    return True

if __name__ == "__main__":
    success = test_structure()
    sys.exit(0 if success else 1)