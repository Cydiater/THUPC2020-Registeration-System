<template>
  <v-dialog 
    v-model = 'isHandlingEmail'
    max-width="400px"
    >
    <v-card
      >
      <v-card-title
        class = 'primary white--text'
        >
        验证邮箱
      </v-card-title>
      <v-card-text
        class = 'pb-0'
        >
        <v-form>
          <v-text-field
            label = '验证码'
            prepend-icon="mdi-email-open"
            v-model = 'code'
            >
          </v-text-field>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          text
          @click = 'verifyEmail(currentEmail)'
          :loading = 'emailStatus[currentEmail] == "waitForResponse"'
          >
          再次发送
        </v-btn>
        <v-btn 
          text
          color = 'primary'
          @click = 'verifyCode({ email: currentEmail, code })'
          >
          验证
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  name: 'HandleEmailDialog',
  data() {
    return {
      code: '',
    }
  },
  methods: {
    ...mapActions(['verifyEmail', 'verifyCode']),
  },
  computed: {
    isHandlingEmail: {
      get() {
        return Boolean(this.$store.state.status.handlingEmail);
      },
      set(value) {
        this.$store.commit(value ? 'setStatus': 'clearStatus', 'handlingEmail');
      }
    },
    ...mapState(['emailStatus', 'currentEmail']),
  }
}
</script>
