from setuptools import setup, find_packages
import pathlib

# Read the contents of README file
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="social-media-curator",
    version="1.0.0",
    description="A comprehensive tool for analyzing and improving social media content",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-repo/social-media-curator",
    author="Social Media Curator Team",
    author_email="your-email@example.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Information Technology",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Communications :: Chat",
        "Topic :: Database",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    keywords="social media, nlp, sentiment analysis, engagement, analytics",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8, <4",
    install_requires=[
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "scikit-learn>=1.3.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "PyQt5>=5.15.0",
        "transformers>=4.30.0",
        "torch>=2.0.0",
    ],
    extras_require={
        "dev": [
            "black>=23.0.0",
            "flake8>=6.0.0",
            "isort>=5.12.0",
            "mypy>=1.0.0",
            "pytest>=7.0.0",
            "pytest-qt>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "social-media-curator=social_media_curator:run_app",
        ],
    },
    package_data={
        "social_media_curator": [
            "data/*.db",
            "data/*.csv",
            "data/*.png",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)