def analyze_prices(price_list, threshold):
    print("📈 Analyzing energy market prices...")
    for index, price in enumerate(price_list, 1):
        if price > threshold:
            print(f"⚠️ WARNING: Hour {index} price spike detected! (£{price}/MWh)")
        else:
            print(f"Hour {index}: £{price}/MWh (Normal)")


if __name__ == "__main__":
    # Mock data representing hourly natural gas prices
    market_prices = [85.2, 88.5, 94.1, 102.5, 89.0]
    alert_threshold = 95.0

    analyze_prices(market_prices, alert_threshold)
