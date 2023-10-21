import sqlite3
conn = sqlite3.connect("airports.db")
cursor = conn.cursor()

def fetch_airports_by_country(country_code):
    cursor.execute("SELECT type, COUNT(*) FROM airport WHERE iso_country=? GROUP BY type ORDER BY type",
                   (country_code,))
    airports = cursor.fetchall()
    return airports
if __name__ == "__main__":
    country_code = input("Enter the country code (e.g., FI for Finland): ").strip().upper()

    airports_info = fetch_airports_by_country(country_code)

    if airports_info:
        print(f"Airports in {country_code} ordered by type:")
        for airport_type, count in airports_info:
            print(f"{count} {airport_type} airports")
    else:
        print(f"No airports found for country code {country_code}.")
    conn.close()