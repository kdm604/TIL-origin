import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'

//VueRouter를 사용하기 위한코드
Vue.use(VueRouter)

//router와 component를 연결
const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  }
]

const router = new VueRouter({
  //뷰 라우터를 설치할때 설정했던 히스토리모드 on/off설정
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
