<template>
    <div class="container mt-5">
        <h2>Project Dashboard</h2>
        <button @click="logout" class="btn btn-danger">Logout</button>
        <ProjectList />
    </div>
</template>

<script>
import ProjectList from '../components/ProjectList.vue';
export default {
    components: { ProjectList },
    methods: {
        logout() {
            localStorage.removeItem('user');
            this.$router.push('/');
        }
    }
};
</script>