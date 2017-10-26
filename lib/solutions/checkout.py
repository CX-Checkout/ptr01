# noinspection PyUnusedLocal

FREEBIES ={
    'E': {2: 'B'},
    'F': {2: 'F'},
    'N': {3: 'M'},
    'R': {3: 'Q'},
    'U': {3: 'U'}
}

def price_freebies(counts):
    price = 0
    for sku_free in FREEBIES.keys():
        freebies = FREEBIES[sku_free]
        item_counts = freebies.keys()
        for item_count in item_counts:
            target_sku = freebies[item_count]
            while (counts[sku_free] >= item_count):
                counts[sku_free] -= item_count
                price += item_count * PRICE_LIST[sku_free]
                counts[target_sku] = (counts[target_sku] - 1) if
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
