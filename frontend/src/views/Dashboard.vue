<template>
  <v-card
    class = 'fill-height'
    flat
    tile
    >

    <vue-headful
      title = 'THUPC2020 Registeration System'
      >
    </vue-headful>

    <v-card
      width="800px"
      class = 'mx-auto my-2'
      >

      <v-card-title>公告</v-card-title>
      <v-card-text>

        <v-list
          >

          <v-list-item
            class = 'my-2'
            v-for = 'announcement of announcements'
            :key = 'announcement.post_id'
            >

            <v-card
              class = "mx-auto"
              width = '800px'
              >

              <v-card-title
                class = 'primary--text font-weight-bold'
                >
                {{announcement.title}}
              </v-card-title>

              <v-card-subtitle 
                >
                {{announcement.author}} at {{ announcement.timestamp | formatTime }}
              </v-card-subtitle>

              <v-card-actions>

                <v-spacer></v-spacer>

                <v-btn icon v-if = 'isAdmin()' @click = 'openEADialog(announcement)'>
                  <v-icon>mdi-pencil</v-icon>
                </v-btn>

                <v-btn
                  icon
                  @click="toggleAnnouncement(announcement)"
                  >
                  <v-icon>{{ announcement.show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
                </v-btn>

              </v-card-actions>

              <v-expand-transition>

                <div v-show="announcement.show">
                  <v-divider></v-divider>

                  <v-card-text>

                    <vue-markdown
                      mode = 'viewer'
                      :source = 'announcement.content'
                      >
                    </vue-markdown>

                  </v-card-text>

                </div>

              </v-expand-transition>

            </v-card>
          </v-list-item>

        </v-list>
      </v-card-text>

    </v-card>

    <v-btn
      fab
      color = 'primary'
      fixed
      bottom
      right
      @click = 'openPADialog'
      v-if = 'isAdmin()'
      >
      <v-icon>mdi-plus</v-icon>
    </v-btn>

    <PostAnnouncement />
    <EditAnnouncement />

  </v-card>
</template>

<script>
import VueMarkdown from 'vue-markdown';
import { mapGetters, mapState, mapMutations } from 'vuex';
import PostAnnouncement from '@/components/PostAnnouncement';
import EditAnnouncement from '@/components/EditAnnouncement';

export default {
  name: "Dashboard",
  components: {
    VueMarkdown,
    PostAnnouncement,
    EditAnnouncement,
  },
  data() {
    return {
      show: [],
    }
  },
  methods: {
    ...mapGetters(['isAdmin', 'isLoggedIn']),
    ...mapMutations(['toggleAnnouncement']),
    openPADialog() {
      this.$store.commit('setStatus', 'postingAnnouncement');
    },
    openEADialog(announcement) {
      this.$store.commit('setCurrentAnnouncement', announcement);
      this.$store.commit('setStatus', 'editingAnnouncement');
    }
  },
  computed: {
    ...mapState(['announcements'])
  },
  created() {
    this.$store.dispatch('getAnnouncements');
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
