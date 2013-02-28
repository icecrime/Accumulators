Accumulators
=======

[![Build Status](https://travis-ci.org/icecrime/Accumulators.png)](https://travis-ci.org/icecrime/Accumulators)

Overview
-------------

Accumulators is a statistical accumulator package strongly inspired by [Boost.Accumulators](http://www.boost.org/doc/libs/1_53_0/doc/html/accumulators.html). It is in *very* early development stage, and I'm pretty much a Python's noob, so any help and/or constructive comments would be appreciated.


Usage
-------------

    >>> from accumulators import AccumulatorSet, statistics
    >>> accu_set = AccumulatorSet([statistics.Mean, statistics.Count])
    >>> accu_set(1.1)(4.2)(12.8)
    <accumulators.accumulator_set.AccumulatorSet object at 0x1059b1bd0>
    >>> accu_set.mean()
    6.033333333333334
    >>> accu_set.count()
    3
