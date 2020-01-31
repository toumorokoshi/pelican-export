from dataclasses import dataclass
from typing import Dict, Optional
from pelican import signals
from .wordpress import WordpressExporter


_EXPORTER_BY_EXPORT_TYPE = {"wordpress": WordpressExporter}
_EXPORTER: Optional[WordpressExporter] = None
# as pelican is only used as a cli, some of these are globals
# that will persist until the process dies.
_PROCESSED_POST_LIST = []


class PelicanExportException(Exception):
    """Generic exception for PelicanExport"""


def configure_exporter(
    export_type: str = "wordpress", export_configuration: Optional[Dict] = None
) -> None:
    """
    Use this method in your pelicanconf.py to configure the
    exporting process, like so::

        from pelican_export import configure_exporter 
        configure_exporter(export_type="wordpress", export_configuration={
            "url": "http://example.com/xmlrpc.php", "username": "foo", "password": "bar"
        })
    """
    if export_type not in _EXPORTER_BY_EXPORT_TYPE:
        raise PelicanExportException(
            f"unable to find export_type {export_type}. Known types are {_EXPORTER_BY_EXPORT_TYPE}"
        )
    global _EXPORTER
    _EXPORTER = _EXPORTER_BY_EXPORT_TYPE[export_type](**export_configuration)


# pelican plugins expect the following functions
def register():
    signals.article_generator_write_article.connect(_process_article)
    signals.finalized.connect(_finalize)


def _process_article(_, content):
    processed_post = _EXPORTER.process_post(content)
    if processed_post:
        _PROCESSED_POST_LIST.append(processed_post)


def _finalize(_):
    _EXPORTER.publish_posts(_PROCESSED_POST_LIST)
