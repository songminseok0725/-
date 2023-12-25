

<template>
  <div v-if="store.userInfo" class="profile-page">
    <h1>{{ store.userInfo.username }}님의 프로필 페이지</h1>
    <div id="profile-container">
      <div id="nav">
        <p :class="{ active: select === 0 }" @click="select = 0">기본 정보 수정</p>
        <p :class="{ active: select === 1 }" @click="select = 1">가입한 상품</p>
        <p :class="{ active: select === 2 }" @click="select = 2">상품 추천 받기</p>
      </div>
      <div id="content-container">
        <UserInfoView id="v1" v-if="select === 0" />
        <joinProductView v-if="select === 1" />
        <recommendProductView v-if="select === 2" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, computed, ref } from "vue";
import { useCounterStore } from "@/stores/counter";
import UserInfoView from "@/views/UserInfoView.vue";
import recommendProductView from "@/views/recommendProductView.vue";
import joinProductView from "@/views/joinProductView.vue";

const select = ref(0);
const store = useCounterStore();
</script>

<style scoped>
#profile-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

#nav {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
}

#nav p {
  cursor: pointer;
  padding: 10px;
  border-radius: 8px;
  transition: background-color 0.3s;
}

#nav p.active {
  background-color: #009688;
  color: #fff;
}

#content-container {
  width: 100%;
}



.profile-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

/* Additional styling for the h1 element */
h1 {
  font-size: 24px;
  color: #009688;
  margin-bottom: 20px;
}

#nav {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
}

#nav p {
  cursor: pointer;
  padding: 10px;
  border-radius: 8px;
  transition: background-color 0.3s;
}

#nav p.active {
  background-color: #009688;
  color: #fff;
}

#content-container {
  width: 100%;
}
</style>
