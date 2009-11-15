Sphinx to GitHub
================

A Python script for preparing the html output of the sphinx documentation
system for github pages. 

It renames any top level folders which start with an underscore and edits any
references to them within the html files.

Why?
----

GitHub processes the incoming html with Jekyll which believes top level folders
starting with an underscore are special and does not let their content be accessible
to the server. This is incompatible with Sphinx which uses underscores at the
start of folder names for static content.

How?
----

Run the script with the path to the ``html`` output directory as the first
argument.

Requirements
------------

The script uses ``/usr/bin/env`` and ``python``. 

Note
----

The first incarnation of this script was written in bash using ``find`` and
``sed``. It was delightfully old school but not very portable and not very fast.
It is available as ``sphinx-to-github.legacy`` because the author isn't ready to
let go yet.

Credits
-------

Thank you to:

* `mikejs <http://github.com/mikejs>`_
* `certik <http://github.com/certik>`_

For their contributions, to Georg Brandl for `Sphinx <http://sphinx.pocoo.org/>`_
and the github crew for the pages functionality.


