#!/usr/bin/python3

"""
Basic unit tests for rename-flac
"""

import unittest

from types import SimpleNamespace
from rename_flac import scheme_processing, fetch_metadata, rename


class TestScheme(unittest.TestCase):
    """Test the scheme processor"""

    def test_tracknumber_title(self):
        args = SimpleNamespace(scheme='%n - %t')
        scheme = scheme_processing(args)
        self.assertEqual(scheme, '%(tracknumber)s - %(title)s')

    def test_tracknumber_title_extra(self):
        args = SimpleNamespace(scheme='%n - %t Foobars200')
        scheme = scheme_processing(args)
        self.assertEqual(scheme, '%(tracknumber)s - %(title)s Foobars200')

    def test_all(self):
        args = SimpleNamespace(scheme='%a - %b - %c - %d - %g - %n - %t')
        scheme = scheme_processing(args)
        self.assertEqual(scheme, "%(artist)s - %(album)s - %(composer)s - "
                                 "%(date)s - %(genre)s - %(tracknumber)s - "
                                 "%(title)s")

    def test_no_tracknumber_or_title(self):
        args = SimpleNamespace(scheme='%a')
        with self.assertRaises(ValueError):
            scheme = scheme_processing(args)


class TestMetadata(unittest.TestCase):
    """Basic metadata tests"""

    def test_metadata(self):
        metadata = fetch_metadata('tests/blank.flac')
        self.assertEqual(metadata['artist'], 'Artist')
        self.assertEqual(metadata['album'], 'Album')
        self.assertEqual(metadata['composer'], 'Composer')
        self.assertEqual(metadata['date'], 'Date')
        self.assertEqual(metadata['genre'], 'Genre')
        self.assertEqual(metadata['tracknumber'], 'Tracknumber')
        self.assertEqual(metadata['title'], 'Title')


if __name__ == '__main__':
    unittest.main()
