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

from . import periodic_table as pt

#===========
# Functions
#===========

# TODO: Numeric arguments

def move_down():
	try:
		# Remember original position
		sel_period = pt.sel_period
		sel_group = pt.sel_group

		# Move down
		pt.sel_group  += (0 if pt.sel_period != len(pt.periods)-3 else -2) # Adjust for lathanides and actinides
		pt.sel_period += 1

		# Negative indexes are errors
		if pt.sel_group < 0:
			raise IndexError()

		# Move more if no element is found
		if pt.periods[pt.sel_period][pt.sel_group] is None:
			move_down()

	except IndexError:
		# Revert to original position
		pt.sel_period = sel_period
		pt.sel_group  = sel_group

def move_right():
	try:
		# Remember original position
		sel_group = pt.sel_group

		# Move right
		pt.sel_group += 1

		# Move more if no element is found
		if pt.periods[pt.sel_period][pt.sel_group] is None:
			move_right()
	except IndexError:
		# Revert to original position
		pt.sel_group = sel_group
