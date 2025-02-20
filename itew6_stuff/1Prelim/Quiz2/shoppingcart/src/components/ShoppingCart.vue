<template>
    <div class="card p-3">
        <h2 class="text">Shopping Cart <i class="bi bi-cart4"></i></h2> 
        <ul class="list-group" v-if="cart.length">
            <li v-for="(item, index) in cart" :key="item.id"
                class="list-group-item d-flex justify-content-between align-items-center">
                <div>
                    <span>{{ item.name }} - ₱{{ item.price }}</span>
                    <input type="number" class="form-control d-inline w-25 ms-2" v-model="item.quantity" min="1"
                        @input="updateQuantity(index, item.quantity)">
                </div>
                <button class="btn btn-danger btn-sm" @click="removeItem(index)">Remove</button>
            </li>
        </ul>
        <p v-else class="text-muted">The cart is empty.</p>
        <h3 class="mt-3">Total: <span class="text-success">₱{{ totalPrice }}</span></h3>
    </div>
</template>


<script>
import { computed } from 'vue';

export default {
    props: {
        cart: Array
    },
    emits: ['update-cart'],
    setup(props, { emit }) {
        const totalPrice = computed(() => {
            return props.cart.reduce((sum, item) => sum + item.price * item.quantity, 0);
        });

        const updateQuantity = (index, quantity) => {
            const updatedCart = [...props.cart];
            updatedCart[index].quantity = quantity;
            emit('update-cart', updatedCart);
        };

        const removeItem = (index) => {
            const updatedCart = [...props.cart];
            updatedCart.splice(index, 1);
            emit('update-cart', updatedCart);
        };

        return { totalPrice, updateQuantity, removeItem };
    }
};
</script>