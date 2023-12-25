<template>
  <div class="exchange-rate-calculator">
    <h1>환율 계산기</h1>
    <select v-model="select1" class="select-box">
      <option disabled value="null" selected>국가를 선택하세요</option>
      <option v-for="payment in payments" :key="payment" :value="payment">
        {{ payment }}
      </option>
      <br />
    </select>
    <p v-if="select1" class="input-group">
      <input type="text" v-model="price2" @input="price2Input" />
      <span>{{ info.CUR_UNIT }}</span>
    </p>
    <div v-if="select1" class="input-group">
      <input type="text" v-model="price1" @input="price1Input" />
      <span>KRW</span>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from "vue";
import axios from "axios";
// prettier-ignore
const payments = ref(
  ["미국", "유럽", "일본", "영국","스위스","캐나다","호주","중국","홍콩","스웨덴","뉴질랜드","싱가포르","노르웨이","아랍에미리트","바레인","브루나이","인도네시아","말레이시아","사우디","태국","쿠웨이트"]
);

// prettier-ignore
const countries = { 미국:"USD", 유럽: "EUR", 일본: "JPY(100)", 영국: "GBP", 스위스: "CHF", 캐나다:"CAD", 호주:"AUD", 중국:"CNH", 홍콩:"HKD", 스웨덴:"SEK", 뉴질랜드:"NZD", 싱가포르:"SGD", 노르웨이:"NOK", 아랍에미리트:"AED", 바레인:"BHD", 브루나이:"BND", 인도네시아:"IDR(100)", 말레이시아:"MYR", 사우디:"SAR", 태국:"THB", 쿠웨이트:"KWD" };

// console.log(countries.유럽);

const select1 = ref(null);

const price2 = ref(0);
const price1 = ref(0);

const info = ref({});

const DEAL_BAS_R = ref(0);

watch(select1, (newValue) => {
  axios({
    method: "post",
    url: "http://127.0.0.1:8000/rates/",
    data: {
      cur_unit: countries[newValue],
    },
  })
    .then((res) => {
      console.log(res);
      info.value = res.data;
      DEAL_BAS_R.value = parseFloat(res.data.DEAL_BAS_R.replace(",", ""));
      console.log(DEAL_BAS_R.value);
      price2.value = 1;
      price1.value = price2.value * DEAL_BAS_R.value;
    })
    .catch((err) => {
      console.log(err);
    });
});

const price2Input = function () {
  price1.value = price2.value * DEAL_BAS_R.value;
};
const price1Input = function () {
  price2.value = price1.value / DEAL_BAS_R.value;
};

onMounted(() => {
  axios({
    method: "get",
    url: "http://127.0.0.1:8000/rates/update/",
  })
    .then((res) => {
      console.log(res);
    })
    .catch((err) => {
      console.log(err);
    });
});
</script>

<style scoped>
.exchange-rate-calculator {
  max-width: 400px;
  margin: 20px auto;
  text-align: center;
}
h1 {
  color: #009688;
}
.select-box {
  margin: 10px;
  padding: 8px;
  font-size: 16px;
  border: 1px solid #009688;
  border-radius: 4px;
  color: #009688;
}
.input-group {
  margin: 10px 0;
  display: flex;
  align-items: center;
}
input {
  flex: 1;
  padding: 8px;
  font-size: 16px;
  border: 1px solid #009688;
  border-radius: 4px;
}
span {
  margin-left: 8px;
  color: #009688;
  font-size: 16px;
}
</style>
