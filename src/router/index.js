import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import Container from "@/components/Container.vue"
import Header from "@/components/Header.vue"
import Main from "@/components/Main.vue"
import Footer from "@/components/Footer.vue"

import Test from "@/components/Test.vue"

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: {name: "index"},
      component: Container,
      children: [
        {
          path: "index",
          name: "index",
          components: {
            header: Header,
            body: Main,
            footer: Footer
          }
        }
      ]
    },
    {
      path: "/test",
      component: Test,
    }
  ]
})
