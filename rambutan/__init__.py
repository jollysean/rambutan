# rambutan
# Contact: Jacob Schreiber
#          jmschr@cs.washington.edu

"""
Rambutan is a set of tools to impute Hi-C datasets.
"""

import numpy
import os
import pyximport

# Adapted from Cython docs https://github.com/cython/cython/wiki/
# InstallingOnWindows#mingw--numpy--pyximport-at-runtime
if os.name == 'nt':
	if 'CPATH' in os.environ:
		os.environ['CPATH'] = os.environ['CPATH'] + numpy.get_include()
	else:
		os.environ['CPATH'] = numpy.get_include()

	# XXX: we're assuming that MinGW is installed in C:\MinGW (default)
	if 'PATH' in os.environ:
		os.environ['PATH'] = os.environ['PATH'] + ';C:\MinGW\bin'
	else:
		os.environ['PATH'] = 'C:\MinGW\bin'

	mingw_setup_args = { 'options': { 'build_ext': { 'compiler': 'mingw32' } }, 'include_dirs': numpy.get_include() }
	pyximport.install(setup_args=mingw_setup_args)

elif os.name == 'posix':
	if 'CFLAGS' in os.environ:
		os.environ['CFLAGS'] = os.environ['CFLAGS'] + ' -I' + numpy.get_include()
	else:
		os.environ['CFLAGS'] = ' -I' + numpy.get_include()

	pyximport.install()

from .rambutan import Rambutan

__version_ = '0.4.1'