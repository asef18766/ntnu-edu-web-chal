import { createRouter, createWebHistory }  from 'vue-router'
import App from "./App.vue"
import PostView from "./components/PostView.vue"
import PostSubmit from "./components/PostSubmit.vue"
import PostEdit from "./components/PostEdit.vue"

const routes = [
  { path: '/', redirect: '/view' },
  { path: '/view', component: PostView, children: [{ path: ':id', component: PostView }] },
  { path: '/submit', component: PostSubmit },
  { path: '/edit', component: PostEdit },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
