from setuptools import setup

setup(
    name="ys-filter"
    , version="v1.0"
    , description="ys-filter package"
    , packages=["ys_filter"]
    , package_dir={'' : 'src'}
    , install_requires=[
        "pyjwt"
        , "requests"
    ]
)
