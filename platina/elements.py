# Copyright 2019 Joakim Nilsson
#
# Platina is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Platina is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Platina.  If not, see <http://www.gnu.org/licenses/>.

from . import periodic_table as pt

#==================
# Add the elements
#==================

# Period 1
pt.element('H',  'Hydrogen', 1, 1)
pt.element('He', 'Helium',   1, 18)

# Period 2
pt.element('Li', 'Lithium',   2, 1)
pt.element('Be', 'Beryllium', 2, 2)
pt.element('B',  'Boron',     2, 13)
pt.element('C',  'Carbon',    2, 14)
pt.element('N',  'Nitrogen',  2, 15)
pt.element('O',  'Oxygen',    2, 16)
pt.element('F',  'Flourine',  2, 17)
pt.element('Ne', 'Neon',      2, 18)

# Period 3
pt.element('Na', 'Sodium',     3, 1)
pt.element('Mg', 'Magnesium',  3, 2)
pt.element('Al', 'Aluminium',  3, 13)
pt.element('Si', 'Silicon',    3, 14)
pt.element('P',  'Phosphorus', 3, 15)
pt.element('S',  'Sulfur',     3, 16)
pt.element('Cl', 'Chlorine',   3, 17)
pt.element('Ar', 'Argon',      3, 18)

# Period 4
pt.element('K',  'Potassium', 4, 1)
pt.element('Ca', 'Calcium',   4, 2)
pt.element('Sc', 'Scandium',  4, 3)
pt.element('Ti', 'Titanium',  4, 4)
pt.element('V',  'Vanadium',  4, 5)
pt.element('Cr', 'Chromium',  4, 6)
pt.element('Mn', 'Manganese', 4, 7)
pt.element('Fe', 'Iron',      4, 8)
pt.element('Co', 'Cobalt',    4, 9)
pt.element('Ni', 'Nickel',    4, 10)
pt.element('Cu', 'Copper',    4, 11)
pt.element('Zn', 'Zink',      4, 12)
pt.element('Ga', 'Gallium',   4, 13)
pt.element('Ge', 'Germanium', 4, 14)
pt.element('As', 'Arsenic',   4, 15)
pt.element('Se', 'Selenium',  4, 16)
pt.element('Br', 'Bromium',   4, 17)
pt.element('Kr', 'Krypton',   4, 18)

# Period 5
pt.element('Rb', 'Rubidium',   5, 1)
pt.element('Sr', 'Strontium',  5, 2)
pt.element('Y',  'Yttrium',    5, 3)
pt.element('Zr', 'Zirconium',  5, 4)
pt.element('Nb', 'Niobium',    5, 5)
pt.element('Mo', 'Molybdenum', 5, 6)
pt.element('Tc', 'Technetium', 5, 7)
pt.element('Ru', 'Ruthenium',  5, 8)
pt.element('Rh', 'Rhodium',    5, 9)
pt.element('Pd', 'Palladium',  5, 10)
pt.element('Ag', 'Silver',     5, 11)
pt.element('Cd', 'Cadmium',    5, 12)
pt.element('In', 'Indium',     5, 13)
pt.element('Sn', 'Tin',        5, 14)
pt.element('Sb', 'Antimony',   5, 15)
pt.element('Te', 'Tellerium',  5, 16)
pt.element('I',  'Iodine',     5, 17)
pt.element('Xe', 'Xenon',      5, 18)

# Period 6
pt.element('Cs', 'Caesium',     6, 1)
pt.element('Ba', 'Barium',      6, 2)
pt.element('*',  'Lanthanides', 6, 3)
pt.element('Hf', 'Hafnium',     6, 4)
pt.element('Ta', 'Tantalum',    6, 5)
pt.element('W',  'Tungsten',    6, 6)
pt.element('Re', 'Rhenium',     6, 7)
pt.element('Os', 'Osmium',      6, 8)
pt.element('Ir', 'Iridium',     6, 9)
pt.element('Pt', 'Platinum',    6, 10)
pt.element('Au', 'Gold',        6, 11)
pt.element('Hg', 'Mercury',     6, 12)
pt.element('Tl', 'Thallium',    6, 13)
pt.element('Pb', 'Lead',        6, 14)
pt.element('Bi', 'Bismuth',     6, 15)
pt.element('Po', 'Polonium',    6, 16)
pt.element('At', 'Astatine',    6, 17)
pt.element('Rn', 'Radon',       6, 18)

# Period 7
pt.element('Fr', 'Fracium',       7, 1)
pt.element('Ra', 'Radium',        7, 2)
pt.element('**', 'Actinides',     7, 3)
pt.element('Rf', 'Rutherfordium', 7, 4)
pt.element('Db', 'Dubnium',       7, 5)
pt.element('Sg', 'Seaborgium',    7, 6)
pt.element('Bh', 'Bohrium',       7, 7)
pt.element('Hs', 'Hassium',       7, 8)
pt.element('Mt', 'Meitnerium',    7, 9)
pt.element('Ds', 'Darmstadtium',  7, 10)
pt.element('Rg', 'Roentgenium',   7, 11)
pt.element('Cn', 'Copernicium',   7, 12)
pt.element('Nh', 'Nihonium',      7, 13)
pt.element('Fl', 'Flerovium',     7, 14)
pt.element('Mc', 'Moscovium',     7, 15)
pt.element('Lv', 'Livermorium',   7, 16)
pt.element('Ts', 'Tennessine',    7, 17)
pt.element('Og', 'Oganesson',     7, 18)

# Lanthanides
pt.element('La', 'Lanthanium',   -2, 1)
pt.element('Ce', 'Cerium',       -2, 2)
pt.element('Pr', 'Praseodymium', -2, 3)
pt.element('Nd', 'Neodynium',    -2, 4)
pt.element('Pm', 'Promethium',   -2, 5)
pt.element('Sm', 'Samarium',     -2, 6)
pt.element('Eu', 'Europium',     -2, 7)
pt.element('Gd', 'Gadolinium',   -2, 8)
pt.element('Tb', 'Terbium',      -2, 9)
pt.element('Dy', 'Dysprosium',   -2, 10)
pt.element('Ho', 'Holmium',      -2, 11)
pt.element('Er', 'Erbium',       -2, 12)
pt.element('Tm', 'Thulium',      -2, 13)
pt.element('Yb', 'Ytterbium',    -2, 14)
pt.element('Lu', 'Lutetium',     -2, 15)

# Actinides
pt.element('Ac', 'Actinium',     -1, 1)
pt.element('Th', 'Thorium',      -1, 2)
pt.element('Pa', 'Protactinium', -1, 3)
pt.element('U',  'Uranium',      -1, 4)
pt.element('Np', 'Neptunium',    -1, 5)
pt.element('Pu', 'Plutonium',    -1, 6)
pt.element('Am', 'Americium',    -1, 7)
pt.element('Cm', 'Curium',       -1, 8)
pt.element('Bk', 'Berkelium',    -1, 9)
pt.element('Cf', 'Californium',  -1, 10)
pt.element('Es', 'Einsteinium',  -1, 11)
pt.element('Fm', 'Fermium',      -1, 12)
pt.element('Md', 'Mendelevium',  -1, 13)
pt.element('No', 'Nobelium',     -1, 14)
pt.element('Lr', 'Lawrenceium',  -1, 15)

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
pt.element_type('Lanthanides',
	'*', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu',
)
pt.element_type('Actinides',
	'**', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr',
)
pt.element_type('Unknown', 'Mt', 'Ds', 'Rg', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og')
