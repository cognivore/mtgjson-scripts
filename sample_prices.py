import json

# Load the full price data from AllPrices.json
with open('AllPrices.json', 'r') as file:
    data = json.load(file)

# Extract every 2000th card to create a sample subset
sample_data = {'data': {}}
cards = list(data['data'].items())

for i in range(0, len(cards), 2000):
    card_id, price_info = cards[i]
    sample_data['data'][card_id] = price_info

# Save the sample data to SomePrices.json
with open('SomePrices.json', 'w') as file:
    json.dump(sample_data, file, indent=4)

print("Sample data written to SomePrices.json")

