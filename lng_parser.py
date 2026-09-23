def calculate_volume(barrels):
    # Standard conversion factor for LNG barrels to cubic meters
    return barrels * 0.159

import datetime

def estimate_delivery(departure_date, travel_days):
    return departure_date + datetime.timedelta(days=travel_days)

# Add this inside your "if __name__ == '__main__':" block at the bottom:



if __name__ == "__main__":
    cargo_barrels = 500000
    print(f"Volume: {calculate_volume(cargo_barrels)} m³")
    today = datetime.date.today()
    print(f"Expected Delivery: {estimate_delivery(today, 12)}")
