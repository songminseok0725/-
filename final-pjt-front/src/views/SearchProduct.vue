<template>
  <div id="d2">
    <h1>검색하기</h1>
    <p>검색 조건을 입력하세요</p>
    <button @click="resetSearch()">검색 조건 초기화</button>
    <hr />
    <form @submit.prevent="getBankAndRange()" class="search-form">
      <label>은행을 선택하세요</label>
      <select v-model="bankInput" class="select-box">
        <option value="">전체은행</option>
        <option v-for="b in bankList" :key="b.id">
          {{ b.kor_co_nm }}
        </option>
      </select>
      <label>예치기간</label>
      <select v-model="rangeInput" class="select-box">
        <option value="">전체기간</option>
        <option v-for="r in rangeList" :key="r.id">
          {{ r }}
        </option>
      </select>
      <input type="submit" value="검색" class="search-button" />
    </form>
  </div>
</template>

<script setup>
  import {ref} from "vue"
  const bankInput = ref("")
  const rangeInput = ref("")
  defineProps({
    bankList: Array,
    rangeList: Array,
  })
  const emit = defineEmits([
    "getBankAndRange",
    "resetSearch",
  ])
  const getBankAndRange = function(){
    emit("getBankAndRange", bankInput, rangeInput)
  }
  const resetSearch = function(){
    bankInput.value = ""
    rangeInput.value = ""
    emit("resetSearch")
  }


</script>

<style scoped>
#d2 {
  width: 300px;
  margin: 20px auto;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
  color: #333;
}

p {
  color: #555;
}

button {
  margin: 10px 0;
  padding: 8px;
  background-color: #777;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.search-form {
  display: flex;
  flex-direction: column;
}

label {
  margin-bottom: 5px;
  color: #333;
}

.select-box,
input {
  margin: 5px 0;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.search-button {
  padding: 10px;
  background-color: #009688;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>