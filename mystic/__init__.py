#!/usr/bin/env python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Author: Alta Fang (altafang @caltech and alta @princeton)
# Author: Patrick Hung (patrickh @caltech)
# Copyright (c) 1997-2016 California Institute of Technology.
# Copyright (c) 2016-2017 The Uncertainty Quantification Foundation.
# License: 3-clause BSD.  The full license text is available at:
#  - http://trac.mystic.cacr.caltech.edu/project/mystic/browser/mystic/LICENSE

# get version numbers, license, and long description
try:
    from .info import this_version as __version__
    from .info import readme as __doc__, license as __license__
except ImportError:
    msg = """First run 'python setup.py build' to build mystic."""
    raise ImportError(msg)

__author__ = 'Mike McKerns'

__doc__ = """
""" + __doc__

__license__ = """
""" + __license__

__all__ = ['solvers', 'termination', 'strategy', 'munge', 'tools', \
           'constraints', 'penalty', 'coupler', 'symbolic', 'monitors', \
           'support', 'model_plotter', 'log_reader', 'collapse_plotter']

# solvers
from . import solvers

# strategies, termination conditions
from . import termination
from . import strategy

# constraints and penalties
from . import constraints
from . import penalty
from . import coupler
from . import symbolic

# monitors, function wrappers, and other tools
from . import monitors
from . import munge
from . import tools

# scripts
from .scripts import model_plotter, log_reader, collapse_plotter
from . import support

# backward compatibility
from .tools import *


def license():
    """print license"""
    print(__license__)
    return

def citation():
    """print citation"""
    print(__doc__[-526:-123])
    return

# end of file
