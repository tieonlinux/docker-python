import unittest

import pandas as pd
from pyarrow.feather import read_feather

class TestPandas(unittest.TestCase):    
    def test_read_csv(self):
        data = pd.read_csv("/input/tests/data/train.csv")

        self.assertEqual(100, len(data.index))

    def test_read_feather(self):
        # Python 3.7 requires PyArrow >= 0.11.0
        # pandas.read_feather(...) support for PyArrow >= 0.11.0 has been added in pandas 0.24 
        # But tsfresh requires pandas<=0.23.4
        # pyarrow.feather.read_feather should be used instead.
        # TODO(rosbo): the twosigmanews lib will need to be updated.
        # data = pd.read_feather("/input/tests/data/feather-0_3_1.feather")
        data = read_feather("/input/tests/data/feather-0_3_1.feather")

        self.assertEqual(10, data.size)
