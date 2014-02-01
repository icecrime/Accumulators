import unittest

from accumulators import AccumulatorSet, statistics


class TestCount(unittest.TestCase):

    def test_empty_count(self):
        accumulator_set = AccumulatorSet(statistics.count)
        self.assertTrue(hasattr(accumulator_set, 'count'))
        self.assertEqual(accumulator_set.count(), 0)

    def test_count(self):
        accumulator_set = AccumulatorSet(statistics.count)
        for i in range(10):
            accumulator_set(i)
        self.assertEqual(accumulator_set.count(), 10)


class TestMean(unittest.TestCase):

    def test_empty_immediate_mean(self):
        accumulator_set = AccumulatorSet(statistics.immediate_mean)
        self.assertTrue(hasattr(accumulator_set, 'mean'))
        self.assertEqual(accumulator_set.mean(), 0)

    def test_empty_mean(self):
        accumulator_set = AccumulatorSet(statistics.mean)
        self.assertTrue(hasattr(accumulator_set, 'mean'))
        self.assertEqual(accumulator_set.mean(), 0)

    def test_mean(self):
        accumulator_set = AccumulatorSet(statistics.mean)
        for i in range(10):
            accumulator_set(i)
        self.assertEqual(accumulator_set.mean(), 4.5)

    def test_immediate_mean(self):
        accumulator_set = AccumulatorSet(statistics.immediate_mean)
        for i, expect in zip(range(5), [0, 0.5, 1, 1.5, 2]):
            accumulator_set(i)
            self.assertEqual(accumulator_set.mean(), expect)


class TestMoment(unittest.TestCase):

    def test_empty_moment(self):
        accumulator_set = AccumulatorSet(statistics.moment(2))
        self.assertTrue(hasattr(accumulator_set, 'moment2'))
        self.assertEqual(accumulator_set.moment2(), 0)

        accumulator_set = AccumulatorSet(statistics.moment(10))
        self.assertTrue(hasattr(accumulator_set, 'moment10'))
        self.assertEqual(accumulator_set.moment10(), 0)

    def test_moment_2(self):
        accumulator_set = AccumulatorSet(statistics.moment(2))
        for i in range(10):
            accumulator_set(i)
        self.assertEqual(accumulator_set.moment2(), 28.5)


class TestSum(unittest.TestCase):

    def test_empty_sum(self):
        accumulator_set = AccumulatorSet(statistics.sum)
        self.assertTrue(hasattr(accumulator_set, 'sum'))
        self.assertEqual(accumulator_set.sum(), 0)

    def test_sum(self):
        accumulator_set = AccumulatorSet(statistics.sum)
        for i in range(10):
            accumulator_set(i)
        self.assertEqual(accumulator_set.sum(), 45)

    def test_sum_pow_2(self):
        accumulator_set = AccumulatorSet(statistics.sumpow(2))
        for i in range(10):
            accumulator_set(i)
        self.assertEqual(accumulator_set.sumpow2(), 285)


class TestVariance(unittest.TestCase):

    def test_empty_variance(self):
        accumulator_set = AccumulatorSet(statistics.variance)
        self.assertTrue(hasattr(accumulator_set, 'variance'))
        self.assertEqual(accumulator_set.variance(), 0)

    def test_variance(self):
        accumulator_set = AccumulatorSet(statistics.variance)
        for i in range(10):
            accumulator_set(i)
        self.assertEqual(accumulator_set.variance(), 8.25)
