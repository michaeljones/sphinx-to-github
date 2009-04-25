
Sphinx to GitHub
================

A basic shell script for preparing the html output of the sphinx documentation
system for github pages. 

It renames any top level folders which start with an underscore and edits any
references to them within the html files.

Why?
----

GitHub processes the incoming html with Jekyll which believes top level folders
starting with an underscore are special and does let their content be accessible
to the server. This is incompatible with Sphinx which uses underscores at the
start of folder names for static content.

How?
----

The script should be run from the top level of the html output, ie. from within
the folder which contains ``index.html`` and the offending underscore folders.

Requirements
------------

To uses:

* bash
* sed

Might make sense to have a pure python script but ``sed`` makes it so easy.

Note
----

This has been written and tested for a very basic project. If you find
complications within more involved setups please let me know and/or patch up the
code a little.


