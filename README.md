VimperatorrcBuilder
===================

Use the features provided by Python to produce a vimperator configuration file.
As the vimperator scripting features are very limited (no way to perform a loop
or conditional statements), I needed a way to duplicate things without writing
them more than once.

At the moment, 'bookmarks' and shortcuts to access search engines have been
provided.

The first thing to do is to create an instance of class VimperatorrcBuilder.

    from VimperatorrcBuilder import VimperatorrcBuilder

    builder = VimperatorrcBuilder()

usage
-----

to print the configuration on the standard output:

    $ chmod +x example.py
    $ ./example.py
    
redirect the output to your vimperator configuration file when you are done

    $ ./exemple.py > ~/.vimperatorrc

bookmarks
---------

bookmarks are pages that you can access by typing '\' followed by a key sequence
of your choice. The same bookmark may also be opened in a new tab by replacing
'\' by '|'. Actually, in most common keyboard layouts, you just need to hold the
shift key.

to define a bookmark, you need to call the method register_bookmark(seq, url)

for example:

    builder.register_bookmark('g', 'github.com')

then you will be able to access your bookmark by pressing \g (or |g if you want
it in a new tab)

default search engine
---------------------

You can change your default search engine (i.e. whichever will handle your
queries when you do :open query by calling set_default_search_engine(engine)

You must supply an engine name which exists on your browser.

To know which engines are currently installed on your browser,

    :dialog searchengines

and check the column 'keyword'

for example:

    builder.set_default_search_engine('duckduckgo')

bang shortcuts
--------------

duckduckgo provides a way to use plenty of other search engines by prefixing
your research by '!' followed by the name of one engine.  This is the bang
notation.  Please refer to https://duckduckgo.com/bang.html for more
information and an exhaustive list of the available search engines.

I reuse this notation in this software to simplify researches on my prefered
search engines.

A bang shortcut can be accessed by pressing 's' followed by a key sequence and
your research string. The same shortcut may also be opened in a new tab by
replacing 's' by 'S'.

to define a bang shortcut, you need to call the method
register_bang_shortcut(seq, bang_shortcut)

for example:

    builder.register_bang_shortcut('o', 'osm')

Then, to do a research on osm (OpenStreetMap), you simply need to type soLondon
(or SoLondon if you want it on a new tab) and the return key.

*nb: duckduckgo must be the default search engine if you want the bang shortcuts
to work properly*

generate the configuration
--------------------------

At last, you can generate the output by calling the method get_output() 
Redirect this output in your vimperator configuration file if you are okay with.

    print(builder.get_output())

License
=======

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
