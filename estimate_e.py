#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

"""Code module to approximate the value of e using a Monte Carlo technique."""

def approx_e(N):
    """approx_e(N)
    Input parameters:
        N - integer, number of sample points.
    Output:
        num - float, approximation of e

    This function becomes more accurate as N grows larger.  approx_e places N random points
    within the box of x in [0,1] and y in [0,3].  The function then counts the number of points
    that lie underneath the curve e^x.  The area of the box is A = 3, and the area underneath the
    curve e^x from 0 to 1 is B = e - 1.  We see that the ratio of number of points and the ratio
    of areas should resemple the same number.  Using this idea, we calculate for e using the number
    of points underneath the curve and the total number of points."""
    # Generate N random x and y coordinates within the box of x in [0,1] and y in [0,3].
    xs = np.random.uniform(0,1,N)
    ys = np.random.uniform(0,3,N)
    # Count how many points lie underneath the function f(x) = exp(x)
    under = np.where(np.exp(xs) > ys, 1, 0).sum()
    # Compute e
    num = (3*under/N)+1
    return num
