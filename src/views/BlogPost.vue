
<template>
  <div class="a4-paper">
    <div class="blog-header-bar">
      <div class="header-row">
        <div class="header-link">
          <router-link v-if="prevBlog" :to="`/blogs/${prevBlog}/`">&lt; Previous</router-link>
        </div>
        <div class="header-title">
          <div class="main-title">{{ blogTitle }}</div>
          <div class="sub-title">{{ blogSeries }}</div>
        </div>
        <div class="header-link" style="text-align:right">
          <router-link v-if="nextBlog" :to="`/blogs/${nextBlog}/`">Following &gt;</router-link>
        </div>
      </div>
      <div class="header-row">
        <div class="header-created">{{ blogCreated }}</div>
      </div>
    </div>
    <div v-if="loading">Loading...</div>
    <div v-else v-html="blogHtml"></div>
  </div>
</template>

<script setup>

import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import MarkdownIt from 'markdown-it';
const route = useRoute();
const blogHtml = ref('');
const blogTitle = ref('');
const blogCreated = ref('');
const blogSeries = ref('');
const loading = ref(true);
const prevBlog = ref(null);
const nextBlog = ref(null);


async function loadBlog() {
  loading.value = true;
  try {
    // Fetch blogs.json to get folder and title
    const blogsRes = await fetch('/blogs.json');
    const blogsData = await blogsRes.json();
    const blog = blogsData.blogs[route.params.folder];
    if (!blog) {
      blogTitle.value = 'Post not found';
      blogHtml.value = '';
      loading.value = false;
      return;
    }
    blogTitle.value = blog.title;
    blogCreated.value = blog.created;
    blogSeries.value = blog.series || '';
    // Find prev/next in index
    const idx = blogsData.index.indexOf(route.params.folder);
    prevBlog.value = idx > 0 ? blogsData.index[idx - 1] : null;
    nextBlog.value = idx < blogsData.index.length - 1 ? blogsData.index[idx + 1] : null;
    // Fetch the markdown file
    const mdRes = await fetch(`/markdownblogs/${route.params.folder}.md`);
    const mdText = await mdRes.text();
    const md = new MarkdownIt();
    blogHtml.value = md.render(mdText);
  } catch (e) {
    blogTitle.value = 'Error loading post';
    blogHtml.value = '';
  }
  loading.value = false;
}

onMounted(loadBlog);

import { watch } from 'vue';
watch(() => route.params.folder, loadBlog);
</script>
<style scoped>
.blog-header-bar {
  border-bottom: 2px solid #ccc;
  border-top: 2px solid #ccc;
  margin-bottom: 2rem;
  padding: 0.5rem 0 0.5rem 0;
}
.header-row {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}
.header-link {
  flex: 1;
  min-width: 5em;
}
.header-title {
  flex: 3;
  text-align: center;
}
.main-title {
  font-size: 1.5em;
  font-weight: bold;
}
.sub-title {
  font-size: 1em;
  color: #888;
}
.header-created {
  flex: 1;
  text-align: center;
  color: #666;
  font-size: 0.9em;
  margin-top: 0.2em;
}
.a4-paper :deep(img), :deep(.a4-paper) img {
  max-width: 100% !important;
  height: auto !important;
  display: block;
  margin: 1rem 0;
}
</style>
