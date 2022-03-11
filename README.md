`rename-flac` is a command-line tool that takes the information from FLAC
metadata to batch rename the files according to a filenaming scheme.

# Dependencies

This program is written in Python3. You will need these to run `rename-flac` correctly:

* python3
* metaflac

If you are using FLAC files, metaflac should already be installed by default.
On Debian distros type this to install the dependencies:

    $ sudo apt install python3 flac

If you want to install `rename-flac` via the `setup.py` file, you will also
need to install `setuptools`:

    $ sudo apt install python3-setuptools

# Installation

## In Debian

`rename-flac` is in Debian! You can install it using:

    $ sudo apt install rename-flac

## With setup.py

You can install `rename-flac` like any other python program with the help of
`setuptools`:

    $ python3 setup.py install

## Manually

Since `rename-flac` is a single python file, you can call you can it directly:

    $ python3 /path/to/rename_flac.py

If like me you want to use this program on a daily basis, it's a good idea
to modify your `.bashrc` (normally in your home folder) to include this:

    > # Alias for rename-flac
    > alias rename-flac="/path/to/rename_flac.py"

You then run these commands to be able to call the program by simply typing `rename-flac`:

    $ chmod +x /path/to/rename_flac.py
    $ source /path/to/.bashrc`

## Building the man page

The man page for `rename-flac` can be generated using the `rst2man` command line
tool provided by the Python docutils project:

    $ rst2man manpage.rst rename-flac.1

# CLI options

Here is a concrete example how I use `rename-flac`:

     $ rename-flac "%n - %t" "/media/Main/Musique/The Beatles"

The example above renames files to look like this: `01 - Yellow Submarine.flac`.
The complete CLI parameters can be found below.

    Usage:
        rename-flac [--verbose] <scheme> <directory>
        rename-flac (-h | --help)
        rename-flac --version
    
    Arguments:
        <scheme>	The filenaming scheme. Has to be between quotation marks
        <directory>	The path to the directory containing the album
    
    Options:
        -h  --help       Shows the help screen
        --version        Outputs version information
        --verbose        Runs the program as verbose mode
    
        These are the options you can use to define the filenaming scheme:
          %a = Artist  |  %b = Album        |  %c = Composer  |  %d = Date
          %g = Genre   |  %n = Tracknumber  |  %t = Title
