<template>
  <div v-if="comment" class="comment-item">
    <p class="comment-info">
      <span class="info-label">작성자:</span> {{ comment.username }}
    </p>
    <p class="comment-info">
      <span class="info-label">내용:</span> {{ comment.content }}
    </p>
    <p class="comment-info">
      <span class="info-label">작성일:</span> {{ comment.created_at }}
    </p>
    <p class="comment-info">
      <span class="info-label">수정일:</span> {{ comment.updated_at }}
    </p>
  </div>

  <div v-if="checkIsAuthor" class="author-actions">
    <RouterLink :to="{ name: 'PutCommentView', params: { id: comment?.id }, query:{articleId: props.articleId, content: comment.content} }" >
      <button class="edit-button">수정</button>
    </RouterLink>
    <button type="button" @click="deleteComment(comment?.id)" class="delete-button">
      삭제
    </button>
  </div>
  <!-- <div v-else class="not-author">내가 쓴 댓글이 아닙니다</div> -->

  <hr class="divider" />
</template>

<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useCounterStore } from "@/stores/counter";
import { useRoute, useRouter } from "vue-router";

const store = useCounterStore();
const router = useRouter();
// const comment = ref(null);

const props = defineProps({
  comment: Object,
  articleId: Number,
});

const checkIsAuthor = props.comment.username === store.userInfo.username;

const deleteComment = (comment_id) => {
  store.deleteComment(comment_id);
  router.push({name:'CommentList', params:{id:props.articleId}})
};

onMounted(() => {
  console.log(props.articleId)
  // axios({
  //   method: "GET",
  //   url: `${store.API_URL}/api/v1/comments/${route.params.id}/`,
  // })
  //   .then((res) => {
  //     comment.value = res.data;
  //   })
  //   .catch((err) => {
  //     console.log(err);
  //   });
});
</script>

<style scoped>
.comment-item {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 20px;
}

.comment-info {
  margin-bottom: 10px;
  font-size: 16px;
  color: #333;
}

.info-label {
  font-weight: bold;
  margin-right: 8px;
  color: #009688;
}

.author-actions {
  margin-top: 10px;
}

.edit-button,
.delete-button {
  background-color: #009688;
  color: #fff;
  border: none;
  padding: 8px 15px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.edit-button:hover,
.delete-button:hover {
  background-color: #00796b;
}

.not-author {
  color: #777;
  margin-top: 10px;
}

.divider {
  margin-top: 20px;
  border: none;
  border-top: 1px solid #ddd;
}
</style>
