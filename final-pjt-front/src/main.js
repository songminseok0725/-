import { createApp } from "vue";
import { createPinia } from "pinia";

import "@fortawesome/fontawesome-free/css/all.css"; // 추가

import piniaPluginPersistedstate from "pinia-plugin-persistedstate";

import App from "./App.vue";
import router from "./router";

import VueGoodTablePlugin from "vue-good-table-next";
import "vue-good-table-next/dist/vue-good-table-next.css";

const app = createApp(App);
const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);
app.use(VueGoodTablePlugin);

app.use(pinia);
app.use(router);

app.mount("#app");

// import the styles
