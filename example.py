#!/usr/bin/env python

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

import VimperatorrcBuilder

def main():
    # create an instance of the class we defined in VimperatorrcBuilder.py
    builder = VimperatorrcBuilder.VimperatorrcBuilder()

    # add the bookmarks you wish
    builder.register_bookmark('a', 'www.archlinux.org')
    builder.register_bookmark('b', 'baylibre.com')
    builder.register_bookmark('c', 'calendar.google.com')
    builder.register_bookmark('d', 'deezer.com')
    builder.register_bookmark('f', 'facebook.com')
    builder.register_bookmark('g', 'github.com')
    builder.register_bookmark('k', 'kernel.org')
    builder.register_bookmark('i', 'www.imdb.com')
    builder.register_bookmark('l', 'linkedin.com')
    builder.register_bookmark('m', 'mail.google.com')
    builder.register_bookmark('o', 'openstreetmap.org')
    builder.register_bookmark('p', 'play.typeracer.com')
    builder.register_bookmark('q', 'qwertee.com')
    builder.register_bookmark('r', 'www.regexlib.com')
    builder.register_bookmark('s', 'sigexec.com')
    builder.register_bookmark('t', 'translate.google.com')
    builder.register_bookmark('v', 'vim.org')
    builder.register_bookmark('w', 'wikipedia.org')
    builder.register_bookmark('y', 'youtube.com')
    builder.register_bookmark('z', 'www.zenk-security.com')

    # create some aliases to search engines
    builder.register_bang_shortcut('a', 'arch')
    builder.register_bang_shortcut('d', 'deezer')
    builder.register_bang_shortcut('g', 'g')
    builder.register_bang_shortcut('i', 'imdb')
    builder.register_bang_shortcut('o', 'osm')
    builder.register_bang_shortcut('r', 'regex')
    builder.register_bang_shortcut('s', 'symbolhound')
    builder.register_bang_shortcut('t', 'tpb')
    builder.register_bang_shortcut('w', 'wiki')
    builder.register_bang_shortcut('y', 'youtube')

    # this is the default behaviour, but it does not hurt to explicit it
    builder.set_default_search_engine('duckduckgo')

    # display the generated configuration on the standard output
    print(builder.get_output())

if __name__ == '__main__':
    main()
