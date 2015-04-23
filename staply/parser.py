# ------------------------------------------------------------------------------------------------
# Software:      Stem Applier (staply)
# Description:   Applies inflections to stem morphemes
# Version:       0.0.1a
# Module:        Main
#
# Author:        Frederic Bayer
# Email:         frederic.s.bayer@gmail.com
# Institution:   Bexhill College
#                Computing & ICT Department
#
# Copyright:     (c) Frederic S. Bayer 2014
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-13SA.
#------------------------------------------------------------------------------------------------

__author__ = 'Frederic Bayer'

def parse(filename):
    print(filename)
    inflections = "This will be an object holding the parsed inflectional data."
    return [True, inflections]


def inflection(infl_name):
    print(infl_name)
    return [None]