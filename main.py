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

# Do not change the structure of this. Many Python distributions have a lib called "parser".
from staply import parser

def main():
    print("Welcome to staply. Please specify a formatted inflection file.")
    print("(Note: The program expects an inflection file in the execution directory.)")
    filename = input()
    parsed = parser.parse(filename)
    if parsed[0]:
        print("File successfully parsed.")
    else:
        print("An error has occurred while parsing your file. Please check your file for mistakes.")
        return
    print("Please enter the name of your desired inflection.")
    infl_name = input()
    exists_infl_name = parser.inflection(infl_name)
    while not exists_infl_name[0]:
        print("No such inflection exists. Please try again or enter exit to quit.")
        infl_name = input()
        if infl_name == "exit":
            return
        exists_infl_name = parser.inflection(infl_name)
    print("Inflection requested has been found. Please enter the word or words you wish to inflect.")
    return

if __name__ == '__main__':
    main()