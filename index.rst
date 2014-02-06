.. toctree::
   :hidden:

   plot_mercator.rst
   slice_nc.rst
   get_data.rst
   writing_tests.rst

Introduction
------------


This is a set of self-contained python examples that demonstrate
patterns, best practices, modules, etc. that we need frequently in our own work
in atmospheric science.


See :ref:`downloads` to get prerequisites


Examples
________

* `Plotting Aqua AMSR-E surface temps <plot_mercator.html>`_ (plot_mercator.py)

  Uses Basemap and pcolormesh to plot a map of time-averaged tropical SSTs

* `Returning a [time,lat,lon] slice of a netcdf dataset <slice_nc.html>`_  (slice_nc.py)

  Uses netCDF4 to read a time,lat,lon slice from an SST file

* `Writing unit and doc tests with nose <writing_tests.html>`_  (slice_nc.py)

  Calls nose from the slice_nc.py module to run a doctest and a 
  unit test

Index
-----

:ref:`genindex`
