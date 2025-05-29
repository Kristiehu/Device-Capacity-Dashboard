import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

# ——— USER CONFIG ———
INPUT_FILE   = "input.xlsx"                # or .csv
SHEET_NAME   = "Sheet1"                    # only for Excel
OUTPUT_FILE  = "output_with_latlon.xlsx"
# change these to match your column names:
ADDR_COL     = "Address"
CITY_COL     = "City"
PROV_COL     = "Province"
COUNTRY_COL  = "Country"
# ——————————————

# 1. Load your data
if INPUT_FILE.lower().endswith((".xls", ".xlsx")):
    df = pd.read_excel(INPUT_FILE, sheet_name=SHEET_NAME, dtype=str)
else:
    df = pd.read_csv(INPUT_FILE, dtype=str)

# 2. Fill NaN with empty strings, build a full‐address field
df = df.fillna("")
df["FullAddress"] = (
    df[ADDR_COL].str.strip() + ", "
  + df[CITY_COL].str.strip() + ", "
  + df[PROV_COL].str.strip() + ", "
  + df[COUNTRY_COL].str.strip()
)

# 3. Prepare geocoder + rate limiter
geolocator = Nominatim(user_agent="batch_geocoder", timeout=10)
geocode    = RateLimiter(
    geolocator.geocode,
    min_delay_seconds  = 1,    # 1 sec between queries
    max_retries        = 2,    # retry twice on failure
    error_wait_seconds = 5     # wait 5s after an error
)

# 4. Add empty lat/lon columns
df["latitude"]  = None
df["longitude"] = None

# 5. Loop & geocode every row
total = len(df)
for i, row in df.iterrows():
    full = row["FullAddress"]
    print(f"Geocoding {i+1}/{total}: {full}")
    try:
        loc = geocode(full)
        if loc:
            df.at[i, "latitude"]  = loc.latitude
            df.at[i, "longitude"] = loc.longitude
        else:
            print(f"⚠️  Warning: no result for row {i+1}")
    except Exception as e:
        print(f"⚠️  Error on row {i+1}: {e}")

# 6. Save results
df.drop(columns="FullAddress").to_excel(OUTPUT_FILE, index=False)
print(f"\n✅ Done! Wrote {total} rows with lat/lon to {OUTPUT_FILE}")
