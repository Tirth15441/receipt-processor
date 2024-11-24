def calculate_points(receipt):
    points = 0

    # 1. Points for alphanumeric characters in retailer name
    points += sum(c.isalnum() for c in receipt['retailer'])

    # 2. Points for round dollar total
    if receipt['total'].split('.')[1] == "00":
        points += 50

    # 3. Points for multiples of 0.25
    if float(receipt['total']) % 0.25 == 0:
        points += 25

    # 4. Points for pairs of items
    points += (len(receipt['items']) // 2) * 5

    # 5. Points for item descriptions
    for item in receipt['items']:
        if len(item['shortDescription'].strip()) % 3 == 0:
            points += -(-float(item['price']) * 0.2 // 1)  # Ceiling rounding

    # 6. Points for odd purchase date
    if int(receipt['purchaseDate'].split('-')[2]) % 2 != 0:
        points += 6

    # 7. Points for purchase time
    hour, minute = map(int, receipt['purchaseTime'].split(':'))
    if 14 <= hour < 16:
        points += 10

    return points
