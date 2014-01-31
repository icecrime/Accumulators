import unittest

from accumulators import AccumulatorSet, statistics


class TestCount(unittest.TestCase):

    def test_empty_count(self):
        accumulator_set = AccumulatorSet([statistics.Count])
        self.assertTrue(hasattr(accumulator_set, 'count'))

    def test_count(self):
        accumulator_set = AccumulatorSet([statistics.Count])
        for i in range(10):
            accumulator_set(i)
        self.assertEqual(accumulator_set.count(), 10)


class TestMean(unittest.TestCase):

    def test_empty_mean(self):
        accumulator_set = AccumulatorSet([statistics.Mean])
        self.assertTrue(hasattr(accumulator_set, 'mean'))

    def test_mean(self):
        accumulator_set = AccumulatorSet([statistics.Mean])
        for i in range(10):
            accumulator_set(i)
        self.assertEqual(accumulator_set.mean(), 4.5)

    def test_immediate_mean(self):
        accumulator_set = AccumulatorSet([statistics.ImmediateMean])
        for i, expect in zip(range(5), [0, 0.5, 1, 1.5, 2]):
            accumulator_set(i)
            self.assertEqual(accumulator_set.mean(), expect)


class TestMoment(unittest.TestCase):

    def test_empty_moment(self):
        accumulator_set = AccumulatorSet([statistics.Moment(2)])
        self.assertTrue(hasattr(accumulator_set, 'moment2'))

        accumulator_set = AccumulatorSet([statistics.Moment(10)])
        self.assertTrue(hasattr(accumulator_set, 'moment10'))

    def test_moment_2(self):
        accumulator_set = AccumulatorSet([statistics.Moment(2)])
        for i in range(10):
            accumulator_set(i)
        self.assertEqual(accumulator_set.moment2(), 28.5)


class TestSum(unittest.TestCase):

    def test_empty_sum(self):
        accumulator_set = AccumulatorSet([statistics.Sum])
        self.assertTrue(hasattr(accumulator_set, 'sum'))

    def test_sum(self):
        accumulator_set = AccumulatorSet([statistics.Sum])
        for i in range(10):
            accumulator_set(i)
        self.assertEqual(accumulator_set.sum(), 45)

    def test_sum_pow_2(self):
        accumulator_set = AccumulatorSet([statistics.SumPow(2)])
        for i in range(10):
            accumulator_set(i)
        self.assertEqual(accumulator_set.sumPow2(), 285)


class TestVariance(unittest.TestCase):

    def test_empty_variance(self):
        accumulator_set = AccumulatorSet([statistics.Variance])
        self.assertTrue(hasattr(accumulator_set, 'variance'))

    def test_variance(self):
        accumulator_set = AccumulatorSet([statistics.Variance])
        for i in range(10):
            accumulator_set(i)
        self.assertEqual(accumulator_set.variance(), 8.25)
