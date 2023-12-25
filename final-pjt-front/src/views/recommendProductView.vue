<template>
  <div class="recommendation-container">
    <h2 class="section-title">상품 추천 받기</h2>
    <hr class="divider" />

    <div class="product-category-container">
      <h3 class="product-category">예금 상품 추천</h3>
      <hr class="divider" />

      <div v-for="depo in recommendDeposites" :key="depo.id" class="product-item">
        <div class="product-info">
          <p class="company">{{ depo.kor_co_nm }}</p>
          <p class="product-name">{{ depo.fin_prdt_nm }}</p>
        </div>
        <div class="additional-info">
          <p class="join-info">{{ depo.join_deny }}</p>
          <p class="join-way">{{ depo.join_way }}</p>
          <p class="special-condition">{{ depo.spcl_cnd }}</p>
        </div>
        <hr class="divider" />
      </div>
    </div>

    <div class="product-category-container">
      <h3 class="product-category">적금 상품 추천</h3>
      <hr class="divider" />

      <div v-for="saving in recommendSavings" :key="saving.id" class="product-item">
        <div class="product-info">
          <p class="company">{{ saving.kor_co_nm }}</p>
          <p class="product-name">{{ saving.fin_prdt_nm }}</p>
        </div>
        <div class="additional-info">
          <p class="join-info">{{ saving.join_deny }}</p>
          <p class="join-way">{{ saving.join_way }}</p>
          <p class="special-condition">{{ saving.spcl_cnd }}</p>
        </div>
        <hr class="divider" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from "@/stores/counter";
import { storeToRefs } from "pinia";
import { ref, onMounted } from "vue";

const store = useCounterStore();
const { recommendDeposites, recommendSavings } = storeToRefs(store);

onMounted(() => {
  store.getRecommendDeposites();
  store.getRecommendSavings();
});
</script>

<style scoped>
.recommendation-container {
  padding: 20px;
}

.section-title {
  font-size: 24px;
  color: #333;
  margin-bottom: 10px;
}

.product-category-container {
  margin-bottom: 20px;
}

.product-category {
  font-size: 20px;
  color: #009688;
  margin-bottom: 10px;
}

.divider {
  margin-top: 10px;
  border: none;
  border-top: 1px solid #ddd;
}

.product-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px;
  background-color: #f5f5f5;
  border-radius: 8px;
  margin-bottom: 15px;
}

.product-info {
  flex: 1;
}

.additional-info {
  flex: 2;
}

.company {
  font-weight: bold;
}

.product-name {
  color: #333;
}

.join-info,
.join-way,
.special-condition {
  color: #777;
  margin-top: 5px;
}
</style>
