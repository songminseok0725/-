<template>
  <div class="search-container">
    <h1 class="title-ment">가까운 은행을 찾아보세요</h1>
    <select v-model="sido" class="select-box">
      <option disabled value="" selected>도/시</option>
      <option v-for="info in searchList" :key="info.id">{{ info.prov }}</option>
    </select>
    <select v-model="sigungoo" :disabled="!sido" class="select-box">
      <option disabled value="">시/군/구</option>
      <option v-for="c in candidateSigungoo" :key="c">{{ c }}</option>
    </select>
    <select v-model="bank" :disabled="!sigungoo" class="select-box">
      <option disabled value="">은행명</option>
      <option v-for="b in bankList" :key="b">{{ b }}</option>
    </select>
    <button :disabled="!(sido && sigungoo && bank)" @click="updateMap">
      검색
    </button>
    <div id="map" class="map-container"></div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch, computed } from "vue";
var map = null;
var ps = null;
var infowindow;
var markers = [];

const loadScript = () => {
  const key = "6e0539f78c5b7a9f15f78b2ea8c086cb";
  const script = document.createElement("script");
  script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${key}&libraries=services&autoload=false`;
  script.addEventListener("load", () => kakao.maps.load(initMap));
  document.head.appendChild(script);
};

const initMap = () => {
  infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });
  const mapContainer = document.querySelector("#map");
  const mapOption = {
    center: new kakao.maps.LatLng(33.450701, 126.570667),
    level: 3,
  };
  map = new kakao.maps.Map(mapContainer, mapOption);
  ps = new kakao.maps.services.Places();
};

const updateMap = () => {
  clearMarkers();

  const searchWord = `${sido.value} ${sigungoo.value} ${bank.value}`;
  ps.keywordSearch(searchWord, placesSearchCB);
};

// const clearMarkers = () => {
//   markers.forEach(marker => marker.setMap(null));
//   markers = [];
// };

function placesSearchCB(data, status, pagination) {
  if (status === kakao.maps.services.Status.OK) {
    var bounds = new kakao.maps.LatLngBounds();

    for (var i = 0; i < data.length; i++) {
      displayMarker(data[i]);
      bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
    }

    map.setBounds(bounds);
  }
}

function displayMarker(place) {
  var marker = new kakao.maps.Marker({
    map: map,
    position: new kakao.maps.LatLng(place.y, place.x),
  });

  markers.push(marker);

  kakao.maps.event.addListener(marker, "click", function () {
    infowindow.setContent(
      '<div style="padding:5px;font-size:12px;">' + place.place_name + "</div>"
    );
    infowindow.open(map, marker);
  });
}

const clearMarkers = () => {
  markers.forEach((marker) => marker.setMap(null));
  markers = [];
  infowindow.close(); // infowindow 닫기
};

onMounted(() => {
  loadScript();
});

const searchList = [
  {
    id: 1,
    prov: "서울특별시",
    city: [
      "종로구",
      "중구",
      "용산구",
      "성동구",
      "광진구",
      "동대문구",
      "중랑구",
      "성북구",
      "강북구",
      "도봉구",
      "노원구",
      "은평구",
      "서대문구",
      "마포구",
      "양천구",
      "강서구",
      "구로구",
      "금천구",
      "영등포구",
      "동작구",
      "관악구",
      "서초구",
      "강남구",
      "송파구",
      "강동구",
    ],
  },
  {
    id: 2,
    prov: "부산광역시",
    city: [
      "중구",
      "서구",
      "동구",
      "영도구",
      "부산진구",
      "동래구",
      "남구",
      "북구",
      "해운대구",
      "사하구",
      "금정구",
      "강서구",
      "연제구",
      "수영구",
      "사상구",
      "기장군",
    ],
  },
  {
    id: 3,
    prov: "대구광역시",
    city: [
      "중구",
      "동구",
      "서구",
      "남구",
      "북구",
      "수성구",
      "달서구",
      "달성군",
      "군위군",
    ],
  },
  {
    id: 4,
    prov: "인천광역시",
    city: [
      "중구",
      "동구",
      "미추홀구",
      "연수구",
      "남동구",
      "부평구",
      "계양구",
      "서구",
      "강화군",
      "옹진군",
    ],
  },
  {
    id: 5,
    prov: "광주광역시",
    city: ["동구", "서구", "남구", "북구", "광산구"],
  },
  {
    id: 6,
    prov: "대전광역시",
    city: ["동구", "중구", "서구", "유성구", "대덕구"],
  },
  {
    id: 7,
    prov: "울산광역시",
    city: ["중구", "남구", "동구", "북구", "울주군"],
  },
  {
    id: 8,
    prov: "세종특별자치시",
    city: [],
  },
  {
    id: 9,
    prov: "경기도",
    city: [
      "수원시",
      "고양시",
      "용인시",
      "성남시",
      "부천시",
      "화성시",
      "안산시",
      "남양주시",
      "안양시",
      "평택시",
      "시흥시",
      "파주시",
      "의정부시",
      "김포시",
      "광주시",
      "광명시",
      "군포시",
      "하남시",
      "오산시",
      "양주시",
      "이천시",
      "구리시",
      "안성시",
      "포천시",
      "의왕시",
      "양평군",
      "여주시",
      "동두천시",
      "가평군",
      "과천시",
      "연천군",
    ],
  },
  {
    id: 10,
    prov: "강원특별자치도",
    city: [
      "춘천시",
      "원주시",
      "강릉시",
      "동해시",
      "태백시",
      "속초시",
      "삼척시",
      "홍천군",
      "횡성군",
      "영월군",
      "평창군",
      "정선군",
      "철원군",
      "화천군",
      "양구군",
      "인제군",
      "고성군",
      "양양군",
    ],
  },
  {
    id: 11,
    prov: "충청북도",
    city: [
      "청주시",
      "충주시",
      "제천시",
      "보은군",
      "옥천군",
      "영동군",
      "증평군",
      "진천군",
      "괴산군",
      "음성군",
      "단양군",
    ],
  },
  {
    id: 12,
    prov: "충청남도",
    city: [
      "천안시",
      "공주시",
      "보령시",
      "아산시",
      "서산시",
      "논산시",
      "계룡시",
      "당진시",
      "금산군",
      "부여군",
      "서천군",
      "청양군",
      "홍성군",
      "예산군",
      "태안군",
    ],
  },
  {
    id: 13,
    prov: "전라북도",
    city: [
      "목포시",
      "여수시",
      "순천시",
      "나주시",
      "광양시",
      "담양군",
      "곡성군",
      "구례군",
      "고흥군",
      "보성군",
      "화순군",
      "장흥군",
      "강진군",
      "해남군",
      "영암군",
      "무안군",
      "함평군",
      "영광군",
      "장성군",
      "완도군",
      "진도군",
      "신안군",
    ],
  },
  {
    id: 14,
    prov: "경상북도",
    city: [
      "포항시",
      "경주시",
      "김천시",
      "안동시",
      "구미시",
      "영주시",
      "영천시",
      "상주시",
      "문경시",
      "경산시",
      "의성군",
      "청송군",
      "영양군",
      "영덕군",
      "청도군",
      "고령군",
      "성주군",
      "칠곡군",
      "예천군",
      "봉화군",
      "울진군",
      "울릉군",
    ],
  },
  {
    id: 15,
    prov: "경상남도",
    city: [
      "창원시",
      "진주시",
      "통영시",
      "사천시",
      "김해시",
      "밀양시",
      "거제시",
      "양산시",
      "의령군",
      "함안군",
      "창녕군",
      "고성군",
      "남해군",
      "하동군",
      "산청군",
      "함양군",
      "거창군",
      "합천군",
    ],
  },
  {
    id: 16,
    prov: "제주특별자치도",
    city: ["제주시", "서귀포시"],
  },
];
const bankList = [
  "국민은행",
  "우리은행",
  "하나은행",
  "기업은행",
  "신한은행",
  "농협은행",
  "수협은행",
  "SC제일은행",
  "KDB산업은행",
  "한국씨티은행",
  "한국수출입은행",
  "대구은행",
  "부산은행",
  "광주은행",
  "제주은행",
  "전북은행",
  "경남은행",
];

const sido = ref("");
watch(sido, (newValue) => {
  console.log(newValue);
});

const candidateSigungoo = computed(() => {
  const tmp = searchList.find((elem) => {
    return elem.prov === sido.value;
  });
  return tmp ? tmp.city : [];
});
const sigungoo = ref("");
watch(sigungoo, (newValue) => {
  console.log(newValue);
});

const bank = ref("");
watch(bank, (newValue) => {
  console.log(newValue);
});
</script>

<style scoped>
/* .search-container {
  max-width: 600px;
  margin: 20px auto;
  text-align: center;
} */

.title-ment {
  color: #009688;
}

.search-container {
  max-width: 1200px; /* 페이지의 최대 폭을 설정합니다 */
  margin: 0 auto; /* 가운데 정렬을 위해 margin을 auto로 설정합니다 */
  padding: 20px; /* 내부 여백을 추가합니다 */
}

.select-box {
  margin: 10px;
  padding: 8px;
  font-size: 16px;
  border: 1px solid #009688;
  border-radius: 4px;
  color: #009688;
}

.search-button {
  background-color: #009688;
  color: #fff;
  border: none;
  padding: 10px 20px;
  font-size: 18px;
  cursor: pointer;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.search-button:hover {
  background-color: #00796b;
}

/* .map-container {
  width: 100%;
  height: 350px;
  margin-top: 20px;
  border: 1px solid #009688;
  border-radius: 4px;
} */
.map-container {
  width: 100%;
  height: 500px; /* 기본 높이를 설정합니다 */
  max-width: 300%; /* 최대 너비를 설정하여 기본 높이를 유지하면서 확장됩니다 */
}
</style>
