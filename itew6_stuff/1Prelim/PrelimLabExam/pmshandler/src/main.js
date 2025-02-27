import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import './assets/bootstrap.min.css';
import './assets/bootstrap.bundle.min.js';
import ProjectForm from './components/ProjectForm.vue';
import ProjectList from './components/ProjectList.vue';

const app = createApp(App);
app.component('ProjectForm', ProjectForm);
app.component('ProjectList', ProjectList);
app.use(router);
app.mount('#app');