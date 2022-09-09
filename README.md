# wetwin
Collaborative digital twin modelling

## First test for showing results on the web

Here we explore the use of jupyter notebooks, together with the package voila and the online service of mybinder.org to create a dashboard directly from a github repository with a jupyter notebook. The aim is 
to test if the development of a dashboard

Show the jupyter notebook online at mybinder.org
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/robot144/wetwin/HEAD?labpath=rhine_meuse_delta_v1.ipynb)

You can also directly launch a notebook as an app in binder.
- for show_timeseries_from_nextcloud.ipynb [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/robot144/wetwin/HEAD?urlpath=voila%2Frender%2Frhine_meuse_delta_v1.ipynb)

There are several other notebooks with tests and examples for individual components:
- for widgets.ipynb [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/robot144/wetwin/HEAD?urlpath=voila%2Frender%2Fwidgets.ipynb)
- for show_timeseries.ipynb [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/robot144/wetwin/HEAD?urlpath=voila%2Frender%2Fshow_timeseries.ipynb)


### Some technical notes

- Voila is a package that strips the code and editing functionality from a notebook and just shows the text and results. Together with ipywidgets you can make the page interactive and make the code respond to the buttons that you add.
- you can install voila also locally (with pip or conda) and run eg `voila widgets.ipynb` to preview the app locally first.
- The standard netCDF4 library cannot read from a regular download, ie one that is not backed by opendap. Using Xarray, this can be done however. The advantage is that a regular web-url will be enough to access the netcdf file. This can for example easily be done using research-drive from surfsara (https://researchdrive.surfsara.nl/index.php/login), which can be obtained together with an account on Snellius or Lisa, or surfdrive as available to all employees of the TU Delft (surfdrive.surf.nl). It is also possible to rent storage commercially (eg at hetzner.de storage share 3 to 5 euro/Tb/month). There re many options.

### About Piodide or JupiterLite versus binder

In the (near) future, it would be nice if the dashboard could fully run in the browser, so the code could be started from a static website. Running the code in the browser is based on WebAssembly, a new technology where eg c-code can be executed in the browser. This technology is being developed at a fast pace, but now in the summer of 2022, many python modules are only partially available. We'll aim to test the deashboards on Jupiterlite, and keep track of when it becomes possible to make the dashboard available through this route to a sufficient extent. 

The following websites show some of the relevant technology:
- [Try JupiterLite in the browser](https://jupyterlite.github.io/demo) Note that you can select the raw format in for a jupyter notebook in a repo and paste the url in the demo version to try it.
- [Explanation of piodide](https://github.com/pyodide/pyodide)

The current status (august 2022) seems to be that binary data (like netcdf and zarr) is not workin enough to use these, downloading data and visualisation. On the other hand, the developments are moving quickly. Especially xarray and zarr are partially available.
Our strategy can be to continue with binder for production and to keep track of what's working in jupyterlite. Things are likely to work faster if we use libraries that are active on jupyterlite.

