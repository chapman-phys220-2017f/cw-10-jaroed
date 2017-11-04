#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import estimate_e as ee
import nose

"""Module to test the code in estimate_e.py"""

def test_approx_e_1():
    """Tests our function for a simple case where we sample with 100 points."""
    actual = 2.71828
    # Approximating
    est = ee.approx_e(100)
    # Debug message
    print("We expected :",actual," but got: ",est)
    # Asserting
    nose.tools.assert_almost_equal(actual,est,0)

def test_approx_e_2():
    """Tests our function for a much more accurate case in which we sample with
    10,000,000 points."""
    actual = 2.71828
    # Approximating
    est = ee.approx_e(10000000)
    # Debug message
    print("We expected: ",actual," but got: ",est)
    # Asserting
    nose.tools.assert_almost_equal(actual,est,1)
