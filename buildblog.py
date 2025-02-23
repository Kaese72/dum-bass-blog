"""Script for building markdown blogs from a directory of markdown files."""

import argparse
import dataclasses
import datetime
import os
import json
import shutil
import time
import markdown
import PyRSS2Gen

FRONTPAGEPLACEHOLDER = "###FRONTPAGEPLACEHOLDER###"
NAVLISTPLACEHOLDER = "###NAVLISTPLACEHOLDER###"
COMMIT_PLACEHOLDER = "###COMMIT_PLACEHOLDER###"


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
            link=f"{base_url}{self.folder}",
            description=self.description,
            guid=PyRSS2Gen.Guid(f"{base_url}{self.folder}"),
            pubDate=str(self.created),
        )


def construct_navigation_list(nav_items: list[tuple[str, str]]) -> str:
    nav_list = ""
    for nav_item in nav_items:
        nav_list += f'<a href="{nav_item[1]}">{nav_item[0]}</a>'
    return nav_list


def render_front_page(blog: BlogDefinition, blog_template: str) -> str:
    with open(f"{blog.folder}/blog.md", "r", encoding="utf-8") as file:
        frontpage_blog_html = markdown.markdown(file.read())

    return blog_template.replace(FRONTPAGEPLACEHOLDER, frontpage_blog_html).replace(
        NAVLISTPLACEHOLDER, construct_navigation_list([("Blogs", "/bloglist.html")])
    )


def render_blog_list_page(blogs: list[BlogDefinition], blog_template: str) -> str:
    bloglisttemplate = "<ul>"
    for blog in blogs:
        bloglisttemplate += (
            f'<li><a href="{blog.folder}/index.html">{blog.title}</a></li>'
        )

    bloglisttemplate += "</ul>"
    return blog_template.replace(FRONTPAGEPLACEHOLDER, bloglisttemplate).replace(
        NAVLISTPLACEHOLDER, construct_navigation_list([("Home", "/index.html")])
    )


def render_blog_page(blog: BlogDefinition, blog_template: str) -> str:
    with open(f"{blog.folder}/blog.md", "r", encoding="utf-8") as file:
        frontpage_blog_html = markdown.markdown(file.read())

    return blog_template.replace(FRONTPAGEPLACEHOLDER, frontpage_blog_html).replace(
        NAVLISTPLACEHOLDER,
        construct_navigation_list(
            [("Home", "/index.html"), ("Blogs", "/bloglist.html")]
        ),
    )


def substitute_and_write(
    page: str,
    substitutions: dict[str, str],
    destination: str,
) -> None:
    for key, value in substitutions.items():
        page = page.replace(key, value)
    with open(destination, "w", encoding="utf-8") as file:
        file.write(page)


def put_folder(folder: str) -> None:
    try:
        os.mkdir(folder)
    except FileExistsError:
        pass


def main(destination_folder: str, substitutions: dict[str, str], base_url: str) -> None:
    """Build markdown blogs from a directory of markdown files.

    Args:
        markdown_folder (str): The name of the folder containing markdown files.
        destination_folder (str): The name of the folder to save the built blogs.
    """
    put_folder(destination_folder)
    # Read the markdown files
    with open("src/blog.template.html", "r", encoding="utf-8") as file:
        blog_template = file.read()

    with open("src/blogs.json", "r", encoding="utf-8") as file:
        blogs = [BlogDefinition.parse(b) for b in json.load(file)]

    for blog in blogs:
        put_folder(f"{destination_folder}/{blog.folder}")
        try:
            resources = os.listdir(f"{blog.folder}/resources")
        except FileNotFoundError:
            # If there are no resources there is nothing to do
            pass
        else:
            put_folder(f"{destination_folder}/{blog.folder}/resources")
            for resource_file in resources:
                shutil.copy(
                    f"{blog.folder}/resources/{resource_file}",
                    f"{destination_folder}/{blog.folder}/resources/{resource_file}",
                )
        substitute_and_write(
            page=render_blog_page(blog, blog_template),
            substitutions=substitutions,
            destination=f"{destination_folder}/{blog.folder}/index.html",
        )

    substitute_and_write(
        page=render_front_page(blogs[0], blog_template),
        substitutions=substitutions,
        destination=f"{destination_folder}/index.html",
    )
    # For resources on the front page to work
    try:
        # delete symlink if it exists. Mostlry used for local development
        os.unlink(f"{destination_folder}/resources")
    except FileNotFoundError:
        pass
    os.symlink(
        f"{blogs[0].folder}/resources/",
        f"{destination_folder}/resources",
        target_is_directory=True,
    )

    substitute_and_write(
        page=render_blog_list_page(blogs, blog_template),
        substitutions=substitutions,
        destination=f"{destination_folder}/bloglist.html",
    )

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
    before = time.time()
    PARSER = argparse.ArgumentParser(description="Build dynamic root.")
    PARSER.add_argument("--output-dir", type=str, default="root")
    PARSER.add_argument("--commit", type=str, default="yeetusgititus")
    PARSER.add_argument("--base-url", type=str, default="https://blog.kaese.space/")
    ARGS = PARSER.parse_args()
    assert ARGS.base_url.endswith("/"), "must end url with / for rss feed to work"
    main(
        destination_folder=ARGS.output_dir,
        substitutions={COMMIT_PLACEHOLDER: ARGS.commit},
        base_url=ARGS.base_url,
    )
    print(f"Built in {time.time() - before:.2f} seconds. Finished at {time.ctime()}")
