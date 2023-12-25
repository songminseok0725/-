<template>
  <div class="navnav">
    <nav>
      <RouterLink :to="{ name: 'home' }">
        <img class="img" src="@/assets/seokbank.jpg" alt="logoimg"
      /></RouterLink>

      <RouterLink :to="{ name: 'map' }">은행찾기</RouterLink>

      <RouterLink :to="{ name: 'rate' }">환율조회</RouterLink>

      <RouterLink :to="{ name: 'product', query: { selectInput: '0' } }">
        금융상품</RouterLink
      >
      <RouterLink v-if="store.isLogin" :to="{ name: 'ArticleView' }"
        >커뮤니티</RouterLink
      >
      <hr />
    </nav>
  </div>
  <div class="user-action">
    <RouterLink v-if="!store.isLogin" :to="{ name: 'SignUpView' }">
      회원가입
    </RouterLink>

    <RouterLink v-if="!store.isLogin" :to="{ name: 'LogInView' }">
      로그인</RouterLink
    >

    <RouterLink v-if="store.isLogin" :to="{ name: 'userinfo' }"
      >마이페이지</RouterLink
    >
    <button
      v-if="store.isLogin"
      @click.prevent="store.logOut()"
      class="logout-button"
    >
      로그아웃
    </button>
  </div>

  <RouterView />
</template>

<script setup>
import { useCounterStore } from "@/stores/counter";
import { onMounted, onBeforeUnmount } from "vue";
import { RouterView, RouterLink } from "vue-router";

const store = useCounterStore();

onMounted(() => {
  store.getWholeProduct();
});
</script>

<style scoped>
nav a img.img {
  border-radius: 10px;
  width: 150px;
  height: 40px;
}

.navnav {
  display: flex;
  flex-direction: column;
}

nav {
  padding: 7px;
  text-align: center;
}

nav a {
  margin: 0 15px;
  color: #009688;
  text-decoration: none;
  font-size: 18px;
  position: relative;
}

nav a:hover {
  color: #f0f0f0;
}

nav a::after {
  content: "";
  display: block;
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 0;
  height: 2px;
  background-color: #009688;
  transition: width 0.3s ease-out;
}

nav a:hover::after {
  width: 100%;
  left: 0;
}

.user-action {
  align-self: flex-end;
  position: absolute;
  top: 0;
  right: 0;
  margin: 10px;
  margin-top: 0; /* 추가된 부분 */
}
.user-action RouterLink {
  margin: 0 25px;
}
.user-action button {
  margin: 0 20px;
}

.user-action a {
  color: #009688;
  text-decoration: none;
  font-size: 13px;
  position: relative;
}

.user-action a:hover {
  color: #f0f0f0;
}

.user-action a::after {
  content: "";
  display: block;
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 0;
  height: 2px;
  background-color: #009688;
  transition: width 0.3s ease-out;
}

.user-action a:hover::after {
  width: 100%;
  left: 0;
}

.logout-button {
  margin: 0 5px;
  color: #009688;
  text-decoration: none;
  font-size: 13px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
}
.logout-button:hover {
  color: #f0f0f0;
}

.logout-button a::after {
  content: "";
  display: block;
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 0;
  height: 2px;
  background-color: #009688;
  transition: width 0.3s ease-out;
}
</style>
