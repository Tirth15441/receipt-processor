from points_calculator import calculate_points

def test_calculate_points():
    receipt = {
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            { "shortDescription": "Mountain Dew", "price": "6.49" }
        ],
        "total": "6.49"
    }
    points = calculate_points(receipt)
    assert points > 0  
