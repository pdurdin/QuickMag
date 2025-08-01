# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QuickMag
                                 A QGIS plugin
 Parses ASC file and generates raster
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2025-06-28
        copyright            : (C) 2025 by P Durdin
        email                : pdurdin@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load QuickMag class from file QuickMag.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .quick_mag import QuickMag
    return QuickMag(iface)
