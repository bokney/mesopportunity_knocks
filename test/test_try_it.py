
#  ¿ how to approach ? #

import pytest
from src.try_it import get_cat_image

class Test_get_cat_image:
    
    def test_function_returns_string(self):
        result = get_cat_image()
        assert isinstance(result, str)

    def test_function_returns_jpg(self):
        result = get_cat_image()
        assert result[-4:] == ".jpg"
