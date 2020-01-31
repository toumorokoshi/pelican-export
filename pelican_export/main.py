import argparse
from .pelican import get_posts
import pelican

PARSER = argparse.ArgumentParser()
PARSER.add_argument("pelican_root_directory")
# PARSER.add_argument("wp_site_url")
# PARSER.add_argument("--wp-username")
# PARSER.add_argument("--wp-password")


def main():
    arguments = PARSER.parse_args()
    for post in get_posts(arguments.pelican_root_directory):
        import pdb

        pdb.set_trace()

