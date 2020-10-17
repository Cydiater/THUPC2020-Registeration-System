<template>


  <v-dialog 
    v-model = 'isLoggingIn' 
    max-width = '400px'
    >

      <v-card>
        <v-card-title class = 'pink darken-2 pink--text text--lighten-5'>
          <span class="headline ">Login</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>

              <v-col cols = "12">
                <v-text-field
                  label="Username"
                ></v-text-field>
              </v-col>

              <v-col cols = "12">
                <v-text-field
                  label="Password"
                  type="password"
                ></v-text-field>
              </v-col>

            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
          >
            Cancel
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
          >
            Login
          </v-btn>
        </v-card-actions>
      </v-card>

  </v-dialog>

</template>

<script>
export default {
  name: 'LoginDialog',
  data() {
    return {

    }
  },
  computed: {
    isLoggingIn: {
      get() {
        return this.$store.state.status == 'loggingIn';
      },
      set(value) {
        this.$store.commit(value ? 
          'openLoginDialog' : 
          'closeLoginDialog');
      }
    }
  }
}
</script>
