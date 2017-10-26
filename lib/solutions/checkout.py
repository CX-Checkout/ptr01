# noinspection PyUnusedLocal
def checkout(skus):
    if len(skus) == 0:
        return -1
    counts = {}
    for item in ['A', 'B', 'C', 'D']:
        counts[item] = 0
    for item in skus:
        counts[item.upper()] += 1
    return ((counts['D'] * 15) +
            (counts['C'] * 20) +
            ((counts['B'] // 2) * 45 + (counts['B'] % 2) * 30) +
            ((counts['A'] // 3) * 130 + (counts['A'] % 3) * 50))
