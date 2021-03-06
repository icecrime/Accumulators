# Copyright 2013 Arnaud Porterie
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Decorator module provides the @accumulator decorator, which offers a
straightforward way of implementing trivial accumulators through a simple
accumulation function.

For example:

    >>> @Accumulator.immediate()  # Don't forget the parentheses here!
    ... def count(accumulator_set, value, datum):
    ...     return value + datum
    ...

The decorator takes care of the boilerplate code required to produce an object
which implements AccumulatorBase.
"""

import functools

from accumulators.accumulator_base import AccumulatorBase


class ImmediateAccuFromFunc(AccumulatorBase):
    """The ImmediateAccumulatorWrapper takes a naked function and turns it into
    something which implements AccumulatorBase.
    """

    def __init__(self, accumulator_set, starting_value, fn):
        super(ImmediateAccuFromFunc, self).__init__(accumulator_set, starting_value)
        self.fn = fn

    def __call__(self, *args, **kwargs):
        # Dispatch stored attributes to the decorated function.
        self.accu = self.fn(self.accumulator_set, self.accu, *args, **kwargs)


class LazyAccuFromFunc(AccumulatorBase):
    """The LazyAccumulatorWrapper takes a naked function and turns it into
    something which implements AccumulatorBase.
    """

    def __init__(self, accumulator_set, starting_value, fn):
        super(LazyAccuFromFunc, self).__init__(accumulator_set, starting_value)
        self.fn = fn

    def __call__(self, *args, **kwargs):
        pass  # No immediate accumulation

    def value(self):
        # Dispatch stored attributes to the decorated function.
        return self.fn(self.accumulator_set)


class Accumulator(object):

    __slots__ = ()

    @staticmethod
    def immediate(depends_on=[], result_name=None, starting_value=0):
        """Immediate accumulator decorator.

        Args:
            depends_on: list of accumulators on which this value depends
            result_name: name of the shortcut extractor function for the set
            starting_value: starting value for the accumulator (defaults to 0)
        """
        return Accumulator._make_wrapper(ImmediateAccuFromFunc, depends_on,
                                         result_name, starting_value)

    @staticmethod
    def lazy(depends_on=[], result_name=None):
        """Lazy accumulator decorator.

        Args:
            depends_on: list of accumulators on which this value depends
            result_name: name of the shortcut extractor function for the set
        """
        return Accumulator._make_wrapper(LazyAccuFromFunc, depends_on,
                                         result_name, starting_value=0)


    @staticmethod
    def _make_wrapper(accu_type, depends_on, result_name, starting_value):

        def _wrapper(fn):
            # The wrapped function acts as factory: it produces AccumulatorBase
            # instances, and forwards decorator parameters to the constructor.
            @functools.wraps(fn)
            def wrapped(accumulator_set):
                return accu_type(accumulator_set, starting_value, fn)

            # We need the Accumulating object to declare its dependencies and
            # its value identifier (if necessary). In this case, we attach this
            # information to the wrapped function.
            wrapped.depends_on = depends_on
            wrapped.value_identifier = result_name
            return wrapped

        return _wrapper
