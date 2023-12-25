<!-- <template>
  <div>
    <h1>게시글 수정</h1>
    <form @submit.prevent="putArticle">
      <div>
        <label for="title">제목:</label>
        <input type="text" v-model.trim="title" id="title" />
      </div>
      <div>
        <label for="content">내용:</label>
        <textarea v-model.trim="content" id="content"></textarea>
      </div>
      <button type="submit">수정</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useCounterStore } from "@/stores/counter";
import { useRouter, useRoute } from "vue-router";

const title = ref(null);
const content = ref(null);
const store = useCounterStore();
const router = useRouter();
const route = useRoute();
const articleId = route.params.id;
const API_URL = store.API_URL;

const putArticle = function () {
  console.log("버튼 눌림");
  axios({
    method: "PUT",
    url: `${API_URL}/api/v1/articles/${articleId}/`,
    data: {
      title: title.value,
      content: content.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log("create 성공");
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style scoped></style> -->

<template>
  <div class="comment-create-container">
    <h1 class="comment-create-title">게시글 수정</h1>
    <form @submit.prevent="putArticle" class="article-form">
      <div class="form-group">
        <!-- <label for="title">제목:</label> -->
        <input
          type="text"
          v-model.trim="title"
          id="title"
          class="form-input"
          placeholder="수정제목을 입력해주세요"
        />
      </div>
      <div class="form-group">
        <!-- <label for="content">내용:</label> -->
        <textarea
          v-model.trim="content"
          id="content"
          class="form-textarea"
          placeholder="수정 내용을 입력해주세요"
        ></textarea>
      </div>
      <button type="submit" class="submit-button">수정</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useCounterStore } from "@/stores/counter";
import { useRouter, useRoute } from "vue-router";


const store = useCounterStore();
const router = useRouter();
const route = useRoute();
const title = ref(route.query.title);
const content = ref(route.query.content);
const articleId = route.params.id;
const API_URL = store.API_URL;

const putArticle = function () {
  console.log("버튼 눌림");
  axios({
    method: "PUT",
    url: `${API_URL}/api/v1/articles/${articleId}/`,
    data: {
      title: title.value,
      content: content.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log("create 성공");
      router.replace({name: 'ArticleView'})
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style scoped>
.comment-create-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.comment-create-title {
  font-size: 28px;
  color: #009688;
  margin-bottom: 20px;
}

.article-form {
  max-width: 400px;
  margin: 0 auto;
}

/* .form-group {
  margin-bottom: 20px;
} */

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-input,
.form-textarea {
  width: 100%;
  padding: 10px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.form-textarea {
  height: 150px;
}

.submit-button {
  background-color: #009688;
  color: #fff;
  padding: 10px 20px;
  font-size: 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #084943;
}
</style>
