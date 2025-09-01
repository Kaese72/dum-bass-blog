<template>
  <div class="a4-paper">
    <h2>All Blog Posts</h2>
    <table class="blog-index-table">
      <thead>
        <tr>
          <th>Title</th>
          <th>Series</th>
          <th>Created</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="blogFolder in blogs.index" :key="blogFolder" class="clickable-row" @click="goToBlog(blogFolder)">
          <td>
            <router-link :to="`/blogs/${blogFolder}/`" @click.stop>{{ blogs.blogs[blogFolder].title }}</router-link>
          </td>
          <td>{{ blogs.blogs[blogFolder].series }}</td>
          <td>{{ blogs.blogs[blogFolder].created }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const blogs = ref({ index: [], blogs: {} });
const router = useRouter();

function goToBlog(blogFolder) {
  router.push(`/blogs/${blogFolder}/`);
}

onMounted(async () => {
  try {
    const res = await fetch('/blogs.json');
    if (res.ok) {
      blogs.value = await res.json();
    }
  } catch (e) {
    // handle error
  }
});
</script>
<style scoped>
.blog-index-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1.5em;
  background: #fff;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}
.blog-index-table th, .blog-index-table td {
  border: 1px solid #ddd;
  padding: 0.75em 1em;
  text-align: left;
}
.blog-index-table th {
  background: #f5f5f5;
  font-weight: bold;
}
.clickable-row {
  cursor: pointer;
  transition: background 0.15s;
}
.clickable-row:hover {
  background: #e6f7ff;
}
</style>

