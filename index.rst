.. toctree::
   :hidden:

   Building the site <build>


Feedback notes  --  2014/Jan/14
_______________________________

* :ref:`build`


Results
=======

* Reproduce CanEsm2 numbers from Figure 2 of 
  `Sherwood et al. <http://www.nature.com/doifinder/10.1038/nature12829>`_:

  * :source:`calc_sherwood.py <calc_sherwood.py>` and :source:`plot_sherwood.py <plot_sherwood.py>`
  
  * omega for warm pool for rist 1000 monts of wap_Amon_CanESM2_esmControl_r1i1p1_190101-225012.nc: :results:`omega plot <sherwood_jan_19.html>`

  * 1000 month area-weighted average of :results:`deltaR and deltaT <sherwood.html>`
    which gives deltaT -7.64 K, deltaR = -22.87 %

  * `Slides fromPhil's January CCCma talk <./cccma_talk.pdf>`_


Overview/review
===============

* Basic definition: latitude-dependent Taylor series expansion as in 
  Feldl and Roe, 2013 :cite:`Feldl13a`:

  .. math::
     :label: feedback     

     -\Delta R_f(x) = - \Delta \left ( \nabla \cdot \vec{F}(x) \right ) + \sum_i \lambda_i (x) \Delta T_s
     + \cal{O}(\Delta T_s^2)

  where :math:`T_s` is either the globally averaged surface temperature :math:`{\overline{T_s}}` or surface temperature 
  average over latitude x.  The feedback parameter for the ith climate
  field is :math:`\lambda_i(x)` is the product of the *radiative kernel* X *the climate response*

  .. math::
     :label: factors

     \lambda_i(x) =  \frac{\Delta R}{\Delta \alpha_i}  \Bigg |_{\alpha_{j,j \neq i}} \frac{ \Delta \alpha_i}{\Delta T_s}

* see also: Roe, 2009 :cite:`Roe09` : Good review of global mean feedback analysis 



Radiative kernels
=================

1) The kernels for Soden et al., 2008 :cite:`Soden08` and  are calculated
   using GFDL radiation code and atmospheric model (AM2p12b) base climatology and 
   archived at http://www.rsmas.miami.edu/personal/bsoden/data/kernels.html in netcdf format.
   The Shell et al., 2008 :cite:`Shell08` using the NCAR CAM are available
   at http://people.oregonstate.edu/~shellk/kernel.html  Vial 2013 :cite:`Vial13` uses
   the Shell 2008 kernel.
  
2) The kernels for Zelinka, 2012a :cite:`Zelinka12a` calculate the radiative response for each
   of the cloud types in the ISCCP CTP-:math:`\tau` bins, for each latitude band and for each
   month.  Given the kernel  K and the change in cloud type :math:`\Delta C` the cloud radiative effect
   for that change is :math:`\Delta R = K \Delta C` and the cloud feedback is 

   .. math::

      f = \frac{\Delta R}{\Delta \overline{T_s}}

   which is a function of cloud top pressure, :math:`\tau`, latitude, longitude, and month.
   

Linear regression
=================

Andrews et al., 2012 :cite:`Andrews12` find the global climate sensitivity using  linear regression 
of :math:`\Delta R` on :math:`\Delta T_s` in equation :eq:`feedback` .   One problem with this
technique is that it assumes time independent forcings, which is probably a poor approximation
according to Armour (2013) :cite:`Armour13`  


Explaining feedbacks
====================

Zhang et al. (2013) :cite:`Zhang13` use single column simulations of a control and and warm case
to show that SCM15 exhibits positive cloud feedback for a trade cumulus cloud regime.  Brient and Bony (2013)
:cite:`Brient13` show that this is due to drying above the boundary layer in the IPSL model.  They show that
they get feedbacks of opposite signs when compare a 4 x :math:`\Delta CO_2` experiment to a +4 K SST
experiment.


Sherwood et al. (2014) :cite:`Sherwood14` look at relative humidity and temperature changes
between 850 and 700 hPa to diagnose low level drying in the CMIP5 ensemble and show that 




Paper downloads
===============

* :cite:`Andrews12`:  `Andrews12: Forcing, feedbacks and climate sensitivity in CMIP5 coupled atmosphere-ocean climate models <http://doi.wiley.com/10.1029/2012GL051607>`_
* :cite:`Armour13`:  `Armour13: Time-Varying Climate Sensitivity from Regional Feedbacks <http://ezproxy.library.ubc.ca/login?url=http://journals.ametsoc.org/doi/abs/10.1175/JCLI-D-12-00544.1>`_
* :cite:`Brient13`:  `Brient13: Interpretation of the positive low-cloud feedback predicted by a climate model under global warming <http://ezproxy.library.ubc.ca/login?url=http://link.springer.com/10.1007/s00382-011-1279-7>`_
* :cite:`Caldwell13`:  `Caldwell13: CMIP3 Subtropical Stratocumulus Cloud Feedback Interpreted through a Mixed-Layer Model <http://journals.ametsoc.org/doi/abs/10.1175/JCLI-D-12-00188.1>`_
* :cite:`Feldl13a`:  `Feldl13a: Four perspectives on climate feedbacks <http://doi.wiley.com/10.1002/grl.50711>`_
* :cite:`Feldl13b`:  `Feldl13b: The Nonlinear and Nonlocal Nature of Climate Feedbacks <http://journals.ametsoc.org/doi/abs/10.1175/JCLI-D-12-00631.1>`_
* :cite:`Gettelman13`:  `Gettelman13: Spatial Decomposition of Climate Feedbacks in the Community Earth System Model <http://journals.ametsoc.org/doi/abs/10.1175/JCLI-D-12-00497.1>`_
* :cite:`Ingram13`:  `Ingram13: A new way of quantifying GCM water vapour feedback <http://link.springer.com/10.1007/s00382-012-1294-3>`_
* :cite:`Roe09`:  `Roe09: Feedbacks, Timescales, and Seeing Red <http://www.annualreviews.org/doi/abs/10.1146/annurev.earth.061008.134734>`_
* :cite:`Sanderson12`:  `Sanderson12: Model-Specific Radiative Kernels for Calculating Cloud and Noncloud Climate Feedbacks <url=http://journals.ametsoc.org/doi/abs/10.1175/JCLI-D-11-00726.1>`_
* :cite:`Shell08`:  `Shell08: Using the Radiative Kernel Technique to Calculate Climate Feedbacks in NCARs Community Atmospheric Model <http://ezproxy.library.ubc.ca/login?url=http://journals.ametsoc.org/doi/abs/10.1175/2007JCLI2044.1>`_
* :cite:`Sherwood14`:  `Sherwood14: Spread in model climate sensitivity traced to atmospheric convective mixing <http://www.nature.com/doifinder/10.1038/nature12829>`_
* :cite:`Soden08`:  `Soden08: Quantifying Climate Feedbacks Using Radiative Kernels <http://ezproxy.library.ubc.ca/login?url=http://journals.ametsoc.org/doi/abs/10.1175/2007JCLI2110.1>`_
* :cite:`Vial13`:  `Vial13: On the interpretation of inter-model spread in CMIP5 climate sensitivity estimates <http://link.springer.com/10.1007/s00382-013-1725-9>`_
* :cite:`Zelinka12`:  `Zelinka12: Climate Feedbacks and Their Implications for Poleward Energy Flux Changes in a Warming Climate <http://ezproxy.library.ubc.ca/login?Url=http://journals.ametsoc.org/doi/abs/10.1175/JCLI-D-11-00096.1>`_
* :cite:`Zelinka12a`:  `Zelinka12a: Computing and Partitioning Cloud Feedbacks Using Cloud Property Histograms. Part I: Cloud Radiative Kernels <http://ezproxy.library.ubc.ca/login?Url=http://journals.ametsoc.org/doi/abs/10.1175/JCLI-D-11-00248.1>`_
* :cite:`Zelinka12b`:  `Zelinka12b: Computing and Partitioning Cloud Feedbacks Using Cloud Property Histograms. Part II: Attribution to Changes in Cloud Amount, Altitude, and Optical Depth <http://ezproxy.library.ubc.ca/login?Url=http://journals.ametsoc.org/doi/abs/10.1175/JCLI-D-11-00249.1>`_
* :cite:`Zelinka13`:  `Zelinka13: Contributions of Different Cloud Types to Feedbacks and Rapid Adjustments in CMIP5 <http://ezproxy.library.ubc.ca/login?Url=http://journals.ametsoc.org/doi/abs/10.1175/JCLI-D-12-00555.1>`_
* :cite:`Zhang13`:  `Zhang13: CGILS: Results from the first phase of an international project to understand the physical mechanisms of low cloud feedbacks in single column models <http://doi.wiley.com/10.1002/2013MS000246>`_


.. rubric:: Citations

.. bibliography:: feedbacks.bib
   :style: unsrt
