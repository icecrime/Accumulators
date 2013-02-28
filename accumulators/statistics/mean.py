"""Mean module provides to flavors of the mean accumulator.

We violate the Python's conventions of starting function names with a lowercase
letter for a reason: the @accumulator decorator produces a class, which means
that Mean() produces an accumulator object.

The computed accumulator is made available on the AccumulatorSet under the
camelCased attribute name 'mean'.
"""

from __future__ import division

from accumulators.accumulator_base import AccumulatorBase
from accumulators.decorator import accumulator


@accumulator(result_name='mean', starting_value=1,
             depends_on=['accumulators.statistics.Count'])
def ImmediateMean(accumulator_set, value, datum):
    """ImmediateMean updates the mean with each new datum rather than reyling
    on the sum and count upon extraction.
    """
    count = accumulator_set.count()
    return (value * (count - 1) + datum) / count


class Mean(AccumulatorBase):
    """Mean accumulator produces its result at extraction time excusively."""

    depends_on = [
        'accumulators.statistics.Count',
        'accumulators.statistics.Sum'
    ]

    def value(self):
        return self.accumulator_set.sum() / self.accumulator_set.count()
