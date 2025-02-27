<!-- src/views/Login.vue -->
<template>
    <div class="container mt-5">
      <h2>Login</h2>
      <form @submit.prevent="login">
        <div class="mb-3">
          <label class="form-label">Username</label>
          <input type="text" v-model="username" class="form-control" required />
        </div>
        <div class="mb-3">
          <label class="form-label">Role</label>
          <select v-model="role" class="form-select" required>
            <option value="user">User</option>
            <option value="admin">Admin</option>
          </select>
        </div>
        <button type="submit" class="btn btn-primary">Login</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        role: 'user'
      };
    },
    methods: {
      login() {
        localStorage.setItem('user', JSON.stringify({ username: this.username, role: this.role }));
        this.$router.push('/dashboard');
      }
    }
  };
  </script>
  