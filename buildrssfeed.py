"""Script for building markdown blogs from a directory of markdown files."""

import argparse
import dataclasses
import datetime
import json
import PyRSS2Gen


@dataclasses.dataclass
class BlogDefinition:
    """A class to represent a blog definition."""

    title: str
    description: str
    folder: str
    created: datetime.date

    @staticmethod
    def parse(blog_dict: dict) -> "BlogDefinition":
        """Create a BlogDefinition from a dictionary."""
        return BlogDefinition(
            title=blog_dict["title"],
            description=blog_dict["description"],
            folder=blog_dict["folder"],
            created=datetime.datetime.strptime(blog_dict["created"], "%Y-%m-%d").date(),
        )

    def rss_item(self, base_url: str) -> str:
        """
        Create an RSS item from the blog definition.
        Requires a base URL since we do not want to use relative links...
        """
        return PyRSS2Gen.RSSItem(
            title=self.title,
            link=f"{base_url}blogs/{self.folder}/",
            description=self.description,
            # This URL is wrong, but I cannot change the GUID now since something might depend on int
            guid=PyRSS2Gen.Guid(f"{base_url}{self.folder}"),
            pubDate=str(self.created),
        )


def main(base_url: str, destination_folder: str = "public") -> None:
    """Build markdown blogs from a directory of markdown files.

    Args:
        markdown_folder (str): The name of the folder containing markdown files.
        destination_folder (str): The name of the folder to save the built blogs.
    """
    with open("public/blogs.json", "r", encoding="utf-8") as file:
        blogs = [BlogDefinition.parse(b) for b in json.load(file)]

    with open(f"{destination_folder}/rss.xml", "w", encoding="utf-8") as file:
        rss = PyRSS2Gen.RSS2(
            title="Blog",
            link=base_url,
            description="RSS feed for the blog",
            lastBuildDate=datetime.datetime.now(),
            items=[b.rss_item(base_url) for b in blogs],
            docs=base_url,
        )
        rss.write_xml(file)


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description="Build dynamic root.")
    PARSER.add_argument("--output-dir", type=str, default="public")
    PARSER.add_argument("--base-url", type=str, default="https://blog.kaese.space/")
    ARGS = PARSER.parse_args()
    assert ARGS.base_url.endswith("/"), "must end url with / for rss feed to work"
    main(
        base_url=ARGS.base_url,
        destination_folder=ARGS.output_dir,
    )
