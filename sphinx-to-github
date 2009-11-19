#! /usr/bin/env python
 
from optparse import OptionParser
import os
import sys


class NoDirectoriesError(Exception):
    "Error thrown when no directories starting with an underscore are found"

class Replacer(object):
    "Encapsulates a simple text replace"

    def __init__(self, from_, to):

        self.from_ = from_
        self.to = to

    def process(self, text):

        return text.replace( self.from_, self.to )

class FileHandler(object):
    "Applies a series of replacements the contents of a file inplace"

    def __init__(self, name, replacers):

        self.name = name
        self.replacers = replacers

    def process(self):

        text = open(self.name).read()

        for replacer in self.replacers:
            text = replacer.process( text )

        open(self.name, "w").write(text)

class DirectoryHandler(object):
    "Encapsulates renaming a directory by removing its first character"

    def __init__(self, name, root):

        self.name = name
        self.new_name = name[1:]
        self.root = root + os.sep

    def path(self):
        
        return os.path.join(self.root, self.name)

    def relative_path(self, directory, filename):

        path = directory.replace(self.root, "", 1)
        return os.path.join(path, filename)

    def new_relative_path(self, directory, filename):

        path = self.relative_path(directory, filename)
        return path.replace(self.name, self.new_name, 1)

    def process(self):

        from_ = os.path.join(self.root, self.name)
        to = os.path.join(self.root, self.new_name)
        os.rename(from_, to)

class VerboseDirectoryHandler(DirectoryHandler):

    def __init__(self, name, root, stream):

        DirectoryHandler.__init__(self, name, root)

        self.stream = stream

    def process(self):

        self.stream.write(
                "Renaming directory '%s' -> '%s'\n" % (self.name, self.new_name)
                )

        DirectoryHandler.process(self)

class Layout(object):
    """
    Applies a set of operations which result in the layout
    of a directory changing
    """

    def __init__(self, directory_handlers, file_handlers):

        self.directory_handlers = directory_handlers
        self.file_handlers = file_handlers

    def process(self):

        for handler in self.file_handlers:
            handler.process()

        for handler in self.directory_handlers:
            handler.process()


class LayoutFactory(object):
    "Creates a layout object"

    def __init__(self, verbose, stream):

        self.verbose = verbose
        self.output_stream = stream

    def create_layout(self, path):

        contents = os.listdir(path)

        # Build list of directories to process
        directories = [d for d in contents if self.is_underscore_dir(path, d)]
        if self.verbose:
            underscore_directories = [
                    VerboseDirectoryHandler(d, path, self.output_stream)
                        for d in directories
                    ]
        else:
            underscore_directories = [
                    DirectoryHandler(d, path) for d in directories
                    ]

        if not underscore_directories:
            raise NoDirectoriesError()

        # Build list of files that are in those directories
        replacers = []
        for handler in underscore_directories:
            for directory, dirs, files in os.walk(handler.path()):
                for f in files:
                    replacers.append(
                            Replacer(
                                handler.relative_path(directory, f),
                                handler.new_relative_path(directory, f)
                                )
                            )

        # Build list of handlers to process all files
        filelist = []
        for root, dirs, files in os.walk(path):
            for f in files:
                if f.endswith(".html"):
                    filelist.append(
                            FileHandler(os.path.join(root, f), replacers)
                            )

        return Layout(underscore_directories, filelist)

    @staticmethod
    def is_underscore_dir(path, directory):

        return (os.path.isdir(os.path.join(path, directory))
            and directory.startswith("_"))



def main(args):

    usage = "usage: %prog [options] <html directory>"
    parser = OptionParser(usage=usage)
    parser.add_option("-v","--verbose", action="store_true",
            dest="verbose", default=False, help="Provides verbose output")
    opts, args = parser.parse_args(args)

    try:
        path = args[0]
    except IndexError:
        sys.stderr.write(
                "Error - Expecting path to html directory:"
                "sphinx-to-github <path>\n"
                )
        return

    layout_factory = LayoutFactory(opts.verbose, sys.stdout)

    try:
        layout = layout_factory.create_layout(path)
    except NoDirectoriesError:
        sys.stderr.write(
                "Error - No top level directories starting with an underscore "
                "were found in '%s'\n" % path
                )
        return

    layout.process()
    


if __name__ == "__main__":
    main(sys.argv[1:])



