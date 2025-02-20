<template>
    <div class="input-group my-3">
        <input v-model="newTask" type="text" class="form-control" placeholder="Enter task..." />
        <button class="btn btn-primary" @click="submitTask">Add Task</button>
    </div>
</template>

<script>
import { ref } from 'vue';

export default {
    emits: ['add-task'],
    setup(_, { emit }) {
        const newTask = ref('');

        const submitTask = () => {
            if (newTask.value.trim()) {
                emit('add-task', newTask.value);
                newTask.value = '';
            }
        };

        return { newTask, submitTask };
    }
};
</script>