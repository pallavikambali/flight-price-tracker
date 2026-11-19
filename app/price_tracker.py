def check_price(flight, target_price, lowest_price):

    current_price = flight["price"]

    if current_price <= target_price:
        print("🎉 Flight price is within your budget!")

    else:
        print("Price is still above your target.")

    if lowest_price is not None:

        if current_price < lowest_price:
            print(f"Price dropped by ₹{lowest_price - current_price}")

        elif current_price > lowest_price:
            print(f"Price increased by ₹{current_price - lowest_price}")

        else:
            print("Price remains unchanged.")