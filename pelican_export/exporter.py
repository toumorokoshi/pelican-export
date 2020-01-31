import abc
from typing import Dict, Iterable, Optional


class Exporter(abc.ABC):
    """
    The exporter ABC declares a generic interface that exporters
    can implement. As long as the exporter adheres to this interface,
    the exporter will be able to use it.
    """

    @abc.abstractmethod
    def __init__(self):
        """
        Exporters are passed the configuration expanded as dictated in the
        export_configuration dictionary for configure_exporter. This should
        be used to configure things such as clients to the system you're 
        exporting to.
        """

    @abc.abstractmethod
    def process_post(self, content) -> Optional[object]:
        """
        Process post is given a pelican content object, and is expected
        to be returned an object that represents a post in your target
        platform, to be processed in publish_posts.

        None can be returned if the content should be skipped.
        """

    @abc.abstractmethod
    def publish_posts(self, processed_posts: Iterable[object]):
        """
        Publish posts should consume a list of posts to process
        (the return object of process_post), and submit them all.
        """
