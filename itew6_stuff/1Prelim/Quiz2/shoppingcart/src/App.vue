<template>
  <div class="container mt-4">
    <h1 class="text-center">Tech Shop</h1>
    <div class="row">
      <div class="col-md-6">
        <ProductList @add-to-cart="addToCart" />
      </div>
      <div class="col-md-6">
        <ShoppingCart :cart="cart" @update-cart="updateCart" />
      </div>
    </div>
  </div>
</template>


<script>
import { ref } from 'vue';
import ProductList from './components/ProductList.vue';
import ShoppingCart from './components/ShoppingCart.vue';


export default {
  components: { ProductList, ShoppingCart },
  setup() {
    const cart = ref([]);

    const addToCart = (product) => {
      const item = cart.value.find((item) => item.id === product.id);
      if (item) {
        item.quantity++;
      } else {
        cart.value.push({ ...product, quantity: 1 });
      }
    };

    const updateCart = (updatedCart) => {
      cart.value = updatedCart;
    };

    return { cart, addToCart, updateCart };
  }
};
</script>
