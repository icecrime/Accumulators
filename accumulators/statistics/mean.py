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
