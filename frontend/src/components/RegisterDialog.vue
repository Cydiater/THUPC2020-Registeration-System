<template>
  <v-dialog
    v-model = 'isRegistering'
    max-width = '600px'
    lazy-validation
    >

    <v-card>

      <v-card-title class = 'headline primary white--text'>
        报名
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

                  <v-tab>队伍基本信息</v-tab>
                  <v-tab>队员 1</v-tab>
                  <v-tab>队员 2</v-tab>
                  <v-tab>队员 3</v-tab>

                  <v-tabs-slider></v-tabs-slider>

                    <v-tab-item
                      class = 'mt-5'
                      eager
                      >

                      <v-text-field
                        label = '队伍名称'
                        prepend-icon = "mdi-account-group"
                        v-model = 'username'
                        :rules = '[rules.rangeLength(3, 20), rules.preventNullCharacter]'
                        >
                      </v-text-field>

                      <v-text-field
                        label = '密码'
                        type = 'password'
                        prepend-icon = "mdi-lock"
                        v-model = 'password'
                        :rules = '[rules.rangeLength(8, 20)]'
                        >
                      </v-text-field>

                      <v-text-field
                        label = '确认密码'
                        type = 'password'
                        prepend-icon = "mdi-lock"
                        v-model = 'confirm_password'
                        :rules = '[rules.sameWith(password)]'
                        >
                      </v-text-field>

                      <v-select
                        prepend-icon = "mdi-compare-vertical"
                        v-model = 'type'
                        label = '队伍类型'
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
                        label = '同意报名条款'
                        ></v-checkbox>

                    </v-tab-item>

                    <v-tab-item
                      class = 'mt-5'
                      v-for = '(member, index) in members'
                      :key = 'index'
                      eager
                      >

                      <v-text-field
                        label = '队员姓名'
                        prepend-icon = "mdi-account"
                        v-model = 'member.name'
                        :rules = '[rules.rangeLength(2, 10), rules.preventNullCharacter]'
                        >
                      </v-text-field>

                      <v-text-field
                        label = '电子邮箱'
                        prepend-icon="mdi-email"
                        v-model = 'member.email'
                        :rules = '[rules.checkEmail]'
                        >
                      </v-text-field>

                      <v-text-field
                        label = '就读学校'
                        prepend-icon = "mdi-school"
                        v-model = 'member.school'
                        :rules = '[rules.rangeLength(2, 100)]'
                        >
                      </v-text-field>

                      <v-text-field
                        label = '电话号码'
                        prepend-icon = "mdi-phone"
                        v-model = 'member.phone'
                        >
                      </v-text-field>

                      <v-text-field
                        label = '收货地址'
                        prepend-icon = "mdi-google-maps"
                        v-model = 'member.location'
                        >
                      </v-text-field>

                      <v-select
                        :items = "['Male', 'Female']"
                        label = '性别'
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
          提交
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
