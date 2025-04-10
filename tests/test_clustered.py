import unittest
from clustered_subset_count import clustered_subset_count

class TestClusteredSubsetCount(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(clustered_subset_count(5, 3, 2), 8)

    def test_full_clustering(self):
        self.assertEqual(clustered_subset_count(4, 2, 10), 6)

    def test_zero_cluster_distance(self):
        self.assertEqual(clustered_subset_count(4, 2, 0), 0)

    def test_single_element(self):
        self.assertEqual(clustered_subset_count(1, 1, 0), 1)

    def test_edge_cluster(self):
        self.assertEqual(clustered_subset_count(2, 2, 1), 1)

    def test_large_d_value(self):
        result = clustered_subset_count(6, 3, 100)
        expected = 20
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
