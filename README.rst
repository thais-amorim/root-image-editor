Root Image Editor
========
|master| |codecov| |MIT license|

.. |master| image:: https://travis-ci.org/thasmarinho/root-image-editor.svg?branch=master
    :target: https://travis-ci.org/thasmarinho/root-image-editor

.. |MIT license| image:: https://img.shields.io/badge/License-MIT-blue.svg
    :target: https://lbesson.mit-license.org/

.. |codecov| image:: https://codecov.io/gh/thasmarinho/root-image-editor/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/thasmarinho/root-image-editor/


First project of the Digital Image Processing course.

Install dependencies
--------------------

$ pip3 install -r requirements.txt

Running
-------

$ python3 main.py

Testing
-------

$ pytest test

Features
--------

Implemented filters:

- Negative
- Logarithmic
- Gamma Correction
- Histogram Equalization
- Median
- Piecewise Linear
- Arithmetic Mean
- Geometric Mean
- Harmonic Mean
- Contra-harmonic Mean
- Convolution
- Laplacian
- Sobel

Color filters:

- Sepia
- Chroma-Key

Color conversion:

- RGB to gray via weighted average
- RGB to gray via simple average
- RGB <-> HSV
- RGB <-> HSI

Other:

- Draw histogram of any image

Contribute
----------

- Issue Tracker: https://github.com/thasmarinho/root-image-editor/issues
- Source Code: https://github.com/thasmarinho/root-image-editor

License
-------

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
