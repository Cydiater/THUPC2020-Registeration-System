<template>
  <v-dialog
    v-model = 'isPostingAnnouncement'
    max-width = "900px"
    >
    <v-card>
      <v-card-title class = 'headline blue darken-2 blue--text text--lighten-5'>
        Post Announcement
      </v-card-title>
      <v-card-text
        >
        <v-form>

          <v-row>

            <v-col
              cols = '12'
              class = 'pa-0'
              >
              <v-text-field
                v-model = 'title'
                label = 'Title'
                >
              </v-text-field>
            </v-col>

            <v-col
              cols = '6'
              >
              <v-textarea
                v-model = 'content'
                ></v-textarea>
            </v-col>

            <v-col
              cols = '6'
              >
              <vue-markdown
                :source = 'content'
                >
              </vue-markdown>

            </v-col>

          </v-row>


        </v-form>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
import VueMarkdown from 'vue-markdown';

export default {
  name: 'PostAnnouncement',
  components: {
    VueMarkdown,
  },
  data() {
    return {
      title: '',
      content: '',
    }
  },
  computed: {
    isPostingAnnouncement: {
      get() {
        return Boolean(this.$store.state.status.postingAnnouncement);
      },
      set(value) {
        this.$store.commit(value ? 'setStatus' : 'clearStatus', 'postingAnnouncement');
      }
    }
  }
}
</script>

<style>
h1, h2, h3, h4, h5, h6 {
  margin-bottom: .5rem;
  line-height: 1.2;
}
</style>
