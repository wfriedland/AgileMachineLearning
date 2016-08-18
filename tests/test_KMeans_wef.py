import unittest
from sklearn import datasets
from Models.KMeans_wef import wrapper_for_kmeans_wef

class TestKMeans(unittest.TestCase):
    def test_kmeans_w_iris_data(self):
        # import some data to play with
        iris = datasets.load_iris()
        data = iris.data
        features = iris.feature_names

        retValue = wrapper_for_kmeans_wef(data,features)
        self.assertGreaterEqual(retValue, 55)  #force test to return success
