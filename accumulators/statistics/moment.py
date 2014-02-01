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

from __future__ import division

from accumulators.decorator import Accumulator
from accumulators.statistics.sum import sumpow


def moment(n):
    depends_on = ['accumulators.statistics.count', sumpow(n)]
    result_name = 'moment{}'.format(n)

    @Accumulator.lazy(result_name=result_name, depends_on=depends_on)
    def moment_n(accumulator_set):
        count = accumulator_set.count()
        if count == 0:
            return 0
        return getattr(accumulator_set, sumpow(n).value_identifier)() / count

    return moment_n
