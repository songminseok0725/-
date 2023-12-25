

<template>
  <div class="community-container">
    <h1 class="community-title">커뮤니티</h1>
    <RouterLink :to="{ name: 'CreateView' }" class="create-link">게시글 작성하기</RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
import { onMounted, onUpdated } from "vue";
import { useCounterStore } from "@/stores/counter";
import { RouterLink } from "vue-router";
import ArticleList from "@/components/ArticleList.vue";

const store = useCounterStore();

onMounted(() => {
  store.getArticles();
});

onUpdated(() => {
  store.getArticles();
});
</script>

<style scoped>
.community-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.community-title {
  font-size: 32px;
  color: #009688;
  margin-bottom: 20px;
}

.create-link {
  background-color: #009688;
  color: #fff;
  padding: 6px 15px;
  text-decoration: none;
  border-radius: 10px;
  font-size: 13px;
  transition: background-color 0.3s;
  /* margin-bottom: 20px; */
}

.create-link:hover {
  background-color: #00796b;
}
</style>

