# -*- coding: utf-8 -*-
"""
***************************************************************************
*   This file is part of Work Feature workbench                           *
*                                                                         *
*   Copyright (c) 2017-2019 <rentlau_64>                                  *
*   https://github.com/Rentlau/WorkFeature-WB                             *
*                                                                         *
*   Code rewrite by <rentlau_64> from Work Features macro:                *
*   https://github.com/Rentlau/WorkFeature                                *
*                                                                         *
*   This workbench is a supplement to the FreeCAD CAx development system. *
*   http://www.freecadweb.org                                             *
*                                                                         *
*   This workbench is free software; you can redistribute it and/or modify*
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation, either version 3 of the License, or     *
*   (at your option) any later version.                                   *
*   for detail see the LICENSE text file or:                              *
*   https://www.gnu.org/licenses/gpl-3.0.html                             *
*                                                                         *
*   This workbench is distributed in the hope that it will be useful,     *
*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the          *
*   GNU Library General Public License for more details.                  *
*                                                                         *
*   You should have received a copy of the GNU Library General Public     *
*   License along with this workbench;                                    *
*   If not, see <https://www.gnu.org/licenses/>                           *
***************************************************************************
"""

import sys
import os.path
import FreeCAD
from PySide import QtCore, QtGui

__title__ = "WorkFeature  workbench"
__author__ = "Rentlau_64"
__url__ = "https://github.com/Rentlau/WorkFeature-WB.git"
__brief__ = '''

'''

###############
m_debug = False
###############

# Get the path of the current python script
path_WF = os.path.dirname(__file__)

path_WF_icons = os.path.join(path_WF, 'Resources', 'Icons')
path_WF_utils = os.path.join(path_WF, 'Utils')
path_WF_resources = os.path.join(path_WF, 'Resources')
path_WF_ui = os.path.join(path_WF, 'Resources', 'Ui')

if not sys.path.__contains__(str(path_WF_utils)):
    sys.path.append(str(path_WF_utils))
    sys.path.append(str(path_WF_ui))


def typecheck(args_and_types, name="?"):
    """ Checks arguments types.

    typecheck([arg1,type),(arg2,type),...])
    """
    for v, t in args_and_types:
        if not isinstance(v, t):
            w = "typecheck[" + str(name) + "]: "
            w += str(v) + " is not " + str(t) + "\n"
            FreeCAD.Console.PrintWarning(w)
            raise TypeError("WF." + str(name))


def getParamType(param):
    if param in ["verbose", ]:
        return "bool"
    elif param in ["release", ]:
        return "string"
    elif param in ["parametric", ]:
        return "int"
    elif param in ["pointSize", "tolerance", ]:
        # return "float"
        return "string"
    else:
        return None


def getParam(param, default=None):
    """ Returns a WorkFeature parameter value from the current config.
    """
    p = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/WF")
    t = getParamType(param)
    # print("getting param ",param, " of type ",t, " default: ",str(default))
    if t == "int":
        if default is None:
            default = 0
        return p.GetInt(param, default)
    elif t == "string":
        if default is None:
            default = ""
        return p.GetString(param, default)
    elif t == "float":
        if default is None:
            default = 0.0
        return p.GetFloat(param, default)
    elif t == "bool":
        if default is None:
            default = False
        return p.GetBool(param, default)
    elif t == "unsigned":
        if default is None:
            default = 0
        return p.GetUnsigned(param, default)
    else:
        return None


def setParam(param, value):
    """ Sets a WorkFeature parameter value with the given value.
    """
    p = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/WF")
    t = getParamType(param)
    if t == "int":
        p.SetInt(param, value)
    elif t == "string":
        p.SetString(param, value)
    elif t == "float":
        p.SetFloat(param, value)
    elif t == "bool":
        p.SetBool(param, value)
    elif t == "unsigned":
        p.SetUnsigned(param, value)


def verbose():
    """ Returns the verbose value from WF user settings
    """
    return getParam("verbose", False)


def release():
    """ Returns the release value from WF user settings
    """
    return getParam("release", None)


def set_release(value):
    """ Sets the release value to WF user settings
    """
    setParam("release", value)


def parametric():
    """ Returns the parametric index from WF user settings

    m_parametric = ['Not','Interactive','Dynamic']
    """
    return getParam("parametric", None)


def set_parametric(value):
    """ Sets the parametric index to WF user settings
    """
    setParam("parametric", value)
    
def pointSize():
    """ Returns the point size from WF user settings
    """
    return float(getParam("pointSize", "5.0"))


def set_pointSize(value):
    """ Sets the point size to WF user settings
    """
    setParam("pointSize", value)
    
def tolerance():
    """ Returns the tolerance from WF user settings
    """
    return float(getParam("tolerance", "1e-12"))


def set_tolerance(value):
    """ Sets the tolerance to WF user settings
    """
    setParam("tolerance", value)
