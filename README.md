# Deep learning approaches on WSIs, IHC, H&E, etc.

[![Build
Status](https://travis-ci.org/cechlauren/HW3_skeleton.svg?branch=master)](https://travis-ci.org/cechlauren/HW3_skeleton)

U-net project with testing.

## STRUCTURE
```
.
├── README.md
├── intro
├── requirements.txt
│   ...
├── Acquisition
│   ├── __main__.py
│   ├── *.groovy
│   └── automation.py
├── test
│    ├── tbd
│    └── tbd
└── evaluation
    ├── tbd
    └── tbd
```

## USAGE

To use the package, first make a new conda environment and activate it

```
conda create -n exampleenv python=3
source activate exampleenv
```

then run

```
conda install --yes --file requirements.txt
```

to install all the dependencies in `requirements.txt`. Then the package's
main function (located in `DeeeepLearning/acquisition/__main__.py`) can be run as follows XXX




## TESTING

Testing is as simple as running

```
python -m pytest
```

from the root directory of this project.


