# noinspection PyUnusedLocal
import string

PRICE_LIST = [50, 30, 20, 15, 40, 10, 20, 10, 35, 60, 80, 90, 15, 40, 10, 50, 30, 50, 30, 20, 40, 50, 20, 90, 10, 50]
PRICE_LIST = dict(zip(string.ascii_uppercase, PRICE_LIST))
DISCOUNTS = {
    'A': {5: 200, 3: 130},
    'B': {2: 45},
    'H': {10: 80, 5: 45},
    'K': {2: 150},
    'P': {5: 200},
    'Q': {3: 80},
    'V': {3: 130, 2: 90}
}

FREEBIES = {
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
                counts[target_sku] = (counts[target_sku] - 1) if counts[target_sku] > 0 else counts[target_sku]
    return price


def price_discounts(counts):
    price = 0
    for sku_disc in DISCOUNTS.keys():
        discounts = DISCOUNTS[sku_disc]
        item_count_disc = reversed(sorted(discounts.keys()))
        for item_count in item_count_disc:
            price += (counts[sku_disc] // item_count) * discounts[item_count]
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
    price += (
              price_any(counts) +
              price_freebies(counts) +
              price_discounts(counts) +
              price_all(counts))
    return price
