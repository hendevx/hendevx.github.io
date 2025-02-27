<template>
    <form @submit.prevent="submitForm">
        <div class="mb-3">
            <label class="form-label">Project Name</label>
            <input v-model="project.name" type="text" class="form-control" required />
        </div>
        <div class="mb-3">
            <label class="form-label">Start Date</label>
            <input v-model="project.startDate" type="date" class="form-control" required />
        </div>
        <div class="mb-3">
            <label class="form-label">End Date</label>
            <input v-model="project.endDate" type="date" class="form-control" required />
        </div>
        <div class="mb-3">
            <label class="form-label">Size</label>
            <select v-model="project.size" class="form-select" required>
                <option>small</option>
                <option>medium</option>
                <option>large</option>
            </select>
        </div>
        <button type="submit" class="btn btn-primary">Save</button>
    </form>
</template>

<script>
export default {
    data() {
        const today = new Date();
        const twoWeeksLater = new Date(today);
        twoWeeksLater.setDate(today.getDate() + 14);
        return { 
            project: { 
                name: '', 
                startDate: today.toISOString().substr(0, 10), 
                endDate: twoWeeksLater.toISOString().substr(0, 10), 
                size: '', 
                status: 'In progress' 
            } 
        };
    },
    methods: {
        submitForm() {
            const projects = JSON.parse(localStorage.getItem('projects')) || [];
            projects.push({ ...this.project, id: Date.now().toString() });
            localStorage.setItem('projects', JSON.stringify(projects));
            this.$router.push('/dashboard');
        }
    }
};
</script>