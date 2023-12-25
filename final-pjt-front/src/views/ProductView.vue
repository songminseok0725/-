<!-- <template>
  <div>
    <p>
      <span @click="select = 0">정기 예금</span>
      |
      <span @click="select = 1">정기 적금</span>
    </p>
    <DepositeView v-if="select === 0" />
    <SavingView v-if="select === 1" />
  </div>
  <RouterView />
</template> -->

<template>
  <div class="product-container">
    <p class="product-title">상품분류</p>
    <div class="product-selector">
      <span @click="select = 0" :class="{ selected: select === 0 }"
        >정기 예금 조회</span
      >
      |
      <span @click="select = 1" :class="{ selected: select === 1 }">
        정기 적금 조회</span
      >
    </div>
    <div class="view-container">
      <DepositeView v-if="select === 0" />
      <SavingView v-if="select === 1" />
      <RouterView />
    </div>
  </div>
</template>

<script setup>
import { RouterView, RouterLink } from "vue-router";
import DepositeView from "@/views/DepositeView.vue";
import SavingView from "@/views/SavingView.vue";
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRoute } from "vue-router";
import { useCounterStore } from "../stores/counter";

const route = useRoute();
const select = ref(0);
const store = useCounterStore();
store.updatedProduct = 0;

select.value = parseInt(route.query.selectInput);
onMounted(() => {
  store.getWholeProduct();
});
</script>

<style scoped>
.product-container {
  /* max-width: 600px; */
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.product-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
}

.product-selector {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.product-selector span {
  cursor: pointer;
  margin-right: 10px;
  font-size: 16px;
  color: #333;
}

.product-selector span.selected {
  color: #009688;
  border-bottom: 2px solid #009688;
}
</style>
