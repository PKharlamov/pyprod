<script setup>
import {useTreeStore} from "@/stores/tree.store";
const treeStore = useTreeStore();

window.onscroll = function() {
  let treeButtonElement = this.document.getElementById("treeButton");
  let treeBrowserElement = this.document.getElementById("treeBrowser");
  let scrollTop = document.documentElement.scrollTop;
  let articleWindow = this.document.getElementById("articleWindow");

  if ((document.documentElement.scrollTop || document.body.scrollTop) - articleWindow.offsetHeight + treeBrowserElement.offsetHeight < 0) {
    treeButtonElement.style.transform = "translateY(" + scrollTop + "px)";
    treeBrowserElement.style.transform = "translateY(" + scrollTop + "px)";
  }
};

</script>

<template>
  <div
    class="
      container
      m-auto
      my-5
      border-2
      border-black
      rounded-lg
      p-5
    "
    v-show="!treeStore.isTreeVisible"
  >
    <p class="text-center text-2xl">{{ listName }}</p>

    <div
      class="
        grid
        gap-4
        grid-cols-1
        sm:grid-cols-2
        md:grid-cols-3
        lg:grid-cols-4
        xl:grid-cols-5
        pt-5
      "
    >
      <subject-block-node
        @showTree="
          treeStore.isTreeVisible = true
          setArticleToShow($event);
          updateRoute();
          this.findFullRoute(this.treeData, this.ArticleToShow.slug)
        "
        v-for="elem in this.treeData"
          :key="elem"
          :title="elem.title"
          :node="elem"
      />
    </div>
  </div>

  <!-- Здесь колхоз надо поправить (absolute top-[500px] left-[0px]) -->
  <div
    id="treeButton"
    v-show="treeStore.isTreeVisible"
  >
    <button
        type="button"
        class="
            absolute top-[500px] left-[0px]
            text-sm
            text-gray-500
            rounded-lg
            md:hidden
            hover:bg-gray-100
          "
        @click="togglePopupTree()"
    >
      <span>&#127795</span>
    </button>
  </div>

  <div
    id="articleWindow"
    class="
      container
      grid
      grid-cols-4
      gap-4
      mx-auto
      my-5
      bg-gray-100
      border-2
      border-gray-300
      rounded-lg
    "
    v-show="treeStore.isTreeVisible"
  >
    <!-- Здесь колхоз надо поправить -->
    <div>
      <div
        id="treeBrowser"
        class="
          mx-auto
          col-span-1
          md:block
        "
        v-if="fullRoute.length > 0"
        v-bind:class="{'hidden col-span-1': !showPopupTree, 'col-span-4': showPopupTree}"
      >
        <div class="mr-0">
          <tree-browser
            @changeArticle="
              setArticleToShow($event);
              updateRoute()
            "
            v-for="child in this.treeData"
              :key="child.title"
              :node="child"
              :path-array="fullRoute"
          ></tree-browser>
        </div>
      </div>
    </div>

    <div
      class="
        md:col-span-3
        col-span-4
        p-10
        bg-white
        rounded-lg
      "
      v-bind:class="{'col-span-3': !showPopupTree, 'col-span-0 hidden': showPopupTree}"
       v-if="(typeof ArticleToShow) === (typeof {})"
    >
      <article-block :node="ArticleToShow"/>
    </div>
  </div>
</template>

<script>
import subjectBlockNode from "@/components/SubjectBlockNode.vue";
import treeBrowser from "@/components/TreeBrowser.vue";
import articleBlock from "@/components/ArticleBlock.vue";
import axios from "axios";
import {useTreeStore} from "@/stores/tree.store";

export default {
  components: {subjectBlockNode, treeBrowser, articleBlock},

  name: "subject-block",

  props: {
    listName: String
  },

  data() {
    return {
      urlArticleTree: 'http://127.0.0.1:8000/api/web/v1/articles/index/',
      urlArticle: 'http://127.0.0.1:8000/api/web/v1/articles/',
      treeData: [],
      errors: [],
      ArticleToShow: Object,
      fullRoute: [],
      showPopupTree: false,
      windowWidth: window.innerWidth,
    }
  },

  async created() {
    await this.fetchArticleTree(this.urlArticleTree)

    if (this.$route.params.slug !== undefined)
      if (this.$route.params.slug.length > 0){
        await this.fetchArticle(this.urlArticle, this.$route.params.slug)
        this.findFullRoute(this.treeData, this.$route.params.slug[0])

        useTreeStore().isTreeVisible = true
      }
  },

  mounted() {
    this.$nextTick(() => {
      window.addEventListener('resize', this.onResize);
    })
  },

  beforeDestroy() {
    // Убедиться что это нужно
    window.removeEventListener('resize', this.onResize);
  },

  methods: {
    findFullRoute(tree, slug) {
      for (const treeNode of tree)
      {
        if (treeNode.slug === slug)
        {
          this.fullRoute.unshift(treeNode.slug)
          return true
        }

        if (this.findFullRoute(treeNode.children, slug) === true)
        {
          this.fullRoute.unshift(treeNode.slug)
          return true
        }
      }
      return false
    },

    setArticleToShow(node) {
      this.ArticleToShow = node
    },

    updateRoute() {
      this.$router.push(`/articles/${this.ArticleToShow.slug}`)
    },

    async fetchArticleTree(url) {
      await axios
          .get(url)
          .then(response => this.treeData.push(...(response.data)))
    },

    async fetchArticle(url, slug) {
      await axios
          .get(url + slug)
          .then(response => this.ArticleToShow = response.data)
    },

    togglePopupTree(){
      this.showPopupTree = !this.showPopupTree;
    },

    onResize() {
      this.windowWidth = window.innerWidth
      if (this.windowWidth > 768)
        this.showPopupTree = false;
    }

  },

  watch: {
    $route: function () {
      if (this.$route.params.slug !== undefined){
        this.fullRoute = []
        this.findFullRoute(this.treeData, this.$route.params.slug[0])
      }
      else {
        useTreeStore().isTreeVisible = false
      }
    },

    ArticleToShow: function() {
      this.showPopupTree = false;
    }
  },

}
</script>
