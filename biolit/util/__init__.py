from __future__ import absolute_import, division, print_function, \
                       unicode_literals
import sys
import csv
import xml.etree.ElementTree as ET

def read_unicode_csv(filename, delimiter=',', quotechar='"',
                     quoting=csv.QUOTE_MINIMAL, lineterminator='\n',
                     encoding='utf-8'):
    # Python 3 version
    if sys.version_info[0] >= 3:
        # Open the file in text mode with given encoding
        # Set newline arg to '' (see https://docs.python.org/3/library/csv.html)
        with open(filename, 'r', newline='', encoding=encoding) as f:
            # Next, get the csv reader, with unicode delimiter and quotechar
            csv_reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar,
                                 quoting=quoting, lineterminator=lineterminator)
            # Now, return the (already decoded) unicode csv_reader generator
            for row in csv_reader:
                yield row
    # Python 2 version
    else:
        # Open the file, no encoding specified
        with open(filename, 'rb') as f:
            # Next, get the csv reader, passing delimiter and quotechar as
            # bytestrings rather than unicode
            csv_reader = csv.reader(f, delimiter=delimiter.encode(encoding),
                                 quotechar=quotechar.encode(encoding),
                                 quoting=quoting, lineterminator=lineterminator)
            # Iterate over the file and decode each string into unicode
            for row in csv_reader:
                yield [cell.decode(encoding) for cell in row]


if sys.version_info[0] >= 3:
    def UnicodeXMLTreeBuilder():
        return None
else:
    class UnicodeXMLTreeBuilder(ET.XMLTreeBuilder):
        # See this thread:
        # http://www.gossamer-threads.com/lists/python/python/728903
        def _fixtext(self, text):
            return text
