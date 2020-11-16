<template>

  <v-dialog 
    v-model = 'isLoggingIn' 
    max-width = '400px'
    >

      <v-card>
        <v-card-title class = 'headline blue darken-2 blue--text text--lighten-5'>
          Login
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
                    label = "Team Name"
                    prepend-icon = "mdi-account-group"
                    :rules = '[rules.rangeLength(3, 20)]'
                    ></v-text-field>
                </v-col>

                <v-col 
                  cols = "12"
                  class = 'pa-0'
                  >
                  <v-text-field
                    v-model = 'password'
                    label = "Password"
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
            Login
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
