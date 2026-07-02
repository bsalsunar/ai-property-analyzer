from fastapi import FastAPI
from pydantic import BaseModel
from backend.ai_engine import analyze_listing
import json
from backend.database import create_tables, save_analysis

app = FastAPI(
    title="AI Property Listing Quality & SEO Analyzer",
    description="Analyze real estate listings for quality, SEO, missing fields, and improvement suggestions.",
    version="1.0.0"
)
create_tables()

class ListingRequest(BaseModel):
    listing_text: str

@app.get("/")
def home():
    return {
        "message": "AI Property Listing Quality & SEO Analyzer API is running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

@app.post("/analyze")
def analyze_property_listing(request: ListingRequest):
    result = analyze_listing(request.listing_text)

    try:
        result_json = json.loads(result)
        save_analysis(request.listing_text, result_json)
        return result_json
    except json.JSONDecodeError:
        return {
            "raw_response": result
        }

