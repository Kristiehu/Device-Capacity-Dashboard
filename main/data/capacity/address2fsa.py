#!/usr/bin/env python3
"""
update_postal_codes.py

Reads a table of addresses, geocodes missing postal codes via Nominatim,
and writes out the results with a Message column.
"""

import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time

# ——— USER CONFIG ———
INPUT_FILE   = "input.xlsx"           # or "addresses.csv"
SHEET_NAME   = "Sheet1"                   # only for Excel
OUTPUT_FILE  = "addresses_with_codes.xlsx"  # or .csv
PAUSE_SEC    = 1                          # respect Nominatim rate-limit
USER_AGENT   = "postal_updater_app"       # any descriptive string
# ——————————————

def load_table(path):
    if path.lower().endswith((".xls", ".xlsx")):
        return pd.read_excel(path, sheet_name=SHEET_NAME)
    else:
        return pd.read_csv(path)

def geocode_postal(geolocator, address, city, retries=3):
    """Return full postcode (e.g. 'M5V 2B2') or None."""
    query = f"{address}, {city}"
    try:
        loc = geolocator.geocode(query, addressdetails=True, timeout=10)
    except GeocoderTimedOut:
        if retries > 0:
            return geocode_postal(geolocator, address, city, retries-1)
        return None
    if not loc:
        return None
    return loc.raw.get("address", {}).get("postcode")

def main():
    # load
    df = load_table(INPUT_FILE)
    geolocator = Nominatim(user_agent=USER_AGENT)

    new_codes = []
    messages  = []

    for _, row in df.iterrows():
        existing = row.get("Postal_code", None)
        if pd.notna(existing) and str(existing).strip():
            new_codes.append(existing)
            messages.append("Existing")
        else:
            code = geocode_postal(geolocator, row["Address"], row["City"])
            if code:
                new_codes.append(code)
                messages.append(f"Found: {code}")
            else:
                new_codes.append(None)
                messages.append("Not found")
            time.sleep(PAUSE_SEC)

    df["Postal_code"] = new_codes
    df["Message"]     = messages

    # save
    if OUTPUT_FILE.lower().endswith((".xls", ".xlsx")):
        df.to_excel(OUTPUT_FILE, index=False)
    else:
        df.to_csv(OUTPUT_FILE, index=False)

    print(f"Done! Wrote {len(df)} rows to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
