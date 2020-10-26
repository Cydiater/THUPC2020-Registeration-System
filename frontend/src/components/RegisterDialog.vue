<template>
  <v-dialog
    v-model = 'isRegistering'
    max-width = '600px'
    >

    <v-card>

      <v-card-title class = 'headline blue darken-2 blue--text text--lighten-5'>
        Sign up
      </v-card-title>

      <v-card-text
        class = 'pb-0'
        >

        <v-container>

          <v-form 
            v-model = 'isFormValid'
            >

            <v-row>

              <v-col
                cols = '12'
                class = 'py-0'
                >

                <v-tabs>

                  <v-tab>Basic</v-tab>
                  <v-tab>Member 1</v-tab>
                  <v-tab>Member 2</v-tab>
                  <v-tab>Member 3</v-tab>

                  <v-tabs-slider></v-tabs-slider>

                    <v-tab-item
                      class = 'mt-5'
                      >
                      <v-text-field
                        label = 'Username'
                        prepend-icon = "mdi-account"
                        v-model = 'username'
                        :rules = '[rules.rangeLength(6, 20)]'
                        >
                      </v-text-field>

                      <v-text-field
                        label = 'Password'
                        type = 'password'
                        prepend-icon = "mdi-lock"
                        v-model = 'password'
                        :rules = '[rules.rangeLength(8, 20)]'
                        >
                      </v-text-field>

                      <v-text-field
                        label = 'Confirm Password'
                        type = 'password'
                        prepend-icon = "mdi-lock"
                        v-model = 'confirm_password'
                        :rules = '[rules.sameWith(password)]'
                        >
                      </v-text-field>

                      <v-text-field
                        label = 'Email'
                        prepend-icon="mdi-email"
                        v-model = 'email'
                        :rules = '[rules.checkEmail]'
                        >
                      </v-text-field>


                    </v-tab-item>

                    <v-tab-item
                      class = 'mt-5'
                      v-for = '(member, index) in members'
                      :key = 'index'
                      >
                      <v-text-field
                        label = 'Member Name'
                        prepend-icon = "mdi-account-outline"
                        v-model = 'member.name'
                        :rules = '[rules.rangeLength(2, 10)]'
                        >
                      </v-text-field>
                    </v-tab-item>

                </v-tabs>


              </v-col>

            </v-row>

          </v-form>

        </v-container>


      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          color = 'primary'
          text
          :disabled = '!isFormValid'
          :loading = 'waitForRegister'
          @click = 'registerRequest({ username, password, email })'
          >
          Sign up
        </v-btn>
      </v-card-actions>

    </v-card>

  </v-dialog> 
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'RegisterDialog',
  data() {
    return {
      isFormValid: false,
      username: '',
      email: '',
      password: '',
      confirm_password: '',
      members: [
        {
          name: '',
        },
        {
          name: '',
        },
        {
          name: '',
        },
      ],
      rules: {
        rangeLength(lowerbound, upperbound) {
          return function(value) {
            if (lowerbound <= value.length && value.length <= upperbound)
              return true;
            return `The length should be between ${lowerbound} and ${upperbound}`;
          }
        },
        sameWith(thisValue) {
          return function(value) {
            if (value && value == thisValue)
              return true;
            return `Confirmed password not match`;
          } 
        },
        checkEmail(value) {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return pattern.test(value) || 'Invalid e-mail.';
        },
      }
    }
  },
  methods: {
    ...mapActions(['registerRequest']),
  },
  computed: {
    isRegistering: {
      get() {
        return Boolean(this.$store.state.status.registering);
      },
      set(value) {
        this.$store.commit(value ? 'setStatus' : 'clearStatus', 'registering');
      }
    },
    waitForRegister() {
      return Boolean(this.$store.state.status.waitForRegister);
    },
  }
}
</script>
