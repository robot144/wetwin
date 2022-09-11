# wetwin
Collaborative digital twin modelling

## First test for showing results on the web

Here we explore the use of jupyter notebooks, together with the package voila and the online service of mybinder.org to create a dashboard directly from a github repository with several jupyter notebooks. The aim is 
to test if the development of a dashboard is both feasible and eficient in this way.

Currently there is one demo noteook:

1. *Rhine Meuse outflow and delta* The notebook shows data from a 3D hydrodynamics simulation from a Delft3-FM model with arelatively coarse grid. This ZUNO-RMM model is being developed currently to support the developement of data-assimilation methods for the region. You can run the notebook `rhine_meuse_delta_v1.ipynb` also at mybinder using this link: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/robot144/wetwin/HEAD?labpatforh=rhine_meuse_delta_v1.ipynb) This will trigger the generation of a docker container with jupiterlab and this repository, which is then started in the cloud. You'll only need a modern browser locally. This will show the notebook and allows you to run and edit the code.
You can also directly launch a notebook as an app in binder. [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/robot144/wetwin/HEAD?urlpath=voila%2Frender%2Frhine_meuse_delta_v1.ipynb)

In addition to this demo, there are a few notebooks that illustrate aspects of the tools that are used. They are simply notes and tests for a particular technique. most likely not all cells are working at any time.

- for ipywidgets widgets.ipynb [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/robot144/wetwin/HEAD?urlpath=widgets.ipynb)
- for ipyleaflet maps maps.ipynb [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/robot144/wetwin/HEAD?urlpath=maps.ipynb)
- for xarray for access to zarr data over internet, zunormm_data.ipynb [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/robot144/wetwin/HEAD?urlpath=zunormm_data.ipynb)


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

