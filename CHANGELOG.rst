v0.3.1.1 (2018-01-08)
---------------------

* MarkovChain.distribution() supports a state as a starting distribution.

v0.3.1.0 (2018-01-08)
---------------------

* Code refactor to follow PEP8
* All new Markov Chain module using numpy backend

  * Function definitions largely the same for common functions
  * MarkovChains can now be constructed using additional class functions

* Functions renamed:

  * Table.expected_value -> Table.ev
  * Table.variance -> Table.var

* Unit Tests! Bumped to around 66% code coverage.

v0.2.9.0 (2017-03-19)
---------------------

* Plot_3d

v0.2.8.1 (2017-03-18)
---------------------

* Plot_continuous now accepts python functions too


v0.2.8.0 (2017-03-13)
---------------------

* Updated unconstrain to rearrange_2 and nicefy to rearrange_1

v0.2.7.1 (2017-03-11)
---------------------

* SymPy integration being finalized - added `unconstrain` and updated `declare`

v0.2.7.0 (2017-03-10)
---------------------

* sample renamed to sample_from_dist to avoid conflicts with datascience

v0.2.6.3 (2017-03-09)
---------------------

* Fixed documentation for plots
* plots removed from global

v0.2.6.2 (2017-03-09)
---------------------

* Plot_continuous works with sympy

v0.2.6.1 (2017-03-09)
---------------------

* Plot_continuous now works with any function passed in as func

v0.2.6.0 (2017-03-06)
---------------------

* Wrapper for plotting continuous functions

v0.2.5.1 (2017-03-06)
---------------------

* Beginning to add SymPy integration in *symbolic_math.py*

v0.2.5.0 (2017-02-22)
---------------------

* Added log_probability_of_path

v0.2.4.4 (2017-02-20)
---------------------

* Fixing installation issues

v0.2.4.3a (2017-02-20)
----------------------

* fixed mfpt

v0.2.4.2 (2017-02-16)
---------------------

* Fixed typo in steady_state, not sure how it happened

v0.2.4.1 (2017-02-16)
---------------------

* Documentation fix

v0.2.4.0 (2017-02-13)
---------------------

* Removed T and S from markov chains
* added .column
* states now sorted

v0.2.3.8 (2017-02-13)
---------------------

* Added get target

v0.2.3.7 (2017-02-12)
---------------------

* Deprecation error fix

v0.2.3.6 (2017-02-12)
---------------------

* Distribution now shows states with probability 0

v0.2.3.5 (2017-02-11)
---------------------

* Added show_ev for conditional distributions

v0.2.3.4 (2017-02-11)
---------------------

* state --> states

v0.2.3.3
--------
* Documentation

v0.2.3.2 (2017-02-11)
---------------------
* Changed label for empirical distribution to state
* mc.distribution accepts states

v0.2.3.1 (2017-02-11)
---------------------

* Fixed mean_first_passage_times

v0.2.3.0 (2017-02-11)
---------------------

* Renamed a ton of functions
* Implemented starting conditions

v0.2.2.0 (2017-02-11)
---------------------

* Begin wrapping of pykov

v0.2.1.3 (2017-02-08)
---------------------

* Plots uses plt.bar instead of Table.hist
* Added optional parameter edges=


v0.2.1.2 (2017-02-04)
---------------------

* Added show_ave as optional parameter

v0.2.1.1 (2017-02-04)
---------------------

* Added show_ev and show_sd as optional parameters for plot

v0.2.1.0 (2017-02-04)
---------------------

* Added sample for single variable distributions
* Added CDF for single variable distributions

v0.2.0.0 (2017-02-03)
---------------------

* Pykov

v0.1.8.1 (2017-02-01)
---------------------

* Renamed emp_dist values to proportions rather than probabilities

v0.1.8.0 (2017-01-30)
---------------------

* Added emp_dist to allow for empirical distributions


v0.1.7.6 (2017-01-19)
---------------------

* __version__ instead of version

v0.1.7.5 (2017-01-18)
---------------------

* Joint Distributions no longer give a warning if probabilities rounded to 6 decimal places = 1

v0.1.7.4 (2017-01-17)
---------------------

* Single variable distributions now check that probabilities sum to 1

v0.1.7.3 (2017-01-17)
---------------------

* Plot now adds edge border if there are fewer than 75 bins
* Plot now has an optional parameter edge that accepts a boolean
* Added marginal_dist which returns a single variable distribution

v0.1.7.2 (2017-01-17)
---------------------

* .values is now an alias for .domain

v0.1.7.1 (2017-01-17)
---------------------

* Fixed vertical axis for Plot

v0.1.7.0 (2017-01-16)
---------------------

* Removed marginal_of_X, marginal_of_Y, etc
* conditional_dist_given(given) is now conditional_dist(label, given)

v0.1.6.4 (2017-01-15)
---------------------

* Joint Distribution functions can have arbitrary number of arguments again

v0.1.6.3 (2017-01-15)
---------------------

* fixed a bug in which toJoint just renamed the x-columns rather than changing the order

v0.1.6.2 (2017-01-14)
---------------------

* toJoint now preserve original order

v0.1.6.1 (2017-01-14)
---------------------

* JointDistribution probabilities don't have to sum to 1,

v0.1.6 (2017-01-14)
-------------------

* Added probability_function for JointDistribution
* probability_function now checks number of arguments in pfunc

v0.1.5.1 (2017-01-12)
---------------------

* Added JointDistribution to the init

v0.1.5 (2017-01-12)
-------------------

* Plotting width now works with events and masks
* JointDistribution can now be used with any variable

v0.1.4.3 (2016-12-20)
---------------------

* Changed the colors for plots

v0.1.4.2
--------

* Slight modifications to plot labels

v0.1.4a
-------

* Single distribution plotting moved from the ``plot_dist`` method to the ``Plot`` function
* Multiple distribution plotting moved from the ``Plot`` function to the ``Plots`` function
* Events are now plotted by passing an argument to ``Plot``

v0.1.3
------

* Added joint distributions
* All ``FiniteDistribution`` objects changed to become ``datascience.tables.Table`` objects
* Began renaming

v0.1.2
------
Initial Release