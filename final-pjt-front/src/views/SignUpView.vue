<!-- views/SignUpView.vue -->

<template>
  <div class="signup-container">
    <h1>회원가입</h1>
    <form @submit.prevent="signUp" class="signup-form">
      <label for="username">이름:</label>
      <input type="text" id="username" v-model.trim="username" />

      <label for="password1">비밀번호:</label>
      <input type="password" id="password1" v-model.trim="password1" />

      <label for="password2">비밀번호 확인:</label>
      <input type="password" id="password2" v-model.trim="password2" />

      <button type="submit">가입</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useCounterStore } from "@/stores/counter";

const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);

const store = useCounterStore();

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  };
  store.signUp(payload);
};
</script>

<style scoped>
.signup-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  text-align: center;
}

.signup-form {
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
