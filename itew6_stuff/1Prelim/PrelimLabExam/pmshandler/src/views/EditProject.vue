<template>
    <div class="container mt-5">
        <h2>Edit Project Status</h2>
        <form @submit.prevent="updateStatus">
            <div class="mb-3">
                <label class="form-label">Status</label>
                <select v-model="project.status" class="form-select" required>
                    <option>In progress</option>
                    <option>Done</option>
                </select>
            </div>
            <button type="submit" class="btn btn-primary">Update</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return { project: {} };
    },
    beforeRouteEnter(to, from, next) {
        const projects = JSON.parse(localStorage.getItem('projects')) || [];
        const project = projects.find(p => p.id === to.params.id);
        if (project && project.status === 'done') {
            alert('This project is already completed and cannot be edited.');
            next('/dashboard');
        } else {
            next(vm => vm.project = project || {});
        }
    },
    methods: {
        updateStatus() {
            let projects = JSON.parse(localStorage.getItem('projects')) || [];
            projects = projects.map(p => p.id === this.project.id ? this.project : p);
            localStorage.setItem('projects', JSON.stringify(projects));
            this.$router.push('/dashboard');
        }
    }
};
</script>