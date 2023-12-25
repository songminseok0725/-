<template>
  <div>
    <div class="product-container">
      <h3>가입한 상품들</h3>
      <hr class="divider" />

      <div class="product-category">
        <div>
          <h4>정기 예금</h4>
          <template v-if="store.userDeposites.length">
            <p
              @click="goDepositeDetail(myDeposite.fin_prdt_cd)"
              v-for="myDeposite in store.userDeposites"
              :key="myDeposite.id"
            >
              {{ myDeposite.kor_co_nm }} | {{ myDeposite.fin_prdt_nm }}
            </p>
          </template>
          <template v-else>
            <p>가입한 정기 예금 상품이 없습니다</p>
          </template>
        </div>

        <div>
          <h4>정기 적금</h4>
          <template v-if="store.userSavings.length">
            <p
              @click="goSavingDetail(mySaving.fin_prdt_cd)"
              v-for="mySaving in store.userSavings"
              :key="mySaving.id"
            >
              {{ mySaving.kor_co_nm }} | {{ mySaving.fin_prdt_nm }}
            </p>
          </template>
          <template v-else>
            <p>가입한 정기 적금 상품이 없습니다</p>
          </template>
        </div>
      </div>
    </div>

    <hr class="divider" />

    <div class="interest-rate-container">
      <h3>가입한 상품 금리</h3>
      <div v-if="show != 0" class="chart-container">
        <canvas id="myChart"></canvas>
      </div>
      <div v-else>
        <p>가입한 상품이 없습니다.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch, onBeforeMount, computed } from "vue";
import { useCounterStore } from "@/stores/counter";
import { storeToRefs } from "pinia";
import { useRouter } from "vue-router";

import axios from "axios";
import Chart from "chart.js/auto";

const router = useRouter();
const store = useCounterStore();
const label = ref([]);
const a1 = ref([]);
const a2 = ref([]);
const { userDeposites, userSavings } = storeToRefs(store);
const show = computed(() => {
  return userDeposites.value.length + userSavings.value.length;
});
onMounted(() => {
  const ctx = document.getElementById("myChart");
  label.value = [
    ...store.userDeposites.map((elem) => elem.fin_prdt_nm),
    ...store.userSavings.map((elem) => elem.fin_prdt_nm),
  ];
  const d1 = store.userDeposites.map((elem) => elem.deposite_optionlist_set);
  const d2 = store.userSavings.map((elem) => elem.saving_optionlist_set);
  a1.value = [];
  a2.value = [];
  for (const a of d1) {
    let minVal = 100;
    let maxVal = 0;
    for (const b of a) {
      minVal = minVal > b.intr_rate ? b.intr_rate : minVal;
      maxVal = maxVal < b.intr_rate ? b.intr_rate : maxVal;
    }
    a1.value.push(minVal);
    a2.value.push(maxVal);
  }
  for (const a of d2) {
    let minVal = 100;
    let maxVal = 0;
    for (const b of a) {
      minVal = minVal > b.intr_rate ? b.intr_rate : minVal;
      maxVal = maxVal < b.intr_rate ? b.intr_rate : maxVal;
    }
    a1.value.push(minVal);
    a2.value.push(maxVal);
  }
  if (label.value.length > 0 && a1.value.length > 0 && a2.value.length > 0) {
    new Chart(ctx, {
      type: "bar",
      data: {
        labels: label.value,
        datasets: [
          {
            label: "저축금리",
            data: a1.value,
            borderWidth: 1,
          },
          {
            label: "최고 우대금리",
            data: a2.value,
            borderWidth: 1,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    });
  }
});

const goDepositeDetail = function (fin_prdt_cd) {
  router.push({
    name: "deposite-detail",
    params: { fin_prdt_cd: fin_prdt_cd },
  });
};

const goSavingDetail = function (fin_prdt_cd) {
  router.push({
    name: "saving-detail",
    params: { fin_prdt_cd: fin_prdt_cd },
  });
};
</script>

<style scoped>
.product-container {
  margin-bottom: 20px;
}

.product-category {
  display: flex;
  justify-content: space-between;
}

.product-category > div {
  width: 48%;
}

.interest-rate-container {
  margin-top: 20px;
}

.chart-container {
  width: 600px;
  height: 400px;
  margin-top: 10px;
}

canvas {
  width: 50%;
  height: 400px;
}

p:hover {
  background-color: #f2f2f2; /* Change the background color to your preference */
  cursor: pointer; /* Change the cursor to a pointer to indicate interactivity */
}
</style>
