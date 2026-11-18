from tickitdb import calculate_price

def test_calculate_price():
    assert calculate_price(200, 2) == 400