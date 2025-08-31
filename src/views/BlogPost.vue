<template>
  <div class="a4-paper">
    <h2>{{ blogTitle }}</h2>
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
const loading = ref(true);

onMounted(async () => {
  loading.value = true;
  try {
    // Fetch blogs.json to get folder and title
    const blogsRes = await fetch('/blogs.json');
    const blogs = await blogsRes.json();
    const blog = blogs.find(b => b.folder === route.params.folder);
    if (!blog) {
      blogTitle.value = 'Post not found';
      blogHtml.value = '';
      loading.value = false;
      return;
    }
    blogTitle.value = blog.title;
    // Fetch the markdown file
    const mdRes = await fetch(`/blogs/${blog.folder}/blog.md`);
    const mdText = await mdRes.text();
    const md = new MarkdownIt();
    blogHtml.value = md.render(mdText);
  } catch (e) {
    blogTitle.value = 'Error loading post';
    blogHtml.value = '';
  }
  loading.value = false;
});
</script>
<style scoped>
.a4-paper :deep(img), :deep(.a4-paper) img {
  max-width: 100% !important;
  height: auto !important;
  display: block;
  margin: 1rem 0;
}
</style>
