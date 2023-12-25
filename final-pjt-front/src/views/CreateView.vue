

<template>
  <div class="create-article-container">
    <h1 class="create-article-title">게시글을 작성하시오</h1>
    <form @submit.prevent="createArticle" class="create-article-form">
      <div class="form-group">
        <!-- <label for="title" class="form-label">제목:</label> -->
        <input type="text" v-model.trim="title" id="title" class="form-input" placeholder="제목을 입력해주세요"/>
      </div>
      <div class="form-group">
        <!-- <label for="content" class="form-label">내용:</label> -->
        <textarea v-model.trim="content" id="content" class="form-textarea" placeholder="내용을 입력해주세요"></textarea>
      </div>
      <input type="submit" value="작성하기" class="submit-button" />
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { useCounterStore } from "@/stores/counter";
import { useRouter, useRoute } from "vue-router";

const title = ref(null);
const content = ref(null);
const store = useCounterStore();
const router = useRouter();
const route = useRoute();

const createArticle = function () {
  axios({
    method: "POST",
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log("게시글 작성 성공");
      router.push({ name: "ArticleView" });
    })
    .catch((err) => {
      console.error(err);
    });
};
</script>

<style scoped>
.create-article-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.create-article-title {
  font-size: 28px;
  color: #009688;
  margin-bottom: 20px;
}

.create-article-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 20px;
}

.form-label {
  font-size: 16px;
  margin-bottom: 5px;
}

.form-input,
.form-textarea {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 16px;
}

.submit-button {
  background-color: #009688;
  color: #fff;
  padding: 10px;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.submit-button:hover {
  background-color: #00796b;
}
</style>

