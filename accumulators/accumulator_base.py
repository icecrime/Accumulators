"""This module provides the AccumulatorBase object."""


class AccumulatorBase(object):
    """Abstract base class for all accumulators."""

    def __init__(self, accumulator_set, start_value=0):
        """Initializes an AccumulatorBase.

        Args:
            accumulator_set: the containing AccumulatorSet instance
            start_value: the initial accumulator value (defaults to 0)
        """
        self.accu = start_value
        self.accumulator_set = accumulator_set

    def __call__(self, datum, weight=1.):
        """Accumulates the provided datum.

        Args:
            datum: the new datum to accumulate
            weight: the weight associated with the datum (defaults to 1)
        """
        pass

    def value(self):
        """Extracts the accumulator value. Extracting the value should not
        prevent further accumulations.

        Returns:
            The accumulator value.
        """
        return self.accu
