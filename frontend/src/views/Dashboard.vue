<template>
  <v-app>
    <Editor
      mode="preview"
      ref="editor"
      hint="Hint"
      v-model="text"
      :emoji = 'false'
      />
  </v-app>
</template>

<script>
import { Editor } from "vuetify-markdown-editor";
import { VApp } from 'vuetify/lib';

export default {
  name: "Dashboard",
  components: {
    Editor,
    VApp
  },
  data() {
    return {
      text: "",
    };
  }
};
</script>
