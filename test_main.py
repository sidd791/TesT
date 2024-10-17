import func

class Test:
    def test_addition(self):
        assert 4 == func.add_num(2, 2)

    def test_difference(self):
        assert 2 == func.difference_num(2, 4)

    def test_product(self):
        assert 4 == func.product_num(2, 2)