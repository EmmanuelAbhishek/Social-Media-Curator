#!/usr/bin/env python3
"""
Main entry point for Social Media Curator application.

This script provides a simple command-line interface to run the application.
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from social_media_curator import run_app

if __name__ == "__main__":
    run_app()