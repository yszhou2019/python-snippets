from setuptools import setup

setup(
    name="ys-filter"
    , version="v1.0"
    , description="ys-filter package"
    , packages=["ys_filter"]
    , package_dir={'ys_filter' : 'src',         # find `ys_filter` packages under `src`
                   '' : 'src'}                  # find other packages under `src`
    , package_data={'ys_filter': ['config'],    # find data files 'config' of `ys_filter`, that is, under `src`, copy into `ys_filter`
                    '' : ['yaml']}              # find data files `yaml` under `src`, but copy into ROOT_DIRECTORY
    , install_requires=[
        "pyjwt"
        , "requests"
    ]
)
