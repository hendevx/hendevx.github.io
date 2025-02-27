import { createRouter, createWebHistory } from 'vue-router';
import Login from './views/Login.vue';
import Dashboard from './views/Dashboard.vue';
import EditProject from './views/EditProject.vue';

const isAuthenticated = () => {
  return localStorage.getItem('user') !== null;
};

const getUserRole = () => {
  const user = localStorage.getItem('user');
  return user ? JSON.parse(user).role : null;
};

const routes = [
  { path: '/', component: Login },
  { path: '/dashboard', component: Dashboard, meta: { requiresAuth: true } },
  { 
    path: '/edit/:id', 
    component: EditProject, 
    meta: { requiresAuth: true, requiresAdmin: true } 
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !isAuthenticated()) {
    next('/');
  } else if (to.meta.requiresAdmin && getUserRole() !== 'admin') {
    next('/dashboard');
  } else {
    next();
  }
});

export default router;