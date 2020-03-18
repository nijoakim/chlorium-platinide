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

from . import periodic_table as pt

#==================
# Add the elements
#==================

# Period 1
pt.Element('H',  'Hydrogen', 1, 1)
pt.Element('He', 'Helium',   1, 18)

# Period 2
pt.Element('Li', 'Lithium',   2, 1)
pt.Element('Be', 'Beryllium', 2, 2)
pt.Element('B',  'Boron',     2, 13)
pt.Element('C',  'Carbon',    2, 14)
pt.Element('N',  'Nitrogen',  2, 15)
pt.Element('O',  'Oxygen',    2, 16)
pt.Element('F',  'Flourine',  2, 17)
pt.Element('Ne', 'Neon',      2, 18)

# Period 3
pt.Element('Na', 'Sodium',     3, 1)
pt.Element('Mg', 'Magnesium',  3, 2)
pt.Element('Al', 'Aluminium',  3, 13)
pt.Element('Si', 'Silicon',    3, 14)
pt.Element('P',  'Phosphorus', 3, 15)
pt.Element('S',  'Sulfur',     3, 16)
pt.Element('Cl', 'Chlorine',   3, 17)
pt.Element('Ar', 'Argon',      3, 18)

# Period 4
pt.Element('K',  'Potassium', 4, 1)
pt.Element('Ca', 'Calcium',   4, 2)
pt.Element('Sc', 'Scandium',  4, 3)
pt.Element('Ti', 'Titanium',  4, 4)
pt.Element('V',  'Vanadium',  4, 5)
pt.Element('Cr', 'Chromium',  4, 6)
pt.Element('Mn', 'Manganese', 4, 7)
pt.Element('Fe', 'Iron',      4, 8)
pt.Element('Co', 'Cobalt',    4, 9)
pt.Element('Ni', 'Nickel',    4, 10)
pt.Element('Cu', 'Copper',    4, 11)
pt.Element('Zn', 'Zink',      4, 12)
pt.Element('Ga', 'Gallium',   4, 13)
pt.Element('Ge', 'Germanium', 4, 14)
pt.Element('As', 'Arsenic',   4, 15)
pt.Element('Se', 'Selenium',  4, 16)
pt.Element('Br', 'Bromium',   4, 17)
pt.Element('Kr', 'Krypton',   4, 18)

# Period 5
pt.Element('Rb', 'Rubidium',   5, 1)
pt.Element('Sr', 'Strontium',  5, 2)
pt.Element('Y',  'Yttrium',    5, 3)
pt.Element('Zr', 'Zirconium',  5, 4)
pt.Element('Nb', 'Niobium',    5, 5)
pt.Element('Mo', 'Molybdenum', 5, 6)
pt.Element('Tc', 'Technetium', 5, 7)
pt.Element('Ru', 'Ruthenium',  5, 8)
pt.Element('Rh', 'Rhodium',    5, 9)
pt.Element('Pd', 'Palladium',  5, 10)
pt.Element('Ag', 'Silver',     5, 11)
pt.Element('Cd', 'Cadmium',    5, 12)
pt.Element('In', 'Indium',     5, 13)
pt.Element('Sn', 'Tin',        5, 14)
pt.Element('Sb', 'Antimony',   5, 15)
pt.Element('Te', 'Tellerium',  5, 16)
pt.Element('I',  'Iodine',     5, 17)
pt.Element('Xe', 'Xenon',      5, 18)

# Period 6
pt.Element('Cs', 'Caesium',     6, 1)
pt.Element('Ba', 'Barium',      6, 2)
pt.Element('*',  'Lanthanide', 6, 3)
pt.Element('Hf', 'Hafnium',     6, 4)
pt.Element('Ta', 'Tantalum',    6, 5)
pt.Element('W',  'Tungsten',    6, 6)
pt.Element('Re', 'Rhenium',     6, 7)
pt.Element('Os', 'Osmium',      6, 8)
pt.Element('Ir', 'Iridium',     6, 9)
pt.Element('Pt', 'Platinum',    6, 10)
pt.Element('Au', 'Gold',        6, 11)
pt.Element('Hg', 'Mercury',     6, 12)
pt.Element('Tl', 'Thallium',    6, 13)
pt.Element('Pb', 'Lead',        6, 14)
pt.Element('Bi', 'Bismuth',     6, 15)
pt.Element('Po', 'Polonium',    6, 16)
pt.Element('At', 'Astatine',    6, 17)
pt.Element('Rn', 'Radon',       6, 18)

# Period 7
pt.Element('Fr', 'Fracium',       7, 1)
pt.Element('Ra', 'Radium',        7, 2)
pt.Element('**', 'Actinide',     7, 3)
pt.Element('Rf', 'Rutherfordium', 7, 4)
pt.Element('Db', 'Dubnium',       7, 5)
pt.Element('Sg', 'Seaborgium',    7, 6)
pt.Element('Bh', 'Bohrium',       7, 7)
pt.Element('Hs', 'Hassium',       7, 8)
pt.Element('Mt', 'Meitnerium',    7, 9)
pt.Element('Ds', 'Darmstadtium',  7, 10)
pt.Element('Rg', 'Roentgenium',   7, 11)
pt.Element('Cn', 'Copernicium',   7, 12)
pt.Element('Nh', 'Nihonium',      7, 13)
pt.Element('Fl', 'Flerovium',     7, 14)
pt.Element('Mc', 'Moscovium',     7, 15)
pt.Element('Lv', 'Livermorium',   7, 16)
pt.Element('Ts', 'Tennessine',    7, 17)
pt.Element('Og', 'Oganesson',     7, 18)

# Lanthanides
pt.Element('La', 'Lanthanium',   -2, 1)
pt.Element('Ce', 'Cerium',       -2, 2)
pt.Element('Pr', 'Praseodymium', -2, 3)
pt.Element('Nd', 'Neodynium',    -2, 4)
pt.Element('Pm', 'Promethium',   -2, 5)
pt.Element('Sm', 'Samarium',     -2, 6)
pt.Element('Eu', 'Europium',     -2, 7)
pt.Element('Gd', 'Gadolinium',   -2, 8)
pt.Element('Tb', 'Terbium',      -2, 9)
pt.Element('Dy', 'Dysprosium',   -2, 10)
pt.Element('Ho', 'Holmium',      -2, 11)
pt.Element('Er', 'Erbium',       -2, 12)
pt.Element('Tm', 'Thulium',      -2, 13)
pt.Element('Yb', 'Ytterbium',    -2, 14)
pt.Element('Lu', 'Lutetium',     -2, 15)

# Actinides
pt.Element('Ac', 'Actinium',     -1, 1)
pt.Element('Th', 'Thorium',      -1, 2)
pt.Element('Pa', 'Protactinium', -1, 3)
pt.Element('U',  'Uranium',      -1, 4)
pt.Element('Np', 'Neptunium',    -1, 5)
pt.Element('Pu', 'Plutonium',    -1, 6)
pt.Element('Am', 'Americium',    -1, 7)
pt.Element('Cm', 'Curium',       -1, 8)
pt.Element('Bk', 'Berkelium',    -1, 9)
pt.Element('Cf', 'Californium',  -1, 10)
pt.Element('Es', 'Einsteinium',  -1, 11)
pt.Element('Fm', 'Fermium',      -1, 12)
pt.Element('Md', 'Mendelevium',  -1, 13)
pt.Element('No', 'Nobelium',     -1, 14)
pt.Element('Lr', 'Lawrenceium',  -1, 15)

#============================
# Group the elements by type
#============================

pt.element_type('Reactive nonmetal',     'H', 'C', 'N', 'O', 'F', 'P', 'S', 'Cl', 'Se', 'Br', 'I')
pt.element_type('Noble gas',             'He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn')
pt.element_type('Alkali metal',          'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr')
pt.element_type('Alkaline earth metal',  'Be', 'Mg', 'Ca', 'Sr', 'Ba', 'Ra')
pt.element_type('Metalloid',             'B', 'Si', 'Ge', 'As', 'Sb', 'Te', 'At')
pt.element_type('Post-transition metal', 'Al', 'Zn', 'Ga', 'Cd', 'In', 'Sn', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'Po', 'Cn')
pt.element_type('Transition metal',
	'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu',
	'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag',
	'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au',
	'Rf', 'Db', 'Sg', 'Bh', 'Hs',
)
pt.element_type('Lanthanide',
	'*', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu',
)
pt.element_type('Actinide',
	'**', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr',
)
pt.element_type('Unknown', 'Mt', 'Ds', 'Rg', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og')
