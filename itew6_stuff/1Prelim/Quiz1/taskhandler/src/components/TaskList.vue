<template>
    <ul class="list-group">
      <li v-for="task in tasks" :key="task.id" class="list-group-item d-flex align-items-center">
        <input 
          type="checkbox" 
          :checked="task.completed" 
          @change="$emit('toggle-task', task.id)" 
          class="form-check-input me-2"
        />
        <span class="flex-grow-1 text-start" :class="{ 'text-decoration-line-through': task.completed }">
          {{ task.text }}
        </span>
        <button class="btn btn-link text-danger p-0 ms-3" @click="$emit('remove-task', task.id)">Delete</button>
      </li>
    </ul>
  </template>
  
  <script>
  export default {
    props: ['tasks'],
    emits: ['toggle-task', 'remove-task']
  };
  </script>
  