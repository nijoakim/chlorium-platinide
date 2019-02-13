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

# Cursor coordinates
sel_period = 0
sel_group  = 0

# Periods and groups
periods = []
for i in range(7):
	periods.append([None]*18)

# Lanthanides and actinides
for i in range(2):
	periods.append([None]*14)

# color dictionary
colors = {
	'Reactive nonmetal': 3, # Yellow
	'Noble gas':         6, # Cyan
	'Alkali metal':      1, # Red
}

def print_table():
	# Non-special-position elements
	for row, period in enumerate(periods[:-2]):
		for col, element in enumerate(period):
			if element is not None:
				# Highlight selected
				if  sel_period == col \
				and sel_group == row:
					attr = curses.A_REVERSE
				else:
					attr = 0

				# Set color
				if element.type in colors:
					attr |= curses.color_pair(colors[element.type])

				# Draw element
				stdscr.addstr(row, col*4, str(element), attr)

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

		# Make searchable
		symbols[symbol.lower()] = self
		names[name.lower()]     = self
		periods[period][group]  = self

		# Member variables
		self.symbol = symbol
		self.name   = name
		self.type   = None

	def __str__(self):
		return self.symbol

def element_type(type, *elements):
	for element in elements:
		symbols[element.lower()].type = type
