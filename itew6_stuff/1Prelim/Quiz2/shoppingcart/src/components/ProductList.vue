<template>
    <div class="card p-3">
      <h2 class="text">Products <i class="bi bi-box"></i></h2>
      <ul class="list-group">
        <li v-for="product in products" :key="product.id" class="list-group-item d-flex justify-content-between align-items-center">
          <span>{{ product.name }} - ₱{{ product.price }}</span>
          <button class="btn btn-success btn-sm" @click="$emit('add-to-cart', product)">Add to Cart</button>
        </li>
      </ul>
    </div>
  </template>
  


<script>
export default {
    emits: ['add-to-cart'],
    setup() {
        const products = [
            { id: 1, name: 'HP Laptop 8GB RAM 1 TB Memory', price: 24999 },
            { id: 2, name: 'JBL Headphones', price: 499 },
            { id: 3, name: 'Logitech Mouse Wired Silent', price: 599 },
            { id: 4, name: 'Brother All-in-One Printer', price: 4999 },
            { id: 5, name: 'LAN Cable 5m', price: 399 },
            { id: 6, name: 'Samsung SSD 2TB', price: 7999 }
        ];

        return { products };
    }
};
</script>