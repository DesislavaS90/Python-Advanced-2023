def shop_from_grocery_list(budget, products, *args):

    bought_products = []

    for p in args:
        if budget < float(p[1]):
            break
        if p[0] in bought_products:
            continue
        if p[0] in products and budget >= float(p[1]):
            budget -= float(p[1])
            bought_products.append(p[0])
            products.remove(p[0])
    if not products:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(products)}"


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))