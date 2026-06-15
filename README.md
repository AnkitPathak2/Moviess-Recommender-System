# 🎬 Movie Recommendation System

A Machine Learning-based Movie Recommendation System that suggests similar movies based on content similarity. The application is built using Python, Streamlit, and TMDB movie datasets, providing users with personalized movie recommendations through an interactive web interface.

## 📌 Project Overview

With thousands of movies available across streaming platforms, finding the right movie can be overwhelming. This project helps users discover movies similar to their favorites by leveraging content-based recommendation techniques.

The system analyzes movie attributes such as genres, keywords, cast, crew, and overview to recommend movies that match user preferences.

## 🎯 Objective

The primary objective of this project is to:

- Build a personalized movie recommendation engine.
- Improve movie discovery using machine learning.
- Provide an interactive and user-friendly web application.
- Demonstrate practical implementation of recommendation systems.

## 🛠️ Technologies Used

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Scikit-Learn
- NLTK
- Pickle

### Web Framework
- Streamlit

### Dataset
- TMDB 5000 Movies Dataset

### Authentication
- Firebase Authentication (Login & Signup System) :contentReference[oaicite:1]{index=1}

## 📂 Dataset Information

The project uses the TMDB 5000 Movies Dataset containing:

- Movie Title
- Genres
- Cast
- Crew
- Keywords
- Overview
- Popularity Metrics
- Ratings

## ⚙️ Methodology

### Data Preprocessing
- Removed missing values
- Extracted relevant movie features
- Combined text-based attributes
- Feature engineering and cleaning

### Feature Extraction
- Text vectorization using Count Vectorizer
- Natural Language Processing techniques

### Similarity Calculation
- Cosine Similarity
- Content-Based Filtering

### Recommendation Engine
- Finds movies similar to the selected movie
- Returns top recommended movies

## 🚀 Features

### 🎥 Movie Recommendations
Get top similar movie recommendations instantly.

### 🔍 Search Functionality
Select a movie from the available list.

### 👤 User Authentication
- User Login
- User Registration
- Firebase Integration

### 🌐 Interactive Web Application
Built using Streamlit for easy access and deployment.

## 📊 Project Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Text Vectorization
   ↓
Cosine Similarity Matrix
   ↓
Recommendation Engine
   ↓
Streamlit Web Application
```

## 🎥 Project Demo

[Demo Video](Demo/movie_recommendation_demo.mkv)

## 💡 Skills Demonstrated

- Machine Learning
- Recommendation Systems
- Natural Language Processing
- Data Preprocessing
- Python Programming
- Streamlit Development
- Firebase Authentication
- Content-Based Filtering

## 📈 Future Improvements

- Hybrid Recommendation System
- Collaborative Filtering
- User Rating-Based Recommendations
- Movie Posters Integration
- TMDB API Integration
- Deployment on Streamlit Cloud

⭐ If you found this project useful, consider giving it a star!
