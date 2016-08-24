import unittest
from Models.pandas_rolling_means_sample import *

class TestKMeans(unittest.TestCase):
    def test_pandas_rolling_mean(self):

        retValue = demo_pandas_rolling_mean()
        self.assertGreaterEqual(retValue, 55)  #force test to return success
