<template>
  <v-dialog
    v-model = 'isPostingAnnouncement'
    max-width = "900px"
    height = '90%'
    >
    <v-card>
      <v-card-title class = 'headline primary white--text'>
        发布公告
      </v-card-title>
      <v-card-text
        >
        <v-form
          v-model = 'isFormValid'
          >

          <v-row 
            >

            <v-col
              cols = '6'
              >
              <v-text-field
                v-model = 'title'
                label = 'Title'
                :rules = '[rules.rangeLength(3, 50)]'
                >
              </v-text-field>
            </v-col>

            <v-col
              cols = '3'
              >
              <v-text-field
                v-model = 'author'
                label = 'Author'
                :rules = '[rules.rangeLength(2, 20)]'
                >
              </v-text-field>
            </v-col>

            <v-col>
              <v-text-field
                :value = 'formatTime'
                label = 'Time'
                type = 'date'
                readonly
                >
              </v-text-field>
            </v-col>

            <v-col
              cols = '6'
              >
              <v-textarea
                v-model = 'content'
                outlined
                label = 'Content'
                rows = '10'
                hide-details
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

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text :disabled = '!isFormValid' color = 'primary' :loading = 'waitForPostAnnouncement' @click = 'postAnnouncement({ title, author, content, timestamp })'>Post</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import VueMarkdown from 'vue-markdown';
import { mapActions } from 'vuex';

export default {
  name: 'PostAnnouncement',
  components: {
    VueMarkdown,
  },
  data() {
    return {
      isFormValid: false,
      title: '',
      author: '',
      content: '',
      timestamp: new Date().getTime(),
      rules: {
        rangeLength(lowerbound, upperbound) {
          return function(value) {
            if (lowerbound <= value.length && value.length <= upperbound)
              return true;
            return `The length should be between ${lowerbound} and ${upperbound}`;
          }
        }
      }
    }
  },
  methods: {
    ...mapActions(['postAnnouncement']),
  },
  computed: {
    isPostingAnnouncement: {
      get() {
        return Boolean(this.$store.state.status.postingAnnouncement);
      },
      set(value) {
        this.$store.commit(value ? 'setStatus' : 'clearStatus', 'postingAnnouncement');
      }
    },
    formatTime() {
      const date = new Date(this.timestamp);
      return `${date.getFullYear()}-${('0' + (date.getMonth() + 1)).split('').splice(-2).join('')}-${('0' + date.getDate()).split('').splice(-2).join('')}`
    },
    waitForPostAnnouncement() {
      return Boolean(this.$store.state.status.waitForPostAnnouncement);
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
