import json

# Load the price data
with open('AllPrices.json', 'r') as file:
    data = json.load(file)

# Initialize a list to store card prices
card_prices = []

# Iterate through each card's price data
for card_id, price_info in data['data'].items():
    min_price = float('inf')
    
    # Check if 'paper' prices and 'cardmarket' prices are available
    if 'paper' in price_info and 'cardmarket' in price_info['paper']:
        cardmarket_prices = price_info['paper']['cardmarket']
        
        # Check if 'retail' prices are available
        if 'retail' in cardmarket_prices:
            # Iterate through each price in 'retail' dictionary
            for date, price in cardmarket_prices['retail'].items():
                # Ensure price is a number before comparing
                if isinstance(price, (int, float)) and price < min_price:
                    min_price = price
    
    # Only add the card if we found a valid price
    if min_price != float('inf'):
        card_prices.append((card_id, min_price))

# Sort the cards by price in descending order
sorted_cards = sorted(card_prices, key=lambda x: x[1], reverse=True)

# Output the sorted list
for card_id, price in sorted_cards:
    print(f'Card ID: {card_id}, Price: ${price:.2f}')

