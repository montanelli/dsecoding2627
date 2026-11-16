products = [
    {"name": "Laptop", "price": 1200, "category": "Electronics"},
    {"name": "Keyboard", "price": 100, "category": "Electronics"},
    {"name": "Chair", "price": 250, "category": "Forniture"},
    {"name": "Desk", "price": 400, "category": "Forniture"},
    {"name": "Earphones", "price": 80, "category": "Electronics"},
    {"name": "Monitor", "price": 300, "category": "Electronics"},
]

# 1. Filter products in category "Electronics" with price greater than 100
# consider to use lambda functions
# expected result on the example: ["Laptop", "Monitor"]
result = list(filter(lambda x: (x["name"] if x["category"] == "Electronics" and x["price"] > 100 else None), products))

print(result)

# solution with list comprehension (valid if the use of lambda function is not specified in the assignment)
result = [ x["name"] for x in products if x["category"] == "Electronics" and x["price"] > 100 ]


# 2. Apply a discount of 10% on the price of each product
# consider to use lambda functions
reduced_products = list(map(lambda p: {p["name"], p["price"] * 0.9, p["category"]}, products))
print(reduced_products)

# solution based on iteration (valid if the use of lambda function is not specified in the assignment)
reduced_products = []
for p in products:
    reduced_price = p["price"] * 0.9
    e = {
        "name": p["name"],
        "price": reduced_price,
        "category": p["category"]
    }
    reduced_products.append(e)
    
print(reduced_products)