"""Decorator module provides the @accumulator decorator, which offers a
straightforward way of implementing trivial accumulators through a simple
accumulation function.

For example:

    >>> @accumulator()  # Don't forget the parentheses here!
    ... def Count(accumulator_set, value, datum):
    ...     return value + datum
    ...

The decorator takes care of the boilerplate code required to produce an object
which implements AccumulatorBase.
"""

import functools

from accumulators.accumulator_base import AccumulatorBase


class AccuFromFunc(AccumulatorBase):
    """The AccumulatorWrapper takes a naked function and turns it into
    something which implements AccumulatorBase.
    """

    def __init__(self, accumulator_set, starting_value, fn):
        super(AccuFromFunc, self).__init__(accumulator_set, starting_value)
        self.fn = fn

    def __call__(self, *args, **kwargs):
        # Dispatch stored attributes to the decorated function.
        self.accu = self.fn(self.accumulator_set, self.accu, *args, **kwargs)


def accumulator(depends_on=[], result_name=None, starting_value=0):
    """The accumulator decorator.

    Args:
        depends_on: the list of accumulators on which this value depends
        result_name: the name of the shortcut extractor function for the set
        starting_value: the starting value for the accumulator (defaults to 0)
    """

    def wrapper(fn):

        # The wrapped function acts as a factory: it produces AccumulatorBase
        # instances, and forwards the decorator parameters to the constructor.
        @functools.wraps(fn)
        def wrapped(accumulator_set):
            return AccuFromFunc(accumulator_set, starting_value, fn)

        # We need the Accumulating object to declare its dependencies and its
        # value identifier (if necessary). In this case, we attach this
        # information to the wrapped function.
        wrapped.depends_on = depends_on
        wrapped.value_identifier = result_name
        return wrapped

    return wrapper
