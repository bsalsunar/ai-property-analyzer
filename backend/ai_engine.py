import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_listing(listing_text):

    prompt = f"""
You are a real estate AI evaluator.

Analyze the following property listing and return STRICT JSON only.

TASKS:

1. Give a Listing Quality Score (0–100)
2. Give an SEO Score (0–100)
3. Detect missing information (price, bedrooms, bathrooms, location, amenities)
4. Explain WHY the scores were given (important)
5. Improve the listing (make it professional and SEO optimized)

OUTPUT FORMAT (STRICT JSON):

{{
  "quality_score": number,
  "seo_score": number,
  "missing_fields": [],
  "explanation": [],
  "improved_listing": "string"
}}

LISTING:
{listing_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
