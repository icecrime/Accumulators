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

import sys


class AccumulatorSet(object):

    def __init__(self, accumulators):
        self.accumulators = []
        self.accumulators_types = set()
        [self._register_accumulator(accu) for accu in accumulators]

    def __call__(self, datum, weight=1.):
        # Forward the provided datum to each registered accumulator.
        for accumulator in self.accumulators:
            accumulator(datum * weight)
        return self

    def _make_attribute_name(self, accu_type):
        return accu_type.__name__[0].lower() + accu_type.__name__[1:]

    def _register_accumulator(self, accu_type):
        # There is no point in registering multiple times a single kind of
        # accumulators.
        accu_type = self._resolve_accumulator_type(accu_type)
        if accu_type in self.accumulators_types:
            pass

        # Iterate on each accumulator's dependency, and recurse to register
        # them. Note that we recurse _before_ registering the accumulator being
        # examined: we need the dependencies to be inserted first.
        for dependency in getattr(accu_type, 'depends_on', []):
            self._register_accumulator(dependency)
        self.accumulators_types.add(accu_type)

        # Instantiate the accumulator, store it to forward the future datums
        # that will be provided.
        accu_obj = accu_type(self)
        self.accumulators.append(accu_obj)

        # Register the extraction function.
        self._register_accumulator_extractor(accu_type, accu_obj)

    def _register_accumulator_extractor(self, accu_type, accu_obj):
        # Register a function on the set to easily retrieve the accumulator's
        # value. We use the accumulator type with a lowercase first letter for
        # the function name, unless specified otherwise.
        value_identifier = getattr(accu_type, 'value_identifier', None)
        if not value_identifier:
            value_identifier = self._make_attribute_name(accu_type)
        self.__dict__[value_identifier] = accu_obj.value

    def _resolve_accumulator_type(self, accu_type):
        # Accumulator type may be expressed as a string.
        str_type = str if sys.version_info[0] == 3 else basestring
        if isinstance(accu_type, (str_type)):
            split = accu_type.split('.')
            type_ = __import__('.'.join(split[:-1]))
            for component in split[1:]:
                type_ = getattr(type_, component)
            accu_type = type_
        return accu_type
