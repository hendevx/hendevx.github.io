<template>
    <div class="mt-3">
        <p>Total Tasks: {{ tasks.length }}</p>
        <p>Pending: {{ pendingTasks }}</p>
        <p>Completed: {{ completedTasks }}</p>
    </div>
</template>

<script>
import { computed } from 'vue';

export default {
    props: ['tasks'],
    setup(props) {
        const pendingTasks = computed(() => props.tasks.filter(task => !task.completed).length);
        const completedTasks = computed(() => props.tasks.filter(task => task.completed).length);

        return { pendingTasks, completedTasks };
    }
};
</script>