prices = {"apple": 30, "banana": 10, "cherry": 50}
sake ={}
prices["apple"]         # 30        — access by key
prices["mango"] = 80    # add new key-value pair
prices["banana"] = 15   # modify by key
len(prices)             # 4

for key in prices:
    
    if key not in sake:
        sake.append(key)
print(sake)             