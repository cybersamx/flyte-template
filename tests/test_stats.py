import unittest

import project.core.data as data


class TestStats(unittest.TestCase):
    def test_load_wine(self):
        df = data.get_data()
        self.assertEqual(178, len(df.index))
        self.assertEqual(14, len(df.columns))


if __name__ == '__main__':
    unittest.main()
