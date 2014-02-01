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

"""Count module provides the count accumulator.

We violate the Python's conventions of starting function names with a lowercase
letter for a reason: the @accumulator decorator produces a class, which means
that Count() produces an accumulator object.

The computed accumulator is made available on the AccumulatorSet under the
camelCased attribute name 'count'.
"""

from accumulators.decorator import Accumulator


@Accumulator.immediate()
def count(accumulator_set, value, datum):
    return value + 1
