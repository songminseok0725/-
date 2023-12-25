<!-- views/findPasswordView.vue -->

<template>
  <div class="findPassword-container">
    <h1>비밀번호 찾기</h1>
    <form @submit.prevent="findPassword" class="findPassword-form">
      <label for="username">이름 :</label>
      <input type="text" id="username" v-model.trim="username" />

      <label for="email">이메일 :</label>
      <input type="text" id="email" v-model.trim="email" />

      <button type="submit">찾기</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useCounterStore } from "@/stores/counter";
import { storeToRefs } from "pinia";
import axios from "axios";

const username = ref(null);
const email = ref(null);

const store = useCounterStore();
const findPassword = function () {
  axios({
    method: "post",
    url: "http://127.0.0.1:8000/accounts/findpassword/",
    data: {
      username: username.value,
      email: email.value,
    },
  })
    .then((res) => {
      username.value = "";
      email.value = "";
      if (res.data.msg === "success") {
        alert("이메일로 비밀번호가 전송되었습니다");
      } else {
        alert("해당 유저가 없거나, 해당유저의 이메일과 일치하지 않습니다.");
      }
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style scoped>
.findPassword-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  text-align: center;
}

.findPassword-form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

label {
  font-weight: bold;
}

input {
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  padding: 10px;
  background-color: #009688;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
