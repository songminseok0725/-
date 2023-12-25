

<template>
  <div class="article-item">
    <h5 class="article-id">{{ article.id }}번 게시글</h5>
    <p class="author">작성자 : {{ article.username }}</p>
    <p class="title">제목 : {{ article.title }}</p>
    <p class="content">내용 : {{ article.content }}</p>

    <RouterLink
      :to="{ name: 'DetailView', params: { id: article.id } }"
      class="detail-link link"
    >
      <button class="detail-button">자세히보기</button>
    </RouterLink>

    <RouterLink
      :to="{ name: 'CommentView', params: { id: article.id } }"
      class="comment-link link"
    >
      <button class="made-button">댓글작성</button>
    </RouterLink>

    <RouterLink
      :to="{ name: 'CommentList', params: { id: article.id } }"
      class="comment-link link"
    >
      <button class="list-button">댓글목록</button>
    </RouterLink>

    <div v-if="checkIsAuthor" class="author-actions">
      <RouterLink
        :to="{ name: 'PutView', params: { id: article.id }, query:{title: article.title, content:article.content} }"
        class="edit-link"
      >
        <button class="edit-button">수정</button>
      </RouterLink>
      <button type="button" @click="deleteArticle(article.id)" class="delete-button">
        삭제
      </button>
    </div>
    <!-- <div v-else class="not-author">내가 쓴 글이 아닙니다</div> -->
    <hr class="divider" />
  </div>
</template>

<script setup>
import { RouterLink } from "vue-router";
import { useCounterStore } from "@/stores/counter";
import { computed, onMounted } from "vue";

const store = useCounterStore();

const props = defineProps({
  article: Object,
});

// 이거 주석처리
// defineProps({
//   article: Object,
// });

// const isAuthor = store.isAuthor;  //이거 주석
// const checkIsAuthor = props.article.username == store.userInfo.username;
const checkIsAuthor = props.article.username === store.userInfo.username;

const deleteArticle = (article_id) => {
  store.deleteArticle(article_id);
};
</script>

<style scoped>
.article-item {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 20px;
}

.article-id {
  color: #555;
  font-size: 16px;
  margin-bottom: 5px;
}

.author {
  font-weight: bold;
}

.title,
.content {
  margin-top: 5px;
}

.link {
  color: #3498db;
  text-decoration: none;
  transition: color 0.3s;
}

.link:hover {
  text-decoration: underline;
}

.author-actions {
  margin-top: 10px;
}

.edit-link {
  margin-right: 10px;
}

.detail-link {
  margin-right: 10px;
}
.comment-link {
  margin-right: 10px;
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

.detail-button,
.list-button,
.made-button {
  background-color: #03312d;
  color: #fff;
  border: none;
  padding: 8px 15px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.detail-button:hover,
.list-button:hover,
.made-button:hover {
  background-color: #010e0c;
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

