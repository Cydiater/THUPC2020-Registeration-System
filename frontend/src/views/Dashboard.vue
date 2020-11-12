<template>
  <v-card
    class = 'fill-height'
    flat
    tile
    >

    <v-list>

      <v-list-item
        class = 'my-2'
        >

        <v-card
          class = "mx-auto"
          width = '800px'
          >

          <v-card-title>
            欢迎报名 THUPC2020
          </v-card-title>

          <v-card-subtitle 
            >
            admin, 2020 年 11 月 11 日
          </v-card-subtitle>

          <v-card-actions>

            <v-spacer></v-spacer>

            <v-btn
              icon
              @click="show = !show"
              >
              <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
            </v-btn>
          </v-card-actions>

          <v-expand-transition>

            <div v-show="show">
              <v-divider></v-divider>

              <v-card-text>

                <vue-markdown
                  mode = 'viewer'
                  :source = 'content'
                >
                </vue-markdown>

              </v-card-text>

            </div>

          </v-expand-transition>
        </v-card>
      </v-list-item>

    </v-list>

    <v-btn
      fab
      color = 'primary'
      fixed
      bottom
      right
      @click = 'openPADialog'
      v-if = 'isLoggedIn'
      >
      <v-icon>mdi-plus</v-icon>
    </v-btn>

    <PostAnnouncement />

  </v-card>
</template>

<script>
import VueMarkdown from 'vue-markdown';
import { mapGetters } from 'vuex';
import PostAnnouncement from '@/components/PostAnnouncement';

export default {
  name: "Dashboard",
  components: {
    VueMarkdown,
    PostAnnouncement,
  },
  data() {
    return {
      text: "",
      show: false,
      content: 'markdown test **bold**',
    };
  },
  methods: {
    ...mapGetters(['isLoggedIn']),
    openPADialog() {
      this.$store.commit('setStatus', 'postingAnnouncement');
    }
  },
  created() {
    if (this.isLoggedIn())
      this.$store.dispatch('fetchUserInfo', localStorage.getItem('username'));
  }
};
</script>

<style>
h1, h2, h3, h4, h5, h6 {
  margin-bottom: .5rem;
  line-height: 1.2;
}
</style>
