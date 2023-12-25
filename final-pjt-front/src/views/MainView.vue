<template>
  <div class="main-view">
    <header class="header">
      <h1>석세권뱅크에 오신것을 환영합니다</h1>
    </header>

    <div class="video-container">
      <video
        ref="myVideo"
        controls
        loop
        muted
        :src="currentVideoSource"
        class="responsive-video"
        autoplay
      >
        Your browser does not support the video tag.
      </video>
    </div>

    <div class="controls">
      <button @click="playPreviousVideo">
        <i class="fas fa-arrow-left"></i>
        <!-- Font Awesome 화살표 왼쪽 아이콘 -->
      </button>

      <button @click="playNextVideo">
        <i class="fas fa-arrow-right"></i>
        <!-- Font Awesome 화살표 오른쪽 아이콘 -->
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      videos: [
        "/mainpagetest1.mp4",
        "/mainpagetest2.mp4",
        // 추가 동영상 경로들을 필요한 만큼 추가하세요
      ],
      currentVideoIndex: 0,
    };
  },
  computed: {
    currentVideoSource() {
      return this.videos[this.currentVideoIndex];
    },
  },
  methods: {
    playPreviousVideo() {
      // 이전 동영상으로 전환
      this.currentVideoIndex =
        (this.currentVideoIndex - 1 + this.videos.length) % this.videos.length;
    },
    playNextVideo() {
      // 다음 동영상으로 전환
      this.currentVideoIndex =
        (this.currentVideoIndex + 1) % this.videos.length;
    },
  },
};
</script>

<style scoped>
.main-view {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

.header {
  background-color: #009688;
  color: #fff;
  /* padding: 1px; */
}

.video-container {
  margin-top: 20px;
}

.responsive-video {
  width: 100%;
  height: auto;
}

.controls {
  margin-top: 10px;
}

.controls button {
  padding: 10px;
  font-size: 16px;
  cursor: pointer;
}
</style>
