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
