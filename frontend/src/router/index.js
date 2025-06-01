import { createRouter, createWebHistory } from 'vue-router'
import SharkComponent from '../components/SharkComponent.vue'
import GamesComponent from '../components/GamesComponent.vue'

const routes = [
  {
		path: '/shark',
		name: 'SharkComponent',
		component: SharkComponent
	},
	{
		path: '/',
		name: 'GamesComponent',
		component: GamesComponent
	}
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
