# noinspection PyUnusedLocal
def price_a(a):
    price = 0
    price += (a // 5) * 200
    a = a % 5
    price += (a // 3) * 130
    a = a % 3
    price += a * 50
    return price

def price_discounts(counts):
    price = 0
    for sku_disc in DISCOUNTS.keys():
        discounts = DISCOUNTS[sku_disc]
        item_count_disc = reversed(sorted(discounts.keys()))
        for item_count in item_count_disc:
            price += (counts[sku_disc] // item_count) * dis
            counts[sku_disc] = counts[sku_disc] % item_count
    return price

def price_all(counts):
    price = 0
    for sku in counts.keys():
        price += counts[sku] * PRICE_LIST[sku]
    return price


def checkout(skus):
    if len(skus) == 0:
        return 0
    counts = {}
    item_names = PRICE_LIST.keys()
    for item in item_names:
        counts[item] = 0
    for item in skus:
        if item not in item_names:
            return -1
        counts[item] += 1
    price = 0
    price += (price_freebies(counts) +
              price_discounts(counts) +
              price_all(counts))
    return price
