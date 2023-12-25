<template>
  <div>
    <p>
      <RouterLink :to="{ name: 'product', query: { selectInput: '0' } }">
        정기 예금 조회
      </RouterLink>
      |
      <RouterLink :to="{ name: 'product', query: { selectInput: '1' } }">
        정기 적금 조회
      </RouterLink>
    </p>
    <div id="hb">
      <h1>정기적금 상세</h1>
      <div v-if="store.token">
        <button
          v-if="
            !store.userInfo.financial_products.includes(
              route.params.fin_prdt_cd
            )
          "
          @click="joinDeposite"
        >
          가입하기
        </button>
        <p v-else class="message">가입한 상태입니다.</p>
      </div>
      <div v-else>
        <p>가입하려면 로그인이 필요합니다.</p>
      </div>
    </div>
    <table v-if="data">
      <tr>
        <th>공시 제출월</th>
        <th>금융회사명</th>
        <th>상품명</th>
        <th>가입제한</th>
        <th>가입 방법</th>
        <th>우대조건</th>
      </tr>
      <tr>
        <td>{{ data[0].dcls_month }}</td>
        <td>{{ data[0].kor_co_nm }}</td>
        <td>{{ data[0].fin_prdt_nm }}</td>
        <td>{{ data[0].join_deny }}</td>
        <td>{{ data[0].join_way }}</td>
        <td>{{ data[0].spcl_cnd }}</td>
      </tr>
    </table>
    <h2>옵션</h2>
    <div v-if="data" id="options">
      <div v-for="option in data[0].saving_optionlist_set">
        <p>이자 지급 방식: {{ option.intr_rate_type_nm }}</p>
        <p>저축 금리: {{ option.intr_rate }} %</p>
        <p>최고 우대 금리: {{ option.intr_rate2 }} %</p>
        <p>저축 기간: {{ option.save_trm }}개월</p>
        <hr />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";
import { useCounterStore } from "@/stores/counter";

const store = useCounterStore();
const route = useRoute();
const data = ref(null);
const select = ref(2);
onMounted(() => {
  axios({
    method: "get",
    url: `http://127.0.0.1:8000/products/saving/${route.params.fin_prdt_cd}/`,
  })
    .then((res) => {
      data.value = res.data;
      console.log(data.value);
    })
    .catch((err) => console.log(err));
});

const joinDeposite = function () {
  console.log(data.value[0].fin_prdt_cd);
  console.log(store.token);
  axios({
    method: "post",
    url: "http://127.0.0.1:8000/products/userproduct/",
    headers: {
      Authorization: `Token ${store.token}`,
    },
    data: {
      financial_products: data.value[0].fin_prdt_cd,
    },
  })
    .then((res) => {
      console.log(res.data);
      store.getUserInfo();
    })
    .catch((err) => console.log(err));
};
</script>


<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  background-color: #fff;
  border-radius: 8px;
}

th,
td {
  padding: 15px;
  border: 1px solid #ddd;
  text-align: left;
}

th {
  background-color: #f2f2f2;
}

p > * {
  text-decoration: none;
  color: black;
}

#hb {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  padding: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  background-color: #fff;
  border-radius: 8px;
}

button {
  padding: 10px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

hr {
  margin: 20px 0;
  border: 0;
  border-top: 1px solid #ccc;
}

#hb h1 {
  margin: 0;
}

#hb div {
  display: flex;
  align-items: center;
}

#hb button {
  margin-left: 10px;
}

h2 {
  margin-top: 20px;
  padding: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  background-color: #f8f8f8;
  border-radius: 8px;
}

#options {
  margin-top: 20px;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  background-color: #f8f8f8;
  border-radius: 8px;
}

#options p {
  margin: 10px 0;
}

#options hr {
  border: 0;
  border-top: 1px solid #ccc;
  margin: 15px 0;
}

p > a {
  text-decoration: none;
  color: black; 
  background-color: #88ebda; 
  padding: 5px 10px; 
  border-radius: 5px; 
  transition: background-color 0.3s ease; 
}

p > a:hover {
  background-color: #45a049; 
  color: white; 
}
p.message {
  background-color: #4CAF50; 
  color: white; 
  padding: 10px; 
  border-radius: 5px; 
}
</style>
