<template>

  <v-dialog 
    v-model = 'isLoggingIn' 
    max-width = '400px'
    >

      <v-card>
        <v-card-title class = 'headline primary white--text'>
          登录
        </v-card-title>
        <v-card-text
          class = 'pb-0'
          >
          <v-container>
            <v-form v-model = 'isFormVaild'>
              <v-row>

                <v-col 
                  cols = "12"
                  class = 'pa-0'
                  >
                  <v-text-field
                    v-model = 'username'
                    label = "队伍名称"
                    prepend-icon = "mdi-account-group"
                    :rules = '[rules.rangeLength(3, 20), rules.preventNullCharacter]'
                    ></v-text-field>
                </v-col>

                <v-col 
                  cols = "12"
                  class = 'pa-0'
                  >
                  <v-text-field
                    v-model = 'password'
                    label = "密码"
                    type = "password"
                    prepend-icon = "mdi-lock"
                    :rules = '[rules.rangeLength(8, 20)]'
                    ></v-text-field>
                </v-col>

              </v-row>
            </v-form>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click = 'loginRequest({ username, password })'
            :loading = 'isWaitForLogin'
            :disabled = '!isFormVaild'
          >
          登录
          </v-btn>
        </v-card-actions>
      </v-card>

  </v-dialog>

</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'LoginDialog',
  data() {
    return {
      isFormVaild: false,
      username: '',
      password: '',
      rules: {
        rangeLength(lowerbound, upperbound) {
          return function(value) {
            if (lowerbound <= value.length && value.length <= upperbound)
              return true;
            return `The length should be between ${lowerbound} and ${upperbound}`;
          }
        },
        preventNullCharacter(value) {
          const pattern = /[\n\r\t\0\s]/;
          if (pattern.test(value))
            return 'Containing null characters';
          return true;
        }
      }
    }
  },
  methods: {
    ...mapActions(['loginRequest']),
  },
  computed: {
    isLoggingIn: {
      get() {
        return Boolean(this.$store.state.status.loggingIn);
      },
      set(value) {
        this.$store.commit(value ? 'setStatus' : 'clearStatus', 'loggingIn');
      }
    },
    isWaitForLogin() {
      return Boolean(this.$store.state.status.waitForLogin);
    }
  }
}
</script>
