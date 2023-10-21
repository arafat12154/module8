from geopy.distance import geodesic
airport_coordinates = {
    "ICAO1": (latitude1, longitude1),  # Replace with actual coordinates
    "ICAO2": (latitude2, longitude2),  # Replace with actual coordinates
}
def get_distance(icao1, icao2):
    if icao1 in airport_coordinates and icao2 in airport_coordinates:
        coord1 = airport_coordinates[icao1]
        coord2 = airport_coordinates[icao2]
        distance = geodesic(coord1, coord2).kilometers
        return distance
    else:
        return None
if __name__ == "__main__":
    icao_code1 = input("Enter the ICAO code of the first airport: ").strip().upper()
    icao_code2 = input("Enter the ICAO code of the second airport: ").strip().upper()

    distance = get_distance(icao_code1, icao_code2)

    if distance is not None:
        print(f"The distance between {icao_code1} and {icao_code2} is approximately {distance:.2f} kilometers.")
    else:
        print("Airport coordinates not found for one or both of the provided ICAO codes.")