import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

# 📥 Step 1: Load address list
input_file = "addresses.xlsx"  # change to .csv if needed
df = pd.read_excel(input_file)  # or use pd.read_csv("addresses.csv")

# Make sure your address column is labeled 'Address'
addresses = df["Address"]

# 🌐 Step 2: Initialize geolocator
geolocator = Nominatim(user_agent="excel_geocoder")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# 🔄 Step 3: Apply geocoding
df["Location"] = addresses.apply(geocode)
df["Latitude"] = df["Location"].apply(lambda loc: loc.latitude if loc else None)
df["Longitude"] = df["Location"].apply(lambda loc: loc.longitude if loc else None)

# 🧾 Step 4: Export to Excel
output_file = "geocoded_addresses.xlsx"
df.to_excel(output_file, index=False)

print("✅ Geocoding complete! File saved as:", output_file)
