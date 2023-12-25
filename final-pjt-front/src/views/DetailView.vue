

<template>
  <div class="detail-container">
    <h1 class="detail-title">게시글 상세 정보</h1>
    <div v-if="article" class="article-details">
      <p class="detail-info">
        <span class="info-label">작성자:</span> {{ article.username }}
      </p>
      <p class="detail-info">
        <span class="info-label">제목:</span> {{ article.title }}
      </p>
      <p class="detail-info">
        <span class="info-label">내용:</span> {{ article.content }}
      </p>
      <p class="detail-info">
        <span class="info-label">작성일:</span> {{ article.created_at }}
      </p>
      <p class="detail-info">
        <span class="info-label">수정일:</span> {{ article.updated_at }}
      </p>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useCounterStore } from "@/stores/counter";
import { useRoute } from "vue-router";
import { RouterLink } from "vue-router";

const store = useCounterStore();
const route = useRoute();
const article = ref(null);

onMounted(() => {
  axios({
    method: "GET",
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
  })
    .then((res) => {
      // console.log(res.data)
      article.value = res.data;
      // arr.value = article.value.financial_products;
    })
    .catch((err) => {
      console.error(err);
    });
});
</script>

<style scoped>
.detail-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.detail-title {
  font-size: 28px;
  color: #009688;
  margin-bottom: 20px;
}

.article-details {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 15px;
}

.detail-info {
  margin-bottom: 10px;
  font-size: 16px;
  color: #333;
}

.info-label {
  font-weight: bold;
  margin-right: 8px;
  color: #009688;
}
</style>
