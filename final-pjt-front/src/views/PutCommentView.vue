<template>
  <div class="comment-create-container">
    <h1 class="comment-create-title">댓글 수정</h1>
    <form @submit.prevent="putComment" class="comment-form">
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

// const title = ref(null);
const store = useCounterStore();
const router = useRouter();
const route = useRoute();
const content = ref(route.query.content);
const commentId = route.params.id;
const API_URL = store.API_URL;

const putComment = function () {
  console.log("버튼 눌림");
  axios({
    method: "PUT",
    url: `${API_URL}/api/v1/comments/${commentId}/`,
    data: {
      // title: title.value,
      content: content.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log("create 성공");
      router.replace({name: 'CommentList',params:{id: route.query.articleId}})
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

.comment-form {
  max-width: 400px;
  margin: 0 auto;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-textarea {
  width: 100%;
  height: 150px;
  padding: 10px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 4px;
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
