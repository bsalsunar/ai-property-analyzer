import pandas as pd
import os

# Load dataset
df = pd.read_csv("data/raw/properties.csv")

# Keep important columns only
df = df[[
    "Overall Qual",
    "Gr Liv Area",
    "Bedroom AbvGr",
    "Full Bath",
    "Neighborhood",
    "Year Built",
    "SalePrice"
]]

# Create synthetic listing description
df["description"] = (
    df["Bedroom AbvGr"].astype(str) + " bed, " +
    df["Full Bath"].astype(str) + " bath home in " +
    df["Neighborhood"] + ". Built in " +
    df["Year Built"].astype(str) +
    " with " + df["Gr Liv Area"].astype(str) + " sqft living area."
)

# Rename for consistency
df.rename(columns={
    "Gr Liv Area": "area_sqft",
    "Bedroom AbvGr": "bedrooms",
    "Full Bath": "bathrooms",
    "Neighborhood": "location"
}, inplace=True)

# Save processed data
os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/properties_clean.csv", index=False)

print("Data processing complete")
