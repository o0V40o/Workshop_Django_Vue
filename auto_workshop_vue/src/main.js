import Vue from 'vue'
import App from './App'
import router from './router'
import MuseUI from 'muse-ui';
import'muse-ui/dist/muse-ui.css';
import theme from 'muse-ui/lib/theme';
import vueHeadful from 'vue-headful';

Vue.config.productionTip = false
Vue.use(MuseUI);
theme.use('dark');
Vue.component('vue-headful', vueHeadful);

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    components: {App},
    template: '<App/>'
})
