===========
rename-flac
===========

-----------------------------
CLI tool to rename FLAC files
-----------------------------

:Author: Louis-Philippe Véronneau
:Date: 2020
:Manual section: 1

Synopsis
========

| rename-flac [**--verbose**] *<scheme>* *<directory>*
| rename-flac (**-h** \| **--help**)
| rename-flac **--version**

Description
===========

**rename-flac** is a command-line tool that takes the information
from FLAC metadata to batch rename the files according to a filenaming
scheme.

Arguments
=========

| *<scheme>*     filenaming scheme
| *<directory>*  path to the directory containing the album

Options
=======

| **-h** **--help**  Shows the help screen
| **--version**  Outputs version information
| **--verbose**  Runs the program as verbose mode

| These are the options you can use to define the filenaming scheme:
|   %a - Artist  \|  %b - Album        \|  %c - Composer  \|  %d - Date
|   %g - Genre   \|  %n - Tracknumber  \|  %t - Title

Examples
========

    $ rename-flac "%n - %t" "/home/user/Music/The Beatles"

Bugs
====

Bugs can be reported to your distribution's bug tracker or upstream
at https://gitlab.com/baldurmen/rename-flac/issues.
