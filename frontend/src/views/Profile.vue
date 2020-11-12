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

                  <v-text-field
                    label = 'Email'
                    prepend-icon="mdi-email"
                    :value = 'email'
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

                </v-tab-item>

                <v-tab-item
                  class = 'mt-5'
                  >

                  <v-text-field
                    label = 'Member Name'
                    prepend-icon = "mdi-account"
                    :value = 'members[0].name'
                    readonly
                    >
                  </v-text-field>

                  <v-text-field
                    label = 'School'
                    prepend-icon = "mdi-school"
                    :value = 'members[0].school'
                    >
                  </v-text-field>

                  <v-select
                    :items = "['Male', 'Female']"
                    label = 'Gender'
                    prepend-icon = "mdi-gender-male-female"
                    :value = 'members[0].gender'
                    readonly
                    >
                  </v-select>

                </v-tab-item>

                <v-tab-item
                  class = 'mt-5'
                  >

                  <v-text-field
                    label = 'Member Name'
                    prepend-icon = "mdi-account"
                    :value = 'members[1].name'
                    readonly
                    >
                  </v-text-field>

                  <v-text-field
                    label = 'School'
                    prepend-icon = "mdi-school"
                    :value = 'members[1].school'
                    readonly
                    >
                  </v-text-field>

                  <v-select
                    :items = "['Male', 'Female']"
                    label = 'Gender'
                    prepend-icon = "mdi-gender-male-female"
                    :value = 'members[1].gender'
                    readonly
                    >
                  </v-select>

                </v-tab-item>

                <v-tab-item
                  class = 'mt-5'
                  >

                  <v-text-field
                    label = 'Member Name'
                    prepend-icon = "mdi-account"
                    :value = 'members[2].name'
                    readonly
                    >
                  </v-text-field>

                  <v-text-field
                    label = 'School'
                    prepend-icon = "mdi-school"
                    :value = 'members[2].school'
                    readonly
                    >
                  </v-text-field>

                  <v-select
                    :items = "['Male', 'Female']"
                    label = 'Gender'
                    prepend-icon = "mdi-gender-male-female"
                    :value = 'members[2].gender'
                    readonly
                    >
                  </v-select>

                </v-tab-item>

              </v-tabs>

            </v-col>

          </v-row>

        </v-container>

      </v-card-text>

    </v-card>
    </v-col>
  </v-row>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'Profile',
  computed: {
    ...mapState({
      username: state => state.user.teamname,
      email: state => state.user.email,
      type: state => state.user.type.toUpperCase(),
      members: state => state.user.members,
    })
  },
  created() {
    this.$store.dispatch('fetchUserInfo', localStorage.getItem('username'));
  }
}
</script>
