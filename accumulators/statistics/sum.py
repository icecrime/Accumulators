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


def SumPow(power):
    @accumulator(result_name='sumPow{}'.format(power))
    def _impl(accumulator_set, value, datum):
        return value + pow(datum, power)
    return _impl
