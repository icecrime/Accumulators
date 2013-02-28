"""Count module provides the count accumulator.

We violate the Python's conventions of starting function names with a lowercase
letter for a reason: the @accumulator decorator produces a class, which means
that Count() produces an accumulator object.

The computed accumulator is made available on the AccumulatorSet under the
camelCased attribute name 'count'.
"""

from accumulators.decorator import accumulator


@accumulator()
def Count(accumulator_set, value, datum):
    return value + 1
