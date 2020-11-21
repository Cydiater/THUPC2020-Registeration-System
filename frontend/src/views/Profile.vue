<template>

  <v-row
    class = 'fill-height'
    align = 'center'
    justify = 'center' 
    >

    <vue-headful
      title = 'THUPC2020 Registeration System'
      >
    </vue-headful>

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
                  eager
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
                  eager
                  v-for = '(member, index) in members'
                  :key = 'index'
                  >

                  <v-row
                    align="center"
                    justify="center"
                    >

                    <v-col
                      cols = 12
                      class = 'py-0'
                      >
                      <v-text-field
                        label = 'Member Name'
                        prepend-icon = "mdi-account"
                        v-model = 'member.name'
                        :rules = '[rules.rangeLength(2, 10)]'
                        readonly
                        >
                      </v-text-field>
                    </v-col>

                    <v-col
                      cols = 12
                      class = 'py-0'
                      >
                      <v-text-field
                        label = 'Email'
                        prepend-icon="mdi-email"
                        v-model = 'member.email'
                        :rules = '[rules.checkEmail]'
                        >
                      </v-text-field>
                    </v-col>

                    <v-col
                      cols = 1
                      class = 'py-0'
                      v-if = 'false'
                      >

                      <v-btn
                        v-if = 'member.emailStatus == "verified"'
                        icon
                        readonly 
                        color = 'primary'
                        :loading = 'waitForGettingEmailStatus'
                        >
                        <v-icon>mdi-check</v-icon>
                      </v-btn>

                      <v-btn
                        v-if = 'member.emailStatus == "null"'
                        text
                        color = 'primary'
                        :loading = 'waitForGettingEmailStatus'
                        >
                        VERIFY
                      </v-btn>

                    </v-col>

                    <v-col
                      cols = 12
                      class = 'py-0'
                      >
                      <v-text-field
                        label = 'School'
                        prepend-icon = "mdi-school"
                        v-model = 'member.school'
                        :rules = '[rules.rangeLength(2, 100)]'
                        readonly
                        >
                      </v-text-field>
                    </v-col>

                    <v-col
                      cols = 12
                      class = 'py-0'
                      >
                      <v-text-field
                        label = 'Phone'
                        prepend-icon = "mdi-phone"
                        v-model = 'member.phone'
                        >
                      </v-text-field>
                    </v-col>

                    <v-col
                      cols = 12
                      class = 'py-0'
                      >
                      <v-text-field
                        label = 'Location'
                        prepend-icon = "mdi-google-maps"
                        v-model = 'member.location'
                        >
                      </v-text-field>
                    </v-col>

                    <v-col
                      cols = 12
                      class = 'py-0'
                      >
                      <v-select
                        :items = "['Male', 'Female']"
                        label = 'Gender'
                        prepend-icon = "mdi-gender-male-female"
                        v-model = 'member.gender'
                        >
                      </v-select>
                    </v-col>

                  </v-row>

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
          text 
          :disabled = '!isFormValid' 
          @click = 'editProfile( members )' 
          color = 'primary' 
          :loading = 'waitForEditingProfile'>
          Update
        </v-btn>
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
      waitForGettingEmailStatus: false,
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
          emailStatus: 'null',
        },
        {
          name: '',
          school: '',
          gender: 'Male',
          email: '',
          phone: '',
          location: '',
          emailStatus: 'null',
        },
        {
          name: '',
          school: '',
          gender: 'Male',
          email: '',
          phone: '',
          location: '',
          emailStatus: 'null',
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
    async user() {
      if (this.$store.state.user) {
        this.username = this.$store.state.user.teamname;
        if (this.$store.state.user.type)
          this.type = this.$store.state.user.type.toUpperCase();
        this.members = this.$store.state.user.members;
        this.waitForGettingEmailStatus = true;
        //for (let member of this.members) 
            //await this.$store.dispatch('updateMemberEmailStatus', member)
        this.waitForGettingEmailStatus = false;
      }
    }
  }
}
</script>
