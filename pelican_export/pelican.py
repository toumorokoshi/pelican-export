import os
from pelican.readers import Readers, MarkdownReader, RstReader
from pelican.generators import ArticlesGenerator


def get_posts(pelican_root_directory: str,):
    """Given a directory containing pelican draft files, return a generator of all pelican post files."""
    # certain keys are required by the reader, even if empty.
    reader_settings = {"READERS": None, "CACHE_PATH": "/tmp"}
    pelican_readers = Readers(reader_settings)
    for (dirpath, _, filename_list) in os.walk(target_directory):
        for filename in filename_list:
            content = pelican_readers.read_file(dirpath, filename)
            yield content
