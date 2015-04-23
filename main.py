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

# Do not change the structure of this. Many Python distributions have libs with these names.
from staply import read, parse

def main():
    # Input filename.
    print("Welcome to staply. Please specify a formatted inflection file.")
    filename = input("File: ")

    # Verify and read file.
    verified = read.verify(filename)
    if verified[0]:
        print("File successfully read.")
    elif verified[1] == 0:
        print("Specified file not found. Please try again.")
        return
    elif verified[1] == 1:
        print("File not valid. Please try again.")
        return
    else:
        print("An unknown error occurred. Please try again.")
        return

    # Define file object.
    ifile = verified[1]

    # Select inflection.
    print("Please enter the name of your desired inflection.")
    infl_name = input("Inflection: ")
    exists_infl_name = parse.inflection(ifile, infl_name)
    while not exists_infl_name:
        print("No such inflection exists. Please try again or enter exit to quit.")
        infl_name = input()
        if infl_name == "exit":
            return
        exists_infl_name = parse.inflection(infl_name)
    print("Inflection requested has been found. Please enter the word or words you wish to inflect.")
    return

if __name__ == '__main__':
    main()