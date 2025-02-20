<template>
  <div class="container text-center mt-5">
    <h1>Task Handler</h1>
    <TaskForm @add-task="addTask" />
    <TaskList :tasks="tasks" @toggle-task="toggleTask" @remove-task="removeTask" />
    <TaskSummary :tasks="tasks" />
  </div>
</template>

<script>
import { ref } from 'vue';
import TaskForm from './components/TaskForm.vue';
import TaskList from './components/TaskList.vue';
import TaskSummary from './components/TaskSummary.vue';

export default {
  components: { TaskForm, TaskList, TaskSummary },
  setup() {
    const tasks = ref([]);

    const addTask = (taskText) => {
      if (taskText.trim()) {
        tasks.value.push({ id: Date.now(), text: taskText, completed: false });
      }
    };

    const toggleTask = (id) => {
      const task = tasks.value.find((task) => task.id === id);
      if (task) task.completed = !task.completed;
    };

    const removeTask = (id) => {
      tasks.value = tasks.value.filter((task) => task.id !== id);
    };

    return { tasks, addTask, toggleTask, removeTask };
  }
};
</script>
