import unittest
import pandas as pd


data = pd.DataFrame({
    'industry': ['Bollywood', 'Bollywood', 'Hollywood', 'Hollywood'],
    'imdb_rating': [8.0, 7.0, 9.0, 8.5]
})

def calculate_avg_rating(df):
    return df.groupby('industry')['imdb_rating'].mean()

class TestCalculateAvgRating(unittest.TestCase):
    def test_avg_rating(self):
        result = calculate_avg_rating(data)
        expected = pd.Series({'Bollywood': 7.5, 'Hollywood': 8.75})
        expected.index.name = 'industry'          
        expected.name = 'imdb_rating'              
        pd.testing.assert_series_equal(result, expected)

if __name__ == '__main__':
    unittest.main()
