"""Script for building markdown blogs from a directory of markdown files."""

import argparse
import dataclasses
import os
import time
import markdown
import json

FRONTPAGEPLACEHOLDER = "###FRONTPAGEPLACEHOLDER###"
NAVLISTPLACEHOLDER = "###NAVLISTPLACEHOLDER###"


@dataclasses.dataclass
class BlogDefinition:
    title: str
    folder: str


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


def main(destination_folder: str) -> None:
    """Build markdown blogs from a directory of markdown files.

    Args:
        markdown_folder (str): The name of the folder containing markdown files.
        destination_folder (str): The name of the folder to save the built blogs.
    """
    try:
        os.mkdir(destination_folder)
    except FileExistsError:
        pass
    # Read the markdown files
    with open("src/blog.template.html", "r", encoding="utf-8") as file:
        blog_template = file.read()

    with open("src/blogs.json", "r", encoding="utf-8") as file:
        blogs: list[BlogDefinition] = []
        for blog in json.load(file):
            blogs.append(BlogDefinition(**blog))

    with open(f"{destination_folder}/index.html", "w", encoding="utf-8") as file:
        file.write(render_front_page(blogs[0], blog_template))

    with open(f"{destination_folder}/bloglist.html", "w", encoding="utf-8") as file:
        file.write(render_blog_list_page(blogs, blog_template))

    for blog in blogs:
        try:
            os.mkdir(f"{destination_folder}/{blog.folder}")
        except FileExistsError:
            pass
        with open(
            f"{destination_folder}/{blog.folder}/index.html", "w", encoding="utf-8"
        ) as file:
            file.write(render_blog_page(blog, blog_template))


if __name__ == "__main__":
    before = time.time()
    PARSER = argparse.ArgumentParser(description="Build dynamic root.")
    PARSER.add_argument("--output-dir", type=str, default="root")
    ARGS = PARSER.parse_args()
    main(ARGS.output_dir)
    print(f"Built in {time.time() - before:.2f} seconds. Finished at {time.ctime()}")
