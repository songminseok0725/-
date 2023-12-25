<template>
  <div id="user-info">
    <h3>회원정보 수정하기</h3>
    <form @submit.prevent="updateUserInfo" class="user-info-form">
      <!-- <div class="form-group">
        <label for="username">Username: </label>
        <input type="text" id="username" class="input-field" v-model="nowUsername" />
      </div> -->

      <div class="form-group">
        <label for="email">Email: </label>
        <input type="text" id="email" class="input-field" v-model="nowEmail" />
      </div>

      <div class="form-group">
        <label for="nickname">Nickname: </label>
        <input
          type="text"
          id="nickname"
          class="input-field"
          v-model="nowNickname"
        />
      </div>

      <div class="form-group">
        <label for="age">나이: </label>
        <input type="text" id="age" class="input-field" v-model="nowAge" />
      </div>

      <div class="form-group">
        <label for="money">현재 가진 금액: </label>
        <input type="text" id="money" class="input-field" v-model="nowMoney" />
      </div>

      <div class="form-group">
        <label for="salary">연봉: </label>
        <input
          type="text"
          id="salary"
          class="input-field"
          v-model="nowSalary"
        />
      </div>

      <div class="form-actions">
        <button class="submit-button" type="submit">수정</button>
        <button
          class="cancel-button"
          @click.prevent="router.replace({ name: 'userinfo' })"
        >
          수정 취소
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useCounterStore } from "@/stores/counter";
import { useRouter } from "vue-router";

const router = useRouter();
const store = useCounterStore();

const nowUsername = ref("");
const nowEmail = ref("");
const nowNickname = ref("");
const nowAge = ref("");
const nowMoney = ref("");
const nowSalary = ref("");

onMounted(() => {
  nowUsername.value = store.userInfo.username;
  nowEmail.value = store.userInfo.email;
  nowNickname.value = store.userInfo.nickname;
  nowAge.value = store.userInfo.age;
  nowMoney.value = store.userInfo.money;
  nowSalary.value = store.userInfo.salary;
});

const updateUserInfo = function () {
  const payLoad = {
    username: nowUsername.value,
    nickname: nowNickname.value,
    email: nowEmail.value,
    age: nowAge.value,
    money: nowMoney.value,
    salary: nowSalary.value,
  };
  store.updateUserInfo(payLoad);
  router.replace({ name: "userinfo" });
};
</script>

<style scoped>
#user-info {
  max-width: 400px;
  margin: 0 auto;
}

.user-info-form {
  display: flex;
  flex-direction: column;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  margin-bottom: 5px;
  font-weight: bold;
}

.input-field {
  padding: 8px;
  font-size: 14px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.form-actions {
  margin-top: 20px;
  display: flex;
  justify-content: space-between;
}

.submit-button,
.cancel-button {
  padding: 10px 15px;
  cursor: pointer;
  border: none;
  border-radius: 4px;
  color: #fff;
  font-weight: bold;
}

.submit-button {
  background-color: #009688;
}

.cancel-button {
  background-color: #777;
}
</style>
