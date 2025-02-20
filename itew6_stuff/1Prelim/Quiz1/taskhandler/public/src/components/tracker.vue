<template>
    <div id="app">
      <h1>Task Tracker</h1>
  
      <!-- Add Task Section -->
      <div>
        <label for="new-task">Add Task:</label>
        <input 
          id="new-task" 
          v-model="newTask" 
          placeholder="Enter a task"
        />
        <button @click="addTask">Add</button>
      </div>
  
      <!-- Task List Section -->
      <div>
        <h3>Tasks:</h3>
        <div v-for="(task, index) in tasks" :key="index">
          <input 
            type="checkbox" 
            v-model="task.completed" 
          />
          <span :class="{ completed: task.completed }">{{ task.name }}</span>
          <button @click="deleteTask(index)">Delete</button>
        </div>
      </div>
  
      <!-- Task Summary Section -->
      <div>
        <p>Total Tasks: {{ totalTasks }}</p>
        <p>Completed Tasks: {{ completedTasks }}</p>
        <p>Message: {{ message }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        newTask: "",
        tasks: []
      };
    },
    computed: {
      totalTasks() {
        return this.tasks.length;
      },
      completedTasks() {
        return this.tasks.filter(task => task.completed).length;
      },
      message() {
        if (this.completedTasks === this.totalTasks && this.totalTasks > 0) {
          return "All tasks completed!";
        } else if (this.completedTasks > 0) {
          return "Some tasks completed.";
        } else {
          return "No tasks completed yet.";
        }
      }
    },
    methods: {
      addTask() {
        if (this.newTask.trim() === "") {
          alert("Task cannot be empty!");
          return;
        }
        this.tasks.push({ name: this.newTask, completed: false });
        this.newTask = "";
      },
      deleteTask(index) {
        this.tasks.splice(index, 1);
      }
    }
  };
  </script>
  
  <style>
  body {
    font-family: Arial, sans-serif; 
    text-align: center;
    background: #a0a8af;
  }
  #app {
    max-width: 500px;
    margin: 50px auto;
    background: rgb(5, 1, 1);
    padding: 20px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  }
  .completed {
    text-decoration: line-through;
    color: gray;
  }
  button {
    margin-left: 10px;
    background-color: rgb(221, 56, 56   );
    color: rgb(5, 1, 1);
    border: none;
    padding: 5px;
    cursor: pointer;
  }
  button:hover {
    background-color: rgb(30, 231, 12);
  }
  </style>