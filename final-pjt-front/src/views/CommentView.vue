

<template>
  <div class="comment-create-container">
    <h1 class="comment-create-title">댓글을 작성하시오</h1>
    <form @submit.prevent="createComment" class="comment-form">
  <div>
    <!-- <label for="content" class="form-label">내용:</label> -->
    <div class="textarea-container">
    <textarea v-model.trim="content" id="content" class="form-textarea" placeholder="내용을 입력해주세요"></textarea>
  </div>
</div>
      <input type="submit" value="작성하기" class="submit-button" />
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useCounterStore } from "@/stores/counter";
import { useRouter, useRoute } from "vue-router";

const content = ref(null);
const store = useCounterStore();
const router = useRouter();
const route = useRoute();
const articleid = route.params.id;
// const articleId = ref(null);

const createComment = function () {
  axios({
    method: "POST",
    url: `${store.API_URL}/api/v1/articles/${articleid}/comments/`,
    data: {
      content: content.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log("댓글 작성 성공");
      router.push({ name: "ArticleView" });
    })
    .catch((err) => {
      console.error(err);
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

.textarea-container {
  position: relative;
}

.comment-form {
  display: flex;
  flex-direction: column;
}

.form-label {
  margin-bottom: 5px;
  font-size: 16px;
}

.form-label::before {
  content: "내용:";
  display: block;
  position: absolute;
  top: 12px;
  left: 10px;
  color: #777; /* Adjust the color as needed */
  font-size: 16px;
  pointer-events: none; /* Ensure the label doesn't interfere with textarea interaction */
}

.form-input,
.form-textarea {
  padding: 10px;
  margin-bottom: 15px;
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

