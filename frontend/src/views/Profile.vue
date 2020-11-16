<template>

  <v-row
    class = 'fill-height'
    align = 'center'
    justify = 'center' 
    >

    <v-col
      :cols = '6'
      >

    <v-card
      v-if = 'isLoggedIn'
      >

      <v-card-title
        class = 'primary--text'
        >
        Registeration Infomation
      </v-card-title>

      <v-card-text
        class = 'pb-0'
        >

        <v-container
          v-if = 'this.$store.state.user'
          >

          <v-form v-model = 'isFormValid'>

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
                    label = 'Team Name'
                    prepend-icon = "mdi-account-group"
                    :value = 'username'
                    readonly
                    >
                  </v-text-field>

                  <v-select
                    prepend-icon = "mdi-compare-vertical"
                    :value = 'type'
                    label = 'Type'
                    :items = '["A", "B", "C"]'
                    readonly
                    >
                  </v-select>

                  <p class = 'text-caption'>
                    A 类：队伍中的所有选手都为清华大学在校学生 <br />
                    B 类：队伍中的所有选手都为大学在校学生，但存在不是清华大学在校学生的选手 <br />
                    C 类：其他队伍
                  </p>

                </v-tab-item>

                <v-tab-item
                  class = 'mt-5'
                  >

                  <v-text-field
                    label = 'Member Name'
                    prepend-icon = "mdi-account"
                    v-model = 'members[0].name'
                    :rules = '[rules.rangeLength(2, 10)]'
                    readonly
                    >
                  </v-text-field>

                  <v-text-field
                    label = 'Email'
                    prepend-icon="mdi-email"
                    v-model = 'members[0].email'
                    :rules = '[rules.checkEmail]'
                    >
                  </v-text-field>

                  <v-text-field
                    label = 'School'
                    prepend-icon = "mdi-school"
                    v-model = 'members[0].school'
                    :rules = '[rules.rangeLength(2, 100)]'
                    readonly
                    >
                  </v-text-field>

                  <v-text-field
                    label = 'Phone'
                    prepend-icon = "mdi-phone"
                    v-model = 'members[0].phone'
                    >
                  </v-text-field>

                  <v-text-field
                    label = 'Location'
                    prepend-icon = "mdi-google-maps"
                    v-model = 'members[0].location'
                    >
                  </v-text-field>

                  <v-select
                    :items = "['Male', 'Female']"
                    label = 'Gender'
                    prepend-icon = "mdi-gender-male-female"
                    v-model = 'members[0].gender'
                    >
                  </v-select>

                </v-tab-item>

                <v-tab-item
                  class = 'mt-5'
                  >

                  <v-text-field
                    label = 'Member Name'
                    prepend-icon = "mdi-account"
                    v-model = 'members[1].name'
                    :rules = '[rules.rangeLength(2, 10)]'
                    readonly
                    >
                  </v-text-field>

                  <v-text-field
                    label = 'Email'
                    prepend-icon="mdi-email"
                    v-model = 'members[1].email'
                    :rules = '[rules.checkEmail]'
                    >
                  </v-text-field>

                  <v-text-field
                    label = 'School'
                    prepend-icon = "mdi-school"
                    v-model = 'members[1].school'
                    :rules = '[rules.rangeLength(2, 100)]'
                    readonly
                    >
                  </v-text-field>

                  <v-text-field
                    label = 'Phone'
                    prepend-icon = "mdi-phone"
                    v-model = 'members[1].phone'
                    >
                  </v-text-field>

                  <v-text-field
                    label = 'Location'
                    prepend-icon = "mdi-google-maps"
                    v-model = 'members[1].location'
                    >
                  </v-text-field>

                  <v-select
                    :items = "['Male', 'Female']"
                    label = 'Gender'
                    prepend-icon = "mdi-gender-male-female"
                    v-model = 'members[1].gender'
                    >
                  </v-select>

                </v-tab-item>

                <v-tab-item
                  class = 'mt-5'
                  >

                  <v-text-field
                    label = 'Member Name'
                    prepend-icon = "mdi-account"
                    v-model = 'members[2].name'
                    :rules = '[rules.rangeLength(2, 10)]'
                    >
                  </v-text-field>

                  <v-text-field
                    label = 'Email'
                    prepend-icon="mdi-email"
                    v-model = 'members[2].email'
                    :rules = '[rules.checkEmail]'
                    >
                  </v-text-field>

                  <v-text-field
                    label = 'School'
                    prepend-icon = "mdi-school"
                    v-model = 'members[2].school'
                    :rules = '[rules.rangeLength(2, 100)]'
                    readonly
                    >
                  </v-text-field>

                  <v-text-field
                    label = 'Phone'
                    prepend-icon = "mdi-phone"
                    v-model = 'members[2].phone'
                    >
                  </v-text-field>

                  <v-text-field
                    label = 'Location'
                    prepend-icon = "mdi-google-maps"
                    v-model = 'members[2].location'
                    >
                  </v-text-field>

                  <v-select
                    :items = "['Male', 'Female']"
                    label = 'Gender'
                    prepend-icon = "mdi-gender-male-female"
                    v-model = 'members[2].gender'
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
        <v-btn text :disabled = '!isFormValid' @click = 'editProfile( members )' color = 'primary' :loading = 'waitForEditingProfile'>Update</v-btn>
      </v-card-actions>

    </v-card>

    </v-col>
  </v-row>
</template>

<script>
import { mapGetters, mapState, mapActions } from 'vuex';

export default {
  name: 'Profile',
  data() {
    return {
      isFormValid: false,
      username: '',
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
      }
    }
  },
  computed: {
    ...mapGetters(['isLoggedIn']),
    ...mapState(['user']),
    waitForEditingProfile() {
      return Boolean(this.$store.state.status.waitForEditingProfile);
    }
  },
  methods: {
    ...mapActions(['editProfile']),
  },
  created() {
    if (this.$store.getters.isLoggedIn)
      this.$store.dispatch('fetchUserInfo', localStorage.getItem('username'));
  },
  watch: {
    user() {
      if (this.$store.state.user) {
        this.username = this.$store.state.user.teamname;
        if (this.$store.state.user.type)
          this.type = this.$store.state.user.type;
        this.members = this.$store.state.user.members;
      }
    }
  }
}
</script>
