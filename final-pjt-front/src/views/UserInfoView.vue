<template>
  <div v-if="store.userInfo">
    <h3>기본 정보</h3>
    <hr />
    <table>
      <tr>
        <th>username</th>
        <th>email</th>
        <th>nickname</th>
        <th>나이</th>
        <th>현재 가진 금액</th>
        <th>연봉</th>
      </tr>
      <tr>
        <td>{{ store.userInfo.username }}</td>
        <td>{{ store.userInfo.email }}</td>
        <td>{{ store.userInfo.nickname }}</td>
        <td>{{ store.userInfo.age }}</td>
        <td>{{ store.userInfo.money }}</td>
        <td>{{ store.userInfo.salary }}</td>
      </tr>
    </table>
    <div class="update-link-container">
      <RouterLink :to="{ name: 'userinfoupdate' }" class="update-link"
        >회원정보 수정</RouterLink
      >
    </div>
    <hr />
    <div>
      <h3>비밀번호 변경하기</h3>
      <form @submit.prevent="changepassword">
        <label for="password1">새로운 비밀번호</label>
        <input type="password" id="password1" v-model.trim="password1" />
        <label for="password2">새로운 비밀번호 확인</label>
        <input type="password" id="password2" v-model.trim="password2" />
        <input type="submit" value="변경하기" />
      </form>
      <p v-if="msg">{{ msg }}</p>
      <hr />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import { useCounterStore } from "@/stores/counter";
import { useRouter } from "vue-router";
import axios from "axios";
const store = useCounterStore();

onMounted(() => {
  store.getUserInfo();
});

const router = useRouter();
const password1 = ref("");
const password2 = ref("");
const msg = ref("");
const changepassword = function () {
  axios({
    method: "post",
    url: "http://127.0.0.1:8000/accounts/changepassword/",
    headers: {
      Authorization: `Token ${store.token}`,
    },
    data: {
      new_password1: password1.value,
      new_password2: password2.value,
    },
  })
    .then((res) => {
      alert(res.data.msg);
      if (res.data.msg === "비밀번호 변경완료") {
        router.replace({ name: "home" });
      } else {
        msg.value = res.data.msg;
      }
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style scoped>
table {
  display: flex;
  flex-direction: row;
  height: 450px;
}

tr,
td {
  margin: 20px 20px;
  display: flex;
  flex-direction: column;
  min-width: 100px;
  text-align: left;
  font-size: 18px;
}

th,
td {
  height: 30px;
  margin: 20px 0px;
}

.update-link-container {
  margin-top: 10px;
  margin-left: 15px;
  padding: 9px;
  color: #fff;
  background-color: #009688;
  border-radius: 10px;
  display: inline-block;
}

.update-link {
  color: #fff;
  text-decoration: none;
}

h3 {
  font-size: 1.5em;
  margin-bottom: 15px;
}

form {
  max-width: 400px;
  margin: 0 auto;
}

label {
  display: block;
  margin-bottom: 8px;
}

input {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-sizing: border-box;
}

input[type="submit"] {
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 15px;
  cursor: pointer;
}

input[type="submit"]:hover {
  background-color: #45a049;
}

p {
  margin-top: 15px;
  color: #f00;
}

hr {
  border: 0;
  border-top: 1px solid #ddd;
  margin-top: 20px;
}
</style>
