# Copyright 2016-2024 Swiss National Supercomputing Centre (CSCS/ETH Zurich)
# ReFrame Project Developers. See the top-level LICENSE file for details.
#
# SPDX-License-Identifier: BSD-3-Clause

import reframe as rfm


class PinnedTest(rfm.RunOnlyRegressionTest, pin_prefix=True):
    '''A simple base test for verifying that prefix pinning works correctly'''
