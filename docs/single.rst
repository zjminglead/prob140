
Single-variable Distributions (``datascience.tables.Table``)
============================================================
.. currentmodule:: prob140



Constucting
-----------

.. ipython:: python

    from prob140 import *
    dist1 = Table().values(np.array([2, 3, 5])).probability(np.array([0.25, 0.5, 0.25]))
    print(dist1)
    dist2 = Table().values(np.arange(1, 8, 2)).probability_function(lambda x: 1/4)
    print(dist2)


.. autosummary::
    :toctree: _autosummary

    Table.values
    Table.probability
    Table.probability_function

Utitilies
---------

.. autosummary::
    :toctree: _autosummary

    Table.prob_event
    Table.event
    Table.cdf
    Table.ev
    Table.sd
    Table.var
    Table.normalized
    Table.sample_from_dist
    emp_dist

Plotting
--------

.. autosummary::
    :toctree: _autosummary

    Plot
    Plots
