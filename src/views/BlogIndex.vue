<template>
  <div class="a4-paper">
    <h2>All Blog Posts</h2>
    <ul>
      <li v-for="blogFolder in blogs.index" :key="blogFolder">
        <router-link :to="`/blogs/${blogFolder}`">{{ blogs.blogs[blogFolder].title }}</router-link>
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
