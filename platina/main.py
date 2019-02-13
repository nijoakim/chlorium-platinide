#!/usr/bin/python3

# Copyright 2019 Joakim Nilsson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#=========
# Imports
#=========

# External
import curses
from curses import wrapper

# Internal
import elements as e
import periodic_table as pt

#======
# Main
#======

def main(stdscr):
	# Share curses screen with periodic table
	pt.stdscr = stdscr

	# Curses colors
	curses.use_default_colors()
	for i in range(1, 16):
		curses.init_pair(i, i, -1)

	# Init. curses
	curses.curs_set(False)

	# Print periodic table
	pt.print_table()

	# Refresh screen and await key press
	stdscr.refresh()
	stdscr.getkey()

# Run main
if __name__ == "__main__":
    wrapper(main) # Curses wrapper for main
