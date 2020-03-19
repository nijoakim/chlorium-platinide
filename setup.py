#!/usr/bin/env python3

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

from distutils.core import setup

setup(
	name         = 'chlorium_platinide',
	version      = '0.1.0',
	author       = 'Joakim Nilsson',
	author_email = 'nijoakim@gmail.com',
	packages     = ['chlorium_platinide'],
	scripts      = ['scripts/chlorium-platinide', 'scripts/clpt'],
	license      = 'GPLv3',
	description  = 'Interactive periodic table for the command-line.'
)
