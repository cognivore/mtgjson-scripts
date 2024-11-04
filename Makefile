PHONY all

AllPrices.json:
	wget https://mtgjson.com/api/v5/AllPrices.json

all: AllPrices.json
