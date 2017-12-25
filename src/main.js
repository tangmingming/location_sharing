// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import 'element-ui/lib/theme-chalk/index.css'
import BaiduMap from "vue-baidu-map"

Vue.use(BaiduMap, {
  ak: "IHDSKwmhHQgLvr5wZwCsZUuHyt6Thv3A"
})


Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
