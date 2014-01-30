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

from __future__ import absolute_import, division

from accumulators.accumulator_base import AccumulatorBase
from accumulators.statistics.sum import SumPow


def Moment(order):
    """Moment function generates an accumulator implementation according to the
    specified order. The return accumulator type produces its value upon
    extraction time exclusively.
    """

    class MomentImpl(AccumulatorBase):

        # The moment calculation depends on the count, and the sum of values
        # raised to the appropriate power (i.e.: moment of order 2 is the sum
        # of squares divded by the count).
        depends_on = ['accumulators.statistics.Count', SumPow(order)]

        # The accumulator result is identified by 'momentX' where X is the
        # statistics order.
        value_identifier = 'moment{}'.format(order)

        def value(self):
            sumPowAttr = SumPow(order).value_identifier
            return (getattr(self.accumulator_set, sumPowAttr)() /
                        self.accumulator_set.count())

    return MomentImpl
