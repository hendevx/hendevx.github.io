<template>
    <ul class="list-group mt-3">
        <li v-for="project in projects" :key="project.id" class="list-group-item">
            {{ project.name }} - Status: {{ project.status }}
            <router-link v-if="userRole === 'admin'" :to="`/edit/${project.id}`"
                class="btn btn-sm btn-warning ms-3">Edit</router-link>
        </li>
    </ul>
</template>

<script>
export default {
    data() {
        return {
            projects: JSON.parse(localStorage.getItem('projects')) || [],
            userRole: JSON.parse(localStorage.getItem('user'))?.role || 'user'
        };
    }
};
</script>