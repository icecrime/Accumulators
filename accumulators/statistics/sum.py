"""Sum module provides the sum accumulator.

We violate the Python's conventions of starting function names with a lowercase
letter for a reason: the @accumulator decorator produces a class, which means
that Sum() produces an accumulator object.

The computed accumulator is made available on the AccumulatorSet under the
camelCased attribute name 'sum'.
"""

from accumulators.decorator import accumulator


@accumulator()
def Sum(accumulator_set, value, datum):
    return value + datum
