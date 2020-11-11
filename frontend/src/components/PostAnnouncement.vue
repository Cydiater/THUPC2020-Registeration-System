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

            <v-col>
              <Editor
                mode = 'preview'
                v-model = 'content'
                :emoji = 'false'
              >

              </Editor>
            </v-col>

          </v-row>


        </v-form>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
import { Editor } from 'vuetify-markdown-editor';

export default {
  name: 'PostAnnouncement',
  components: {
    Editor,
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
