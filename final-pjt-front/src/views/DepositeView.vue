<template>
  <div id="d1">
    <div>
      <SearchProductView
        @get-bank-and-range="getBankAndRange"
        @reset-search="resetSearch"
        :bank-list="bankList"
        :range-list="rangeList"
      />
    </div>
    <hr />
    <div>
      <h1>정기 예금</h1>
      <div>
        <vue-good-table
          :columns="columns"
          :rows="rows"
          @row-click="onRowClick"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import SearchProductView from "@/views/SearchProduct.vue";
import { ref, onMounted, watch, computed, onBeforeMount } from "vue";
import { useRouter } from "vue-router";
import { useCounterStore } from "@/stores/counter";
import axios from "axios";
import { setMapStoreSuffix, storeToRefs } from "pinia";

const columns = [
  {
    label: "공시 제출일",
    field: "dcls_month",
  },
  {
    label: "금융 회사명",
    field: "kor_co_nm",
  },
  {
    label: "상품명",
    field: "fin_prdt_nm",
  },
  {
    label: "6개월",
    field: "intr_rate6",
    type: "num",
  },
  {
    label: "12개월",
    field: "intr_rate12",
    type: "num",
  },
  {
    label: "24개월",
    field: "intr_rate24",
    type: "num",
  },
  {
    label: "36개월",
    field: "intr_rate36",
    type: "num",
  },
  {
    label: "fin_prdt_co",
    field: "fin_prdt_co",
    type: "string",
    hidden: true,
  },
];
const rows = ref([]);
const rowsWhole = ref([]);
// const bankList = ref([]);
const bank = ref("");
const rangeList = ref(["6개월", "12개월", "24개월", "36개월"]);
const range = ref("");
const router = useRouter();
const store = useCounterStore();

const getRowsWhole = function () {
  rowsWhole.value = [];
  for (const depo of store.deposites) {
    let tmp = {
      dcls_month: null,
      kor_co_nm: null,
      fin_prdt_nm: null,
      fin_prdt_cd: null,
      intr_rate6: null,
      intr_rate12: null,
      intr_rate24: null,
      intr_rate36: null,
    };
    tmp.dcls_month = depo.dcls_month;
    tmp.kor_co_nm = depo.kor_co_nm;
    tmp.fin_prdt_nm = depo.fin_prdt_nm;
    tmp.fin_prdt_cd = depo.fin_prdt_cd;
    for (const option of depo.deposite_optionlist_set) {
      if (option.save_trm == 6) {
        tmp.intr_rate6 = option.intr_rate || null;
      } else if (option.save_trm == 12) {
        tmp.intr_rate12 = option.intr_rate || null;
      } else if (option.save_trm == 24) {
        tmp.intr_rate24 = option.intr_rate || null;
      } else if (option.save_trm == 36) {
        tmp.intr_rate36 = option.intr_rate || null;
      }
    }
    rowsWhole.value.push(tmp);
  }
  rows.value = [...rowsWhole.value];
};

const { deposites, banks } = storeToRefs(store);
const bankList = computed(() => banks.value);
watch(deposites, (newValue) => {
  getRowsWhole();
});

onMounted(() => {
  getRowsWhole();
});

const doSearch = function () {
  if (bank.value) {
    rows.value = rowsWhole.value.filter(
      (elem1) => elem1.kor_co_nm === bank.value
    );
  }
  if (range.value) {
    rows.value = rows.value.filter((elem2) =>
      range.value === "6개월"
        ? elem2.intr_rate6
        : range.value === "12개월"
        ? elem2.intr_rate12
        : range.value === "24개월"
        ? elem2.intr_rate24
        : range.value === "36개월"
        ? elem2.intr_rate36
        : false
    );
  }
};

const resetSearch = function () {
  rows.value = rowsWhole.value;
  range.value = "";
  bank.value = "";
};

const getBankAndRange = function (bankInput, rangeInput) {
  bank.value = bankInput.value;
  range.value = rangeInput.value;
  doSearch();
};

const onRowClick = function (params) {
  // params.row - row object
  // params.pageIndex - index of this row on the current page.
  // params.selected - if selection is enabled this argument
  // indicates selected or not
  // params.event - click event
  console.log(params.row);
  router.push({
    name: "deposite-detail",
    params: { fin_prdt_cd: params.row.fin_prdt_cd },
  });
};
</script>

<style scoped>
#d1 {
  display: flex;
  flex-direction: row;
  justify-content: left;
}

hr {
  margin: 10px 10px;
}
</style>
