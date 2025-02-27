<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <router-link class="navbar-brand" to="/dashboard">Project Manager</router-link>
      </div>
    </nav>
    <div class="container mt-4">
      <ProjectForm />
      <ProjectList />
    </div>
    <router-view />
  </div>
</template>

<script>
import ProjectForm from './components/ProjectForm.vue';
import ProjectList from './components/ProjectList.vue';

export default {
  name: 'App',
  components: { ProjectForm, ProjectList }
};
</script>