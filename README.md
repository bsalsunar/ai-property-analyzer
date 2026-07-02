# AI Property Listing Quality & SEO Analyzer

## Project Overview

This project is an AI-powered real estate application that analyzes property listings and provides quality feedback, SEO scoring, missing information detection, explainable AI reasoning, and an improved listing recommendation.

The goal is to help real estate agents, property owners, and listing platforms improve listing quality before publishing.

---

## Problem Statement

Many real estate listings are incomplete, poorly written, or not optimized for search visibility. This can reduce user engagement, search ranking, and lead generation.

This application solves that problem by using AI to evaluate a listing and provide actionable recommendations.

---

## Features

* Listing Quality Score
* SEO Score
* Missing Information Detection
* Explainable AI Feedback
* Improved SEO-Friendly Listing
* FastAPI Backend
* Streamlit User Interface
* SQLite Database Storage

---

## Technology Stack

* Python
* Pandas
* FastAPI
* Streamlit
* SQLite
* OpenAI API
* Python-dotenv
* Requests

---

## Project Structure

```text
ai-property-analyzer/

data/
  raw/
  processed/

backend/
  ai_engine.py
  main.py
  database.py
  data_prep.py

frontend/
  app.py

docs/
README.md
requirements.txt
```

---

## Data Collection

The project uses a public real estate housing dataset.

Dataset source:

Ames Housing Dataset / Kaggle real estate housing dataset

The raw dataset is stored in:

```text
data/raw/properties.csv
```

The processed dataset is stored in:

```text
data/processed/properties_clean.csv
```

---

## Data Engineering

The data pipeline performs the following steps:

1. Loads raw property data
2. Selects relevant real estate columns
3. Cleans and standardizes records
4. Creates synthetic listing descriptions
5. Saves processed data as CSV
6. Stores analysis results in SQLite

Database:

```text
realestate.db
```

Main table:

```text
analysis_results
```

---

## AI Component

The AI engine evaluates each property listing and returns structured JSON output.

AI outputs include:

* Quality Score
* SEO Score
* Missing Fields
* Explanation
* Improved Listing

This goes beyond simple text generation because the system performs analysis, scoring, issue detection, explanation, and recommendation generation.

---

## API Endpoints

### Health Check

```http
GET /health
```

### Analyze Listing

```http
POST /analyze
```

Example request:

```json
{
  "listing_text": "2 bed apartment in Dallas. Nice location. Contact now."
}
```

Example response:

```json
{
  "quality_score": 45,
  "seo_score": 40,
  "missing_fields": ["price", "bathrooms", "amenities"],
  "explanation": [
    "The listing description is too short.",
    "Important property details are missing.",
    "SEO keywords and location details are weak."
  ],
  "improved_listing": "Modern 2-bedroom apartment located in Dallas..."
}
```

---

## How to Run the Project

### 1. Clone Repository

```bash
git clone YOUR_REPOSITORY_URL
cd ai-property-analyzer
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add OpenAI API Key

Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
```

### 5. Run Backend

```bash
uvicorn backend.main:app --reload
```

Open API docs:

```text
http://127.0.0.1:8000/docs
```

### 6. Run Frontend

Open a second terminal:

```bash
source venv/bin/activate
streamlit run frontend/app.py
```

---

## Architecture

```text
Real Estate Dataset
        ↓
Data Cleaning & Transformation
        ↓
SQLite Database
        ↓
AI Listing Analyzer
        ↓
FastAPI Backend
        ↓
Streamlit UI
```

---

## Assumptions

* The project focuses on listing quality rather than property price prediction.
* Public housing data is used for demonstration.
* Some listing descriptions are generated from structured housing fields.
* AI scoring is based on listing completeness, clarity, SEO strength, and information richness.

---

## Future Improvements

* Add image quality analysis
* Add duplicate listing detection
* Add price anomaly detection
* Add user authentication
* Deploy backend and frontend online
* Add historical analytics dashboard

---

## Final Outcome

The final application allows a user to paste a property listing and receive:

* Quality Score
* SEO Score
* Missing Information
* AI Explanation
* Improved Listing Recommendation
