import { createRouter, createWebHistory } from 'vue-router';

import Home from './views/Home.vue';
import BlogIndex from './views/BlogIndex.vue';
import BlogPost from './views/BlogPost.vue';


const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/blogs', name: 'BlogIndex', component: BlogIndex },
  { path: '/blogs/:folder', name: 'BlogPost', component: BlogPost }  
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
