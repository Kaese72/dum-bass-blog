<template>
  <div class="a4-paper">
    <h2>All Blog Posts</h2>
    <ul>
      <li v-for="blog in blogs" :key="blog.folder">
        <router-link :to="`/blogs/${blog.folder}/`">{{ blog.title }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const blogs = ref([]);

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
