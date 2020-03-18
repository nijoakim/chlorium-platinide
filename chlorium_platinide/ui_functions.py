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

from . import periodic_table as pt

#===========
# Functions
#===========

# TODO: Numeric arguments

def move_up():
	move(0, -1)

def move_down():
	move(0, 1)

def move_left():
	move(-1, 0)

def move_right():
	move(1, 0)

def move(x: int, y: int):
	# Base case
	if  x == 0 \
	and y == 0:
		return

	try:
		# Remember original position and planned movement
		sel_period: int = pt.sel_period
		sel_group:  int = pt.sel_group
		xx: int = x
		yy: int = y

		# Move up
		if y < 0:
			y += 1
			pt.sel_group  += (0 if pt.sel_period != len(pt.periods)-2 else 2) # Adjust for lanthanides and actinides
			pt.sel_period -= 1

		# Move down
		elif y > 0:
			y -= 1
			pt.sel_group  -= (0 if pt.sel_period != len(pt.periods)-3 else 2) # Adjust for lanthanides and actinides
			pt.sel_period += 1

		# Move left
		elif x < 0:
			x += 1
			pt.sel_group -= 1

		# Move right
		elif x > 0:
			x -= 1
			pt.sel_group += 1

		# Negative indexes are errors
		if pt.sel_group  < 0 \
		or pt.sel_period < 0:
			raise IndexError()

		# Move more if None element is found
		if pt.periods[pt.sel_period][pt.sel_group] is None:
			x = xx
			y = yy

	except IndexError:
		# Revert to original position
		pt.sel_period = sel_period
		pt.sel_group  = sel_group

	# Move more
	move(x, y)
