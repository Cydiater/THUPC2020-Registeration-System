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

                <Editor
                  mode = 'viewer'
                  :value = 'content'
                >

                </Editor>

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
import { Editor } from 'vuetify-markdown-editor';
import { mapGetters } from 'vuex';
import PostAnnouncement from '@/components/PostAnnouncement';

export default {
  name: "Dashboard",
  components: {
    Editor,
    PostAnnouncement,
  },
  data() {
    return {
      text: "",
      show: false,
      content: 'markdown test *bold*',
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
      this.$store.dispatch('fetchUserInfo');
  }
};
</script>
