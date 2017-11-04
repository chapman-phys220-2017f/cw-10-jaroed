# PHYS220 CW 10 

**Author(s):** **Jarod Penniman, Jared Love**

[![Build Status](https://travis-ci.org/chapman-phys220-2017f/cw-10-jaroed.svg?branch=master)](https://travis-ci.org/chapman-phys220-2017f/cw-10-jaroed)

## Specification

1. Go through the example notebook and code with your group. Discuss and make sure you understand what is happening.
1. Create a new module `estimate_e.py`. Using the fact that $\int_0^1 e^x dx = e - 1$, estimate the value of $e$ using a Monte Carlo technique. (Hint: think about how $\pi$ is estimated in the notebook.) Test your implementation using a test module `test_estimate_e.py` that passes with Travis.
1. Complete the exercise at the bottom of the notebook. Be sure to preserve the existing code such that the rest of the notebook still runs unmodified.

Pro-tip: using git to manage conflicts on Jupyter notebooks is a pain. I recommend delegating one person from your group to edit the notebook, to avoid merge conflicts.

## Assessment

Analyze in this section what you found useful about this assignment in your own words. Include any lingering questions or comments that you may have.

**The assignment was a nice refresher on random number generators, and a creative way of obtaining approximations.  My question would be the following...  everytime someone runs the test function, it in turn runs the code module.  The code module does not have a set output, since it uses a random number generator.  To be safe, I lowered the accuracy needed for the test to pass.  Is there a way to ensure an accurate result and trust that the test will not fail (other than trusting mathematics and probabilities)?  It is a possibility, after all, that the function could randomly select all points above the curve and thus estimate e=0, with a perfectly fine code module.  In this case the test would fail even though the code is good.  A very very low chance but still worth asking!**

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

**Jarod Penniman, Jared Love**
