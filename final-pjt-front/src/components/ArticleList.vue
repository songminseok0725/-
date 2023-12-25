

<template>
  <div class="article-list">
    <h3 class="list-title">게시글</h3>
    <div class="article-container">
      <ArticleListItem
        v-for="article in store.articles"
        :key="article.id"
        :article="article"
      />
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from "@/stores/counter";
import ArticleListItem from "@/components/ArticleListItem.vue";
import { onMounted } from "vue";

const store = useCounterStore();

onMounted(() => {
  store.getArticles();
});
console.log(store.articles);
</script>

<style scoped>
.article-list {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.list-title {
  color: #333;
  font-size: 24px;
  margin-bottom: 20px;
}

.article-container {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
}

/* Optional: Add a subtle hover effect on the articles */
.article-container:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

</style>


