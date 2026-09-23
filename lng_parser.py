def calculate_volume(barrels):
    # Standard conversion factor for LNG barrels to cubic meters
    return barrels * 0.159

if __name__ == "__main__":
    cargo_barrels = 500000
    print(f"Volume: {calculate_volume(cargo_barrels)} m³")
