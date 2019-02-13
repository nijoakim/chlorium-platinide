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

import curses

#================
# Periodic table
#================

# Curses screen
stdscr = None

# Dictionaries for searching
symbols = {}
names   = {}

# Periods and groups
periods = []
for i in range(7):
	periods.append([None]*18)

# Lanthanides and actinides
for i in range(2):
	periods.append([None]*14)

def print_table():
	for row, period in enumerate(periods[:-2]):
		for col, element in enumerate(period):
			if element is not None:
				stdscr.addstr(row, col*4, str(element))

	# Lanthanides
	stdscr.addstr(7+1, 2*4, '  *')
	for col, element in enumerate(periods[-1]):
		stdscr.addstr(7+1, (col+3)*4, str(element))

	# Actinides
	stdscr.addstr(7+2, 2*4, ' **')
	for col, element in enumerate(periods[-2]):
		stdscr.addstr(7+2, (col+3)*4, str(element))

class element:
	def __init__(
			self,
			symbol,
			name,
			period,
			group,
		):

		# Adjust for 0-indexing
		period = period-1 if period > 0 else period
		group  = group-1  if group > 0  else group

		symbols[symbol.lower()] = self
		names[name.lower()]     = self
		periods[period][group]  = self

		self.symbol = symbol
		self.name   = name

	def __str__(self):
		return self.symbol
