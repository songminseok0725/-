import { createRouter, createWebHistory } from "vue-router";
import MainView from "@/views/MainView.vue";
import SignUpView from "@/views/SignUpView.vue";
import LogInView from "@/views/LogInView.vue";
import UserInfoView from "@/views/UserInfoView.vue";
import UserInfoUpdate from "@/views/UserInfoUpdate.vue";
import MapView from "@/views/MapView.vue";
import RateView from "@/views/RateView.vue";
import ProductView from "@/views/ProductView.vue";
import DepositeDetailView from "@/views/DepositeDetailView.vue";
import SavingDetailView from "@/views/SavingDetailView.vue";
import ArticleView from "@/views/ArticleView.vue"; // 민석
import DetailView from "@/views/DetailView.vue"; // 민석
import CreateView from "@/views/CreateView.vue"; // 민석
import PutView from "@/views/PutView.vue"; // 민석
import CommentView from "@/views/CommentView.vue"; // 민석
import CommentList from "@/components/CommentList.vue"; // 이거 추가
import PutCommentView from "@/views/PutCommentView.vue"; // 이거 추가
import UserProfileView from "@/views/UserProfileView.vue";
import { useCounterStore } from "@/stores/counter";
//
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: MainView,
    },
    {
      path: "/signup",
      name: "SignUpView",
      component: SignUpView,
    },
    {
      path: "/login",
      name: "LogInView",
      component: LogInView,
    },
    {
      path: "/userinfo",
      name: "userinfo",
      component: UserProfileView,
    },
    {
      path: "/userinfoupdate",
      name: "userinfoupdate",
      component: UserInfoUpdate,
    },
    {
      path: "/map",
      name: "map",
      component: MapView,
    },
    {
      path: "/rate",
      name: "rate",
      component: RateView,
    },
    {
      path: "/product",
      name: "product",
      component: ProductView,
    },
    {
      path: "/deposite/detail/:fin_prdt_cd ",
      name: "deposite-detail",
      component: DepositeDetailView,
    },
    {
      path: "/saving/detail/:fin_prdt_cd",
      name: "saving-detail",
      component: SavingDetailView,
    },
    // 민석
    // 게시글 페이지
    {
      path: "/article",
      name: "ArticleView",
      component: ArticleView,
    },
    // 게시글 페이지
    {
      path: "/article/:id",
      name: "DetailView",
      component: DetailView,
    },
    // 게시글 작성 페이지
    {
      path: "/create",
      name: "CreateView",
      component: CreateView,
    },
    // 게시글 수정 페이지
    {
      path: "/put/:id",
      name: "PutView",
      component: PutView,
    },
    // 댓글 구현
    {
      path: "/comment/:id",
      name: "CommentView",
      component: CommentView,
    },
    // 댓글 목록
    {
      path: "/commentlist/:id",
      name: "CommentList",
      component: CommentList,
    },
    // 댓글 수정
    {
      path: "/putcomment/:id",
      name: "PutCommentView",
      component: PutCommentView,
    },
  ],
});

router.beforeEach((to, from) => {
  const store = useCounterStore();
  if (to.name === "userinfo" && !store.isLogin) {
    window.alert("로그인이 필요합니다.");
    return { name: "LogInView" };
  }
  if ((to.name === "SignUpView" || to.name === "LogInView") && store.isLogin) {
    window.alert("이미 로그인 되어있습니다.");
    return { name: "MainView" };
  }
  if (to.name === "userinfo") {
    store.getUserInfo();
  }
});

export default router;
