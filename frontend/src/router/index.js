import Vue from 'vue';
import VueRouter from 'vue-router';

import Dashboard from '@/views/Dashboard'
import Profile from '@/views/Profile';

Vue.use(VueRouter);

const routes = [
  {
    name: 'dashboard',
    path: '/',
    component: Dashboard,
  },

  {
    name: 'profile',
    path: '/profile',
    component: Profile,
  },

  {
    path: '*',
    redirect: '/',
  },
];

const router = new VueRouter({
  mode: 'history',
  routes
});

export default router;
