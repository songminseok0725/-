
<template>
  <div class="comment-list-container">
    <h3 class="comment-list-title">댓글목록</h3>

    <CommentListItem
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
      :article-id="parseInt(route.params.id)"
    />
  </div>
</template>

<script setup>
import { useCounterStore } from "@/stores/counter";
import { ref, onMounted, onUpdated } from "vue";
import { useRoute } from "vue-router";

import CommentListItem from "@/components/CommentListItem.vue";
import axios from "axios";

const store = useCounterStore();
const route = useRoute();
const comments = ref(null);

onMounted(() => {
  axios({
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
  })
    .then((res) => {
      comments.value = res.data.comment_set;
    })
    .catch((err) => {
      console.log(err);
    });
});
onUpdated(()=>{
  axios({
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
  })
    .then((res) => {
      comments.value = res.data.comment_set;
    })
    .catch((err) => {
      console.log(err);
    });

})

</script>

<style scoped>
.comment-list-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.comment-list-title {
  font-size: 24px;
  color: #009688;
  margin-bottom: 20px;
}
</style>

