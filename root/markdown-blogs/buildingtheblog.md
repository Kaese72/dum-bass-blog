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

### The "first" version of the blog

The first few iterations of the blogs lived solely on my computer and are not worth showcasing. Keep in mind that the
only successful webdesign I had done before was a small project in grade school, so when I call the blog `the best webdesign in my life`,
you need to have appropriate expectations. 

Anyway, the "first" iteraction looked like "this"... and I realize my current solution does not support inputing pictures in the blog post... Instead of solving the problem I have elected to ignore it and add the capability later.

### Deployment

There is only a few couple of things I care about when deploying,

* GitOps way of working
* Few steps to update blog

Two options seemed reasonable to me

* Proxy against github
* Build and deploy the entire blog on Kubernetes

The second option I knew how to do, but I realize in retrospect that the first would
probably have been easier to work with over time since I could have pointed the proxy
towards the master branch in Github. After some experimentation I could not figure out 
an easy way to setup the proxy because accessing the raw files from 
`raw.githubusercontent.com` did not return the content type. This can be resolved, there are
services that do it that I do not want to pay for and I wanted to move forward 
so I opted for the second option. 

I already have a K3s single node installation running on a virtual machine in Azure, so its
just a matter of deploying building and deplying the blog there. This will be done in two
easy steps

1. [Build the blog](https://github.com/Kaese72/dum-bass-blog/blob/3f4df428997a046f1dcc3a468a97ce069795fc53/.github/workflows/build-the-blog.yml)
   1. Via [Dockerfile](https://github.com/Kaese72/dum-bass-blog/blob/3f4df428997a046f1dcc3a468a97ce069795fc53/Dockerfile)
2. [Deploy the blog](https://github.com/Kaese72/dum-bass-blog/blob/3f4df428997a046f1dcc3a468a97ce069795fc53/Deployment.yaml)

Shortly before this project started, my home lab, [rectal computer](https://www.youtube.com/watch?v=y-bYSC6OT6s) had broken down because of
a disk failure. No one backs up their home labs, right? I sure had not. Coincidentally, the home lab is also the machine I had Argo CD running on.
I popped in another disk I had laying around (which will surely break down soon too), 
installed [K3s](https://k3s.io/), 
deployed [Argo CD](https://argo-cd.readthedocs.io/en/stable/getting_started/), 
and [added the Azure K3s cluster](https://argo-cd.readthedocs.io/en/stable/operator-manual/cluster-management/#adding-a-cluster). 

We're back in business!

Letting Argo CD handle the deployment is very simple in my case. There are no secrets in the deployment (yet... foreshadowing)
and the Git repository the blog is maintained in is public. 
