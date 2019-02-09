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

# Dictionaries for searching
symbols = {}
names   = {}

# 1-indexed periods and groups
periods = [None]
for i in range(7):
	periods.append([None]*19)

def print_table():
	for period in periods:
		if period is not None:
			for element in period[1:]:
				if element is not None:
					print(element, ' '*(3-len(str(element))), end='')
				else:
					print('    ', end='')
			print()

class element:
	def __init__(
			self,
			symbol,
			name,
			period,
			group,
		):

		symbols[symbol.lower()] = self
		names[name.lower()]     = self
		periods[period][group]  = self

		self.symbol = symbol
		self.name   = name

	def __str__(self):
		return self.symbol
