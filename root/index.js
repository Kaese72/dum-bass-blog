blogBlobs = []
shouldRender = 0

async function renderBlogs() {
    if (blogBlobs.length == 0) {
        blogBlobsResp = await fetch("/blogs.json")
        blogBlobs = await blogBlobsResp.json()
    }

    if (shouldRender >= blogBlobs.length) {
        // No more blogs to render?
        return
    }

    // There are blogs to render :)
    blogItem = blogBlobs[shouldRender]
    content = document.getElementById('blogPostContainer')
    response = await fetch(blogItem.file)
    divElement = document.createElement("div")
    divElement.classList.add("paperSheet")
    divElement.innerHTML = marked.parse(await response.text());
    articleElement = document.createElement("article")
    articleElement.appendChild(divElement)
    content.appendChild(articleElement)
}
renderBlogs()
