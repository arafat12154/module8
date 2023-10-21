import sqlite3
conn = sqlite3.connect("airports.db")
cursor = conn.cursor()
def fetch_airport_info(icao_code):
    cursor.execute("SELECT name, municipality FROM airport WHERE ident=?", (icao_code,))
    airport_info = cursor.fetchone()
    return airport_info
if __name__ == "__main__":
    while True:
        icao_code = input("Enter  ICAO code of the airport (or 'q' to quit): ").strip().upper()
        if icao_code == 'Q':
            break
        airport_info = fetch_airport_info(icao_code)
        if airport_info:
            airport_name, town = airport_info
            print(f"ICAO Code: {icao_code}")
            print(f"Airport Name: {airport_name}")
            print(f"Location (Town): {town}")
        else:
            print(f"No information found for ICAO code {icao_code}.")
    conn.close()