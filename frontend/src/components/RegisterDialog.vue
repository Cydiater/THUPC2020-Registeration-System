<template>
  <v-dialog
    v-model = 'isRegistering'
    max-width = '600px'
    lazy-validation
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
                      eager
                      >

                      <v-text-field
                        label = 'Team Name'
                        prepend-icon = "mdi-account-group"
                        v-model = 'username'
                        :rules = '[rules.rangeLength(3, 20), rules.preventNullCharacter]'
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

                      <v-select
                        prepend-icon = "mdi-compare-vertical"
                        v-model = 'type'
                        label = 'Type'
                        :items = '["A", "B", "C"]'
                        >
                      </v-select>

                      <p class = 'text-caption'>
                        A 类：队伍中的所有选手都为清华大学在校学生 <br />
                        B 类：队伍中的所有选手都为大学在校学生，但存在不是清华大学在校学生的选手 <br />
                        C 类：其他队伍
                      </p>

                      <v-checkbox
                        v-model = 'agree'
                        label = 'Agree to terms of enrollment'
                        ></v-checkbox>

                    </v-tab-item>

                    <v-tab-item
                      class = 'mt-5'
                      v-for = '(member, index) in members'
                      :key = 'index'
                      eager
                      >

                      <v-text-field
                        label = 'Member Name'
                        prepend-icon = "mdi-account"
                        v-model = 'member.name'
                        :rules = '[rules.rangeLength(2, 10), rules.preventNullCharacter]'
                        >
                      </v-text-field>

                      <v-text-field
                        label = 'Email'
                        prepend-icon="mdi-email"
                        v-model = 'member.email'
                        :rules = '[rules.checkEmail]'
                        >
                      </v-text-field>

                      <v-text-field
                        label = 'School'
                        prepend-icon = "mdi-school"
                        v-model = 'member.school'
                        :rules = '[rules.rangeLength(2, 100)]'
                        >
                      </v-text-field>

                      <v-text-field
                        label = 'Phone'
                        prepend-icon = "mdi-phone"
                        v-model = 'member.phone'
                        >
                      </v-text-field>

                      <v-text-field
                        label = 'Location'
                        prepend-icon = "mdi-google-maps"
                        v-model = 'member.location'
                        >
                      </v-text-field>

                      <v-select
                        :items = "['Male', 'Female']"
                        label = 'Gender'
                        prepend-icon = "mdi-gender-male-female"
                        v-model = 'member.gender'
                        required
                        >
                      </v-select>

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
          :disabled = '!isFormValid || !agree'
          :loading = 'waitForRegister'
          @click = 'registerRequest({ username, password, members, type })'
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
      agree: true,
      username: '',
      password: '',
      confirm_password: '',
      type: 'A',
      members: [
        {
          name: '',
          school: '',
          gender: 'Male',
          email: '',
          phone: '',
          location: '',
        },
        {
          name: '',
          school: '',
          gender: 'Male',
          email: '',
          phone: '',
          location: '',
        },
        {
          name: '',
          school: '',
          gender: 'Male',
          email: '',
          phone: '',
          location: '',
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
