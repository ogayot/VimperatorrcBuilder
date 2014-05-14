# Copyright (C) 2014 Olivier Gayot
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import time

class VimperatorrcBuilder():
	bookmarks = {}
	bookmark_pfx = '\\', '|'
	bang_shortcuts_pfx = 's', 'S'
	bang_shortcuts = {}
	default_engine = 'duckduckgo'

	def __init__(self):
		pass

	def register_bookmark(self, seq, url):
		""" Add a new bookmark and bind it to a given key-sequence """

		self.bookmarks[seq] = url

	def register_bang_shortcut(self, seq, bang_shortcut):
		""" Add a new bang shortcut and bind it to a key-sequence """

		self.bang_shortcuts[seq] = bang_shortcut

	def set_default_search_engine(self, engine):
		""" Set the default search engine (i.e. when you type 'open foo') """

		self.default_engine = engine

	def get_output(self):
		''' Return a string containing the full output to redirect '''

		output = '" Generated using VimperatorrcBuilder\n'
		output += '" ' + time.ctime() + '\n'

		output += '\n" bookmarks\n'
		for key in self.bookmarks:
			output += 'map \'' + self.bookmark_pfx[0] + key + '\' :o<Space>' + self.bookmarks[key] + '<Return>\n'
			output += 'map \'' + self.bookmark_pfx[1] + key + '\' :t<Space>' + self.bookmarks[key] + '<Return>\n'

		output += '\n" default search engine\n'
		output += 'set defsearch=' + self.default_engine + '\n'

		output += '\n" bang shortcuts\n'
		for key in self.bang_shortcuts:
			output += "noremap '" + self.bang_shortcuts_pfx[0] + key + "' o!" + self.bang_shortcuts[key] + ' \n'
			output += "noremap '" + self.bang_shortcuts_pfx[1] + key + "' t!" + self.bang_shortcuts[key] + ' \n'
		return output

