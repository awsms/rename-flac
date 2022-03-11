#!/usr/bin/python3

"""
rename-flac takes the information from FLAC metadata to batch rename
the files according to a file-naming scheme.

These are the options you can use to define the filenaming scheme:
  %a = Artist  |  %b = Album        |  %c = Composer  |  %d = Date
  %g = Genre   |  %n = Tracknumber  |  %t = Title
"""
import sys
import subprocess
import re
import os
import argparse


__version__ = "2.2.0"

TAGS = dict(a='artist', b='album', c='composer', d='date',
            g='genre', n='tracknumber', t='title')


def parse_args(sys_args):  # pylint: disable=W0613
    """CLI arguments comprehension"""
    example_text = '''example:
        $ rename-flac "%n - %t" "/media/Main/Musique/The Beatles"'''
    parser = argparse.ArgumentParser(prog='rename-flac',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description=__doc__,
                                 epilog=example_text)
    parser.add_argument('scheme', type=str,
                    help='filenaming scheme')
    parser.add_argument('directory', type=str,
                    help='path to the directory containing the album')
    parser.add_argument('--version', action='version', version='%(prog)s ' + __version__)
    parser.add_argument('--verbose', action='store_true',
                    help='run the program in verbose mode')
    return parser.parse_args()


def scheme_processing(args):
    """Process the scheming arguments."""
    if not re.search("%[tn]", args.scheme):  # To have a unique filename
        raise ValueError("%t or %n has to be present in <scheme>")
    scheme = re.sub('%%([%s])' % ''.join(TAGS.keys()),
                    lambda m: '%%(%s)s' % TAGS[m.group(1)],
                    args.scheme)
    return scheme


def fetch_metadata(filepath):
    """Fetch metadata and format it."""
    mf_args = ["--show-tag=%s" % tag for tag in TAGS.values()]
    tags = ["%s=" % tag for tag in TAGS.values()]
    # make sure the keys exist. Prevents failure in case of incomplete metadata
    metadata = dict.fromkeys(list(TAGS.values()), '')
    pipe = subprocess.Popen(["metaflac"] + mf_args + [filepath],
                            stdout=subprocess.PIPE)
    output, error = pipe.communicate()
    if pipe.returncode:
        raise IOError("metaflac failed: %s" % error)
    output = output.decode('utf-8') # binary to string
    output = output.splitlines()
    for tag in tags:
        for item in output:
            x = re.compile(re.escape(tag), re.IGNORECASE)
            if bool(re.match(x, item)):
                tag = tag.replace("=", "")
                if tag == "tracknumber":
                    metadata[tag] = x.sub("", item).zfill(2)
                else:
                    metadata[tag] = x.sub("", item)
    return metadata


def rename(scheme, dirname, filename, args):
    """Renames the files."""
    filepath = os.path.join(dirname, filename)
    new_filename = scheme % fetch_metadata(filepath) + ".flac"
    if new_filename == filename:
        if args.verbose:
            print('"%s" is already named correctly' % filename)
    else:
        new_filepath = os.path.join(dirname, new_filename)
        os.rename(filepath, new_filepath)
        if args.verbose:
            print('"%s" --> "%s"' % (filename, new_filename))


def main():
    """Main function."""
    args = parse_args(sys.argv[1:])
    scheme = scheme_processing(args)
    if not os.path.isdir(args.directory):
        raise NotADirectoryError("%s is not a valid directory"
                                 % args.directory)
    counter = 0
    for dirname, _, filenames in os.walk(args.directory, topdown=False):
        for filename in sorted(filenames):
            if filename.endswith('.flac'):
                counter += 1
                try:
                    rename(scheme, dirname, filename, args)
                except KeyboardInterrupt:
                    raise
                except OSError:
                    sys.exit("Error: %s title contains /. Please rename it"
                             % filename)
    if counter < 1:
        raise FileNotFoundError("No FLAC files found in %s"
                                 % args.directory)


if __name__ == "__main__":
    main()
