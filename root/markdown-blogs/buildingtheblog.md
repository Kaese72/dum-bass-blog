# Building the blog

I have a lot of stupid ideas... I like to think about them as misunderstood pieces of art, not because they have
any particular value, but because my they are a way for me to express myself and entertain the people around me. 

Some of these ideas are just thought experiements, like `Umami Lies`, but others are quite practical and arguably useful
for someone with to much time on their hands, like `A practical implementation of "download more RAM"`.

For quite some time it has been on my mind to write some of these ideas down and let people revel in my apparent stupidity
in the hopes that it will entertain someone. Should I write a book? Should I make a podcast like other great creators? No... I am
to lazy for that. I will create... a blog.

## Background

### The seed of an idea

Some time ago I was watching a [video about WSL](https://www.youtube.com/watch?v=tuhzVDc0Slg) where Scott Hanselman at some
point talked about the development of his blog. It had a pretty cool feature, where the blog on the front page included
a reference to a Git repository the blog was built from. Whenever an update was made via git, the blog would be built and
deployed with a now new reference to the commit. I though this was pretty cool and wanted to replicate this concept.

This great idea combined with a will to express a myriad of stupid ideas lead to the creation of this blog.

### The architecture

The first rule of building anything is to over engineer the architecture. For this reason I am not going
to thing about it at all, and instead just wing it. There are a couple of things I want to be able to do though

* Write blog posts in Markdown
* Present the latest blog post on the front page
* See all blog posts in chronological
* Deploy on Kubernetes
* Have everything close to code
* Not be to serious about anything

### The design

In retrospect I realize that to anyone who visits the blog it will be immediately apparent that I am not a 
UI guy. I am a backend and script guy, not visuals and art. 

I wanted the blog to have the look and feel of some kind of technical report, with a front page, table of contents,
sections, etc. I could have just create a word document and upload a PDF... but that would be too easy. I also want to
learn webdesign since I effectively suck at it (at the time of writing, but probably still too). 

## The Journey

The first few iterations of the blogs lived solely on my computer and are not worth showcasing. Keep in mind that the
only successful webdesign I had done before was a small project in grade school, so when I call the blog `he best webdesign in my life`,
you need to have appropriate expectations. 

Anyway, the "first" iteraction looked like "this"... and I realize my current solution does not support inputing pictures in the blog post... Instead of solving the problem I have elected to ignore it and add the capability later.


