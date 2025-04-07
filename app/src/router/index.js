import { createRouter, createWebHistory } from "vue-router";

import Landing from "@/components/views/Landing.vue";
import Home from "@/components/views/Home.vue";
import Authentication from "@/components/views/Authentication.vue";

const routes = [
    {
        path: '/',
        component: Landing
    },
    {
        path: '/home',
        component: Home
    },
    {
        path: '/authentication-:type',
        name: 'authentication',
        component: Authentication
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router