import { ref, computed, watch, onMounted } from "vue";
import axios from "axios";
import { defineStore } from "pinia";
import router from "../router";
import { useRouter } from "vue-router"; // 민석

export const useCounterStore = defineStore(
  "counter",
  () => {
    const router = useRouter(); // 민석
    const articles = ref([]); // 민석
    // const article = ref([]); // 이거 주석 처리
    const article = ref(null); // 이거 추가
    const comments = ref([]); // 민석
    const comment = ref([]); // 댓글 삭제 위해 이거 추가함.
    const API_URL = "http://127.0.0.1:8000";
    const content = ref(null);

    // 민석 // DRF에 article 조회 요청을 보내는 action
    const getArticles = function () {
      axios({
        method: "GET",
        url: `${API_URL}/api/v1/articles/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          // console.log(res)
          articles.value = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    };

    // // 민석 // DRF에 comments 조회 요청을 보내는 action
    // const getComments = function () {
    //   axios({
    //     method: "GET",
    //     url: `${API_URL}/api/v1/comments/`,
    //     headers: {
    //       Authorization: `Token ${token.value}`,
    //     },
    //   })
    //     .then((res) => {
    //       // console.log(res)
    //       comments.value = res.data;
    //     })
    //     .catch((err) => {
    //       console.log(err);
    //     });
    // };

    // 댓글 구현
    const createComment = function () {
      const articleId = article.value.id; // 수정: 현재 선택된 게시글의 ID 사용
      axios({
        method: "POST",
        url: `${API_URL}/api/v1/articles/${articleId}/comments/`,
        data: {
          content: content.value, //  content 변수 사용
        },
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          console.log("create 성공");
          // router.push({ name: 'ArticleView' })
        })
        .catch((err) => {
          console.log(err);
        });
    };
    const updatedProduct = ref(0);
    const userDeposites = ref([]);
    const userSavings = ref([]);
    const banks = ref([]);
    const deposites = ref([]);
    const savings = ref([]);
    const recommendDeposites = ref([]);
    const recommendSavings = ref([]);

    const signUp = function (payload) {
      const username = payload.username;
      const password1 = payload.password1;
      const password2 = payload.password2;
      axios({
        method: "post",
        url: `${API_URL}/accounts/registration/`,
        data: {
          username,
          password1,
          password2,
        },
      })
        .then((res) => {
          const password = password1;
          logIn({ username, password });
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const token = ref(null);
    const isLogin = computed(() => {
      console.log(token.value);
      return token.value !== null;
    });

    watch(isLogin, (newValue, oldValue) => {
      if (!newValue) {
        logOut();
      }
    });
    const userInfo = ref(null);

    const getUserInfo = function () {
      axios({
        method: "get",
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          console.log("getuserinfo");
          userInfo.value = res.data;
          if (userInfo.value.financial_products) {
            userInfo.value.financial_products =
              userInfo.value.financial_products.split(",");
          } else {
            userInfo.value.financial_products = [];
          }
        })
        .then(() => {
          getDeposites();
        })
        .then(() => {
          getSavings();
        })
        .then(() => {
          userDeposites.value = [];
          userSavings.value = [];
          const depo = ref();
          const savi = ref();
          for (const fin_prdt_cd of userInfo.value.financial_products) {
            depo.value = [];
            savi.value = [];
            depo.value = deposites.value.filter(
              (elem) => elem.fin_prdt_cd === fin_prdt_cd
            );
            savi.value = savings.value.filter(
              (elem) => elem.fin_prdt_cd === fin_prdt_cd
            );
            console.log(fin_prdt_cd);
            console.log(depo.value, savi.value);

            if (depo.value[0]) {
              userDeposites.value.push(depo.value[0]);
            } else {
              userSavings.value.push(savi.value[0]);
            }
            console.log(userDeposites.value);
            console.log(userSavings.value);
          }
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const updateUserInfo = function (payload) {
      axios({
        method: "put",
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
        data: payload,
      })
        .then((res) => {
          console.log("updateUserinfo");
          getUserInfo();
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const logIn = function (payload) {
      const username = payload.username;
      const password = payload.password;
      axios({
        method: "post",
        url: `${API_URL}/accounts/login/`,
        data: {
          username,
          password,
        },
      })
        .then((res) => {
          token.value = res.data.key;
          console.log(token.value);
          getUserInfo();
          router.replace({ name: "home" });
        })
        .catch(() => {
          alert("아이디 또는 비밀번호를 확인하세요");
          router.push({ name: "LogInView" });
        });
    };

    const logOut = function () {
      if (token.value) {
        axios({
          method: "post",
          url: `${API_URL}/accounts/logout/`,
          headers: {
            Authorization: `Token ${token.value}`,
          },
        })
          .then((res) => {
            token.value = null;
            userInfo.value = null;
            userDeposites.value = [];
            userSavings.value = [];
            deposites.value = [];
            savings.value = [];
            recommendDeposites.value = [];
            recommendSavings.value = [];
            router.replace({ name: "home" });
          })
          .catch((err) => {
            console.log(err);
          });
      }
    };

    const updateProduct = function () {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/products/",
      })
        .then(() => {
          console.log("products updated");
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const getDeposites = function () {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/products/deposite/",
      })
        .then((res) => {
          deposites.value = res.data;
          console.log("deposites loaded");
          return res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const getSavings = function () {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/products/saving/",
      })
        .then((res) => {
          savings.value = res.data;
          console.log("savings loaded");
          return res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    };
    const getBanks = function () {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/products/bank/",
      })
        .then((res) => {
          banks.value = res.data;
          console.log("banks loaded");
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const getWholeProduct = function () {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/products/",
      })
        .then(() => {
          console.log("products updated");
        })
        .then(() => {
          getDeposites();
        })
        .then(() => {
          getSavings();
        })
        .then(() => {
          getBanks();
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const shuffle = function (array) {
      for (let index = array.length - 1; index > 0; index--) {
        // 무작위 index 값을 만든다. (0 이상의 배열 길이 값)
        const randomPosition = Math.floor(Math.random() * (index + 1));

        // 임시로 원본 값을 저장하고, randomPosition을 사용해 배열 요소를 섞는다.
        const temporary = array[index];
        array[index] = array[randomPosition];
        array[randomPosition] = temporary;
      }
    };

    const getRecommendDeposites = function () {
      recommendDeposites.value = deposites.value.filter((elem) => {
        return !deposites.value.includes(userDeposites.value);
      });
      const tmp = [];
      const tmp1 = [];
      const tmp2 = [];
      for (const co of userDeposites.value.map((elem) => elem.fin_co_no)) {
        tmp.push(co);
      }
      for (const re of recommendDeposites.value) {
        if (tmp.includes(re.fin_co_no)) {
          tmp1.push(re);
        } else {
          tmp2.push(re);
        }
      }
      shuffle(tmp2);
      recommendDeposites.value = [...tmp1, ...tmp2];
      recommendDeposites.value = recommendDeposites.value.slice(0, 20);
      shuffle(recommendDeposites.value);
      recommendDeposites.value = recommendDeposites.value.slice(0, 3);
    };

    const getRecommendSavings = function () {
      recommendSavings.value = savings.value.filter((elem) => {
        return !savings.value.includes(userSavings.value);
      });
      const tmp = [];
      const tmp1 = [];
      const tmp2 = [];
      for (const co of userSavings.value.map((elem) => elem.fin_co_no)) {
        tmp.push(co);
      }
      for (const re of recommendSavings.value) {
        if (tmp.includes(re.fin_co_no)) {
          tmp1.push(re);
        } else {
          tmp2.push(re);
        }
      }
      tmp2.sort(() => {
        Math.random();
      });
      shuffle(tmp2);
      recommendSavings.value = [...tmp1, ...tmp2];
      recommendSavings.value = recommendSavings.value.slice(0, 20);
      shuffle(recommendSavings.value);
      recommendSavings.value = recommendSavings.value.slice(0, 3);
    };

    // 환율
    const rates = function () {
      axios({
        method: "get",
        url: `${API_URL}/rates/`,
      });
    };

    // 이거 주석처리
    // const isAuthor = computed(() => {
    //   // 현재 로그인한 사용자와 게시글 작성자를 비교하여 일치하면 true, 아니면 false 반환
    //   return (
    //     isLogin.value &&
    //     userInfo.value &&
    //     article.value.user === userInfo.value.id
    //   );
    // });

    // 현재 로그인된 계정==게시글 작성계정일때만  수정 삭제 가능 기능.
    const checkIsAuthor = computed(() => {
      // 게시글이 선택되었을 때만 계산
      if (article.value) {
        return (
          isLogin.value &&
          userInfo.value &&
          article.value.user === userInfo.value.id
        );
      }
      // 게시글이 선택되지 않은 경우 false 반환
      return false;
    });

    // const deleteArticle = async function (articleId) {
    //   const articleId = article.value.id;
    //   try {
    //     // 삭제 전에 작성자 여부를 확인
    //     if (!isAuthor.value) {
    //       console.error("작성자만 삭제할 수 있습니다.");
    //       return;
    //     } else {
    //       await axios.delete(`${API_URL}/api/v1/articles/${articleId}/`, {
    //         headers: {
    //           Authorization: `Token ${token.value}`,
    //         },
    //       });
    //       // 삭제 성공 시 다른 동작 수행 (예: 게시글 목록 다시 불러오기)
    //       getArticles();
    //     }
    //   } catch (error) {
    //     console.error("게시글 삭제 실패", error);
    //     // 실패 시 필요한 처리 수행
    //   }
    // };

    // 게시글 삭제
    const deleteArticle = function (articleId) {
      // const articleId = article.value.id;
      axios({
        method: "DELETE",
        url: `${API_URL}/api/v1/articles/${articleId}/`,
        header: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          console.log("delete 성공");
          getArticles();
          router.push({ name: "ArticleView" });
          // this.$router.push({ path: '/article/:id/' });
        })
        .catch((err) => {
          console.log("err. 삭제 실패");
        });
    };

    // 댓글 삭제
    const deleteComment = function (commentId) {
      // const commentId = comment.value.id; //article.value.id;
      axios({
        method: "DELETE",
        url: `${API_URL}/api/v1/comments/${commentId}/`,
        // data: {},
        header: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          console.log("delete 성공");

          // router.push({ name: "CommentView" });
          // this.$router.push({ path: '/comment/:id/' });
        })
        .catch((err) => {
          console.log("err. 삭제 실패");
        });
    };

    return {
      checkIsAuthor,
      deleteArticle,
      deleteComment,
      createComment,
      articles, // 민석
      article,
      getArticles, // 민석
      comments, // 민석
      comment,
      content, // 추가: 댓글 내용을 저장할 변수
      // getComments, // 민석
      API_URL,
      // 회원가입, 로그인 유무, 로그인, 로그아웃
      signUp,
      logIn,
      isLogin,
      logOut,
      // 유저정보, 유저 정보를 로드하는 함수, 유저 정보를 업데이트 하는 함수,
      userInfo,
      getUserInfo,
      updateUserInfo,
      // 모든 은행데이터, 모든 예금 데이터, 모든 적금 데이터
      banks,
      deposites,
      savings,
      // 예금/적금/은행 정보를 DB에 업데이트 시키는 함수
      updateProduct,
      // 모든 예금, 적금, 은행 정보를 로드하는 함수
      getDeposites,
      getSavings,
      getBanks,
      // 모든 예금, 적금, 은행 정보를 한번에 로드하는 함수
      getWholeProduct,
      // 유저가 가입한 예금, 적금
      userDeposites,
      userSavings,

      getRecommendDeposites,
      recommendDeposites,
      getRecommendSavings,
      recommendSavings,
      // 토큰
      token,
      rates,
      updatedProduct,
    };
  },
  { persist: { storage: sessionStorage } }
);
