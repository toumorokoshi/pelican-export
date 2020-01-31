import logging
from argparse import ArgumentParser
from datetime import datetime
from typing import Iterable, Dict, Optional
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts
from .exporter import Exporter

GET_POST_PAGE_COUNT = 10

LOG = logging.getLogger(__name__)


class WordpressExporter(Exporter):
    """
    Publish all posts to Wordpress.

    * posts are created as drafts, to allow the exporter
      to review before publishing.
    """

    def __init__(
        self,
        url: str,
        username: str,
        password: str,
        post_status: str = "draft",
    ):
        """
        The following configuration parameters are supported
        """
        self._client = Client(url, username, password)
        self._post_status = post_status

    def process_post(self, content) -> Optional[WordPressPost]:
        """Create a wordpress post based on pelican content"""
        if content.status == "draft":
            return None
        post = WordPressPost()
        post.title = content.title
        post.slug = content.slug
        post.content = content.content
        # this conversion is required, as pelican uses a SafeDateTime
        # that python-wordpress-xmlrpc doesn't recognize as a valid date.
        post.date = datetime.fromisoformat(content.date.isoformat())
        post.term_names = {
            "category": [content.category.name],
        }
        if hasattr(content, "tags"):
            post.term_names["post_tag"] = [tag.name for tag in content.tags]
        return post

    def publish_posts(self, processed_posts: Iterable[WordPressPost]):
        post_id_by_title = self._get_post_id_by_title()
        operation = "null"
        for post in processed_posts:
            if post.title in post_id_by_title:
                post.id = post_id_by_title[post.title]
                operation = "creating"
            else:
                post.id = self._client.call(posts.NewPost(post))
                operation = "updating"
            post.post_status = self._post_status
            LOG.info(f"{operation} post {post.title}, post id {post.id}")
            self._client.call(posts.EditPost(post.id, post))

    def _get_post_id_by_title(self) -> Dict[str, int]:
        """Get all post ids, by their title."""
        post_id_by_title = {}
        page = 0
        while True:
            posts_on_page = self._client.call(
                posts.GetPosts({"offset": page * GET_POST_PAGE_COUNT})
            )
            for post in posts_on_page:
                post_id_by_title[post.title] = post.id

            # we know we're done processing all posts if we
            # get fewer posts than the page would return max.
            if len(posts_on_page) < GET_POST_PAGE_COUNT:
                break
            page += 1
        return post_id_by_title
