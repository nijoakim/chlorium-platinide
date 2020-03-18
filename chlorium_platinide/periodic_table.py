# Copyright 2019-2020 Joakim Nilsson
#
# Chlorium Platinide is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Chlorium Platinide is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Chlorium Platinide.  If not, see <http://www.gnu.org/licenses/>.

#=========
# Imports
#=========

# Type checking
from __future__ import annotations
from typing import Dict, List, Optional

import curses

#================
# Periodic table
#================

# Curses screen
stdscr = None

# Dictionaries for searching
symbols: Dict[str, Element] = {}
names:   Dict[str, Element] = {}

# Cursor coordinates
sel_period: int = 0
sel_group:  int = 0

# Periods holding groups
periods: List[List[Optional[Element]]] = []
for i in range(7):
	periods.append([None]*18)

# Lanthanides and actinides
for i in range(2):
	periods.append([None]*15)

# Color dictionary
colors: Dict[str, int] = {
	'Reactive nonmetal':     3,  # Yellow
	'Noble gas':             6,  # Cyan
	'Alkali metal':          1,  # Red
	'Alkaline earth metal':  11, # Pale yellow
	'Transition metal':      9,  # Pale red
	'Metalloid':             2,  # Green
	'Post-transition metal': 15, # White
	'Lanthanide':            13, # Pale magenta
	'Actinide':              5,  # Magenta
	'Unknown':               8,  # Gray
}

def print_table():
	# Write asterisks for the lanthanides and actinides
	stdscr.addstr(len(periods)-1,   1*4, '  *', curses.color_pair(colors['Lanthanide']))
	stdscr.addstr(len(periods)-1+1, 1*4, ' **', curses.color_pair(colors['Actinide']))

	for row, period in enumerate(periods):
		# Add a spacing row between the lanthanides/actinides and the main table
		row_offset: int = (0 if row < len(periods)-2 else 1)

		for col, element in enumerate(period):
			# Indent the lanthanides and actinides
			col_offset: int = (0 if row < len(periods)-2 else 2)

			# Write element
			if element is not None:
				# Highlight selected
				if  sel_period == row \
				and sel_group  == col:
					attr = curses.A_REVERSE
				else:
					attr = 0

				# Set color
				if element.type in colors:
					attr |= curses.color_pair(colors[element.type])

				# Write
				stdscr.addstr(row+row_offset, (col+col_offset)*4, str(element), attr)

class Element:
	def __init__(
			self,
			symbol: str,
			name: str,
			period: int,
			group: int,
		):

		# Adjust for 0-indexing
		period = period-1 if period > 0 else period
		group  = group-1  if group > 0  else group

		# Make searchable
		symbols[symbol.lower()] = self
		names[name.lower()]     = self
		periods[period][group]  = self

		# Member variables
		self.symbol: str           = symbol
		self.name:   str           = name
		self.type:   Optional[str] = None

	def __str__(self):
		return self.symbol

def element_type(type_: str, *elements: str):
	"""Makes an element searchable by type."""

	for element in elements:
		symbols[element.lower()].type = type_
