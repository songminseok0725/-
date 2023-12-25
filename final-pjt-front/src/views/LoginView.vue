<!-- views/LoginView.vue -->

<template>
  <div class="login-container">
    <h1>로그인</h1>
    <form @submit.prevent="logIn" class="login-form">
      <label for="username">이름 :</label>
      <input type="text" id="username" v-model.trim="username" />

      <label for="password">비밀번호 :</label>
      <input type="password" id="password" v-model.trim="password" />

      <button type="submit">로그인</button>
    </form>
  </div>
  <PasswordFindView />
</template>

<script setup>
import PasswordFindView from "@/views/PasswordFindView.vue";
import { ref } from "vue";
import { useCounterStore } from "@/stores/counter";
import { storeToRefs } from "pinia";

const username = ref(null);
const password = ref(null);

const store = useCounterStore();
const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.logIn(payload);
  username.value = "";
  password.value = "";
};
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  text-align: center;
}

.login-form {
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
