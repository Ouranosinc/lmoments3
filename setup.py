from setuptools import setup
import versioneer


requirements = open("requirements.txt").readlines()
readme = open("README.rst").read()

setup(
    name='lmoments3',
    author="Florenz A.P. Hollebrandse",
    author_email="f.a.p.hollebrandse@protonmail.ch",
    packages=['lmoments3'],
    python_requires=">=3.8",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    classifiers=[
      "Development Status :: 5 - Production/Stable",
      "Intended Audience :: Developers",
      "Intended Audience :: Science/Research",
      "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
      "Natural Language :: English",
      "Operating System :: OS Independent",
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3.8",
      "Programming Language :: Python :: 3.9",
      "Programming Language :: Python :: 3.10",
      "Topic :: Scientific/Engineering :: Mathematics"
    ],
    description="A library extend scipy with L-moments to calculate optimal parameters for a number of distributions",
    keywords=["lmoments3", "statistics"],
    long_description=readme,
    long_description_content_type="text/x-rst",
    install_requires=requirements,
    zip_safe=False,
)
