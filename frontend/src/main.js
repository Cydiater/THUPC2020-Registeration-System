import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import VueMarkdown from 'vue-markdown';

import router from '@/router';
import store from '@/store';

Vue.config.productionTip = false

Vue.use(VueMarkdown);

new Vue({
  vuetify,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
