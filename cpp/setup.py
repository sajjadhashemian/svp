from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension(
        "svp",  # Module name
        ["svp.cpp"],  # Source file
        include_dirs=["/opt/anaconda3/envs/fplll/include/eigen3"],  # Path to Eigen headers
        cxx_std=17,  # C++ standard
    ),
]

setup(
    name="svp",
    version="0.1",
    description="A Pybind11 wrapper for the Decision-SVP problem",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)

# python setup.py build_ext --inplace