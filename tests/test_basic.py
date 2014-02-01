try:
    import unittest.mock as mock
except ImportError:
    import mock

import unittest

from accumulators import AccumulatorSet


class TestBasic(unittest.TestCase):

    def test_accu_dependency(self):
        accu, depend = mock.MagicMock(), mock.MagicMock()
        accu.depends_on = [depend]
        accumulator_set = AccumulatorSet(accu)

        accu.assert_called_with(accumulator_set)
        depend.assert_called_with(accumulator_set)

    def test_accu_extractor(self):
        accu = mock.MagicMock()
        accu.value_identifier = 'test'
        accumulator_set = AccumulatorSet(accu)

        self.assertTrue(hasattr(accumulator_set, 'test'))

    def test_accu_call(self):
        accu = mock.MagicMock()
        accuSet = AccumulatorSet(accu)
        accu.reset_mock()

        accuSet(1.)
        self.assertEqual(accu.mock_calls, [mock.call()(1.)])

    def test_accu_call_weight(self):
        accu = mock.MagicMock()
        accuSet = AccumulatorSet(accu)
        accu.reset_mock()

        accuSet(1., 2.)
        self.assertEqual(accu.mock_calls, [mock.call()(2.)])
