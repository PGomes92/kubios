# -*- coding: utf-8 -*-
"""
Kubios Import & Export
----------------------

This package provides functions to export NN/RR interval series in KUBIOS readable formats and import KUBIOS HRV results
from KUBIOS report files in .TXT format.

Notes
-----
..  This module is part of the master thesis
	"Development of an Open-Source Python Toolbox for Heart Rate Variability (HRV)".

Author
------
..  Pedro Gomes, Master Student, University of Applied Sciences Hamburg

Thesis Supervisors
------------------
..  Hugo Silva, PhD, Instituto de Telecomunicacoes, PLUX wireless biosignals S.A.
..  Prof. Dr. Petra Margaritoff, University of Applied Sciences Hamburg

Last Update
-----------
13-09-2018

:copyright: (c) 2018 by Pedro Gomes
:license: BSD 3-clause, see LICENSE for more details.
"""
# allow lazy import
from kubios import *

# Package info
__author__ = "Pedro Gomes"
__email__ = "pgomes92@gmail.com"
__maintainer__ = "Pedro Gomes"
__status__ = "Development"
__license__ = "BSD 3-Clause License"
__version__ = "0.1"
name = "kubios"
description = "Python package to support KUBIOS file management."
long_description = "Python package to export RRI data in KUBIOS readable format and to read/import KUBIOS results " \
				   "from KUBIOS reports."
