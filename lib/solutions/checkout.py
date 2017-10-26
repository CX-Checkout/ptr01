# noinspection PyUnusedLocal
def checkout(skus):
    if len(skus) == 0:
        return 0
    counts = {}
    for item in ['A', 'B', 'C', 'D']:
        counts[item] = 0
    for item in skus:
        if item not in ['A', 'B', 'C', 'D']:
            return -1
        counts[item.upper()] += 1
    return ((counts['D'] * 15) +
            (counts['C'] * 20) +
            ((counts['B'] // 2) * 45 + (counts['B'] % 2) * 30) +
            ((counts['A'] // 3) * 130 + (counts['A'] % 3) * 50))


def checkout(skus):
    if len(skus) == 0:
        return 0
    counts = {}
    item_names = ['A', 'B', 'C', 'D', 'E']
    for item in item_names:
        counts[item] = 0
    for item in skus:
        if item not in item_names:
            return -1
        counts[item] += 1
    counts['B'] = counts['B'] - (counts['E'] // 2)
    counts['B'] = 0 if counts['B'] < 0 else counts['B']
    return (
        (counts['E'] * 40) +
        (counts['D'] * 15) +
        (counts['C'] * 20) +
        ((counts['B'] // 2) * 45 + (counts['B'] % 2) * 30) +
    price_a(counts[‘A'])
    )