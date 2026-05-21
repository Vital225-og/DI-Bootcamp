# defi 1 
# word_dict = {}
# word = input("Entrez un mot : ").strip()

# for index, lettre in enumerate(word):
#     if lettre in word_dict:
#         word_dict[lettre].append(index)
#     else:
#         word_dict[lettre] = [index]

# print(word_dict)


# defi 2

items_purchase = {
    "Apple": "$4",
    "Honey": "$3",
    "Fan": "$14",
    "Bananas": "$4",
    "Pan": "$100",
    "Spoon": "$2"
}

wallet = "$100"

basket = []

wallet = int(wallet.replace("$", "").replace(",", ""))

for item, price in items_purchase.items():
    price = int(price.replace("$", "").replace(",", ""))

    if wallet >= price:
        basket.append(item)
        wallet -= price

if basket:
    print(sorted(basket))
else:
    print("Nothing")