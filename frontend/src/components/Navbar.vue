<template>
  <nav>

    <!-- Top Bar -->

    <v-app-bar
      class = 'primary'
      dense
      app
      >

      <v-app-bar-nav-icon @click = "showSidebar = !showSidebar" class = 'blue--text text--lighten-5'></v-app-bar-nav-icon>
      <v-toolbar-title
        class = 'mr-5 white--text'
        >
        <v-row
          align="center"
          justify="start"
          style = 'width: 900px;'
          >

          <v-col
            cols = 5
            >
              THUPC2020 Registeration System
          </v-col>

          <v-col
            cols = 1
            >
            <v-img 
              height = "40px"
              src = '@/assets/thusaac.png'
              contain
              class = 'ma-0'
              ></v-img>
          </v-col>

          <v-col
            cols = 1
            >
            <a href = 'https://www.kuaishou.com/'>
              <v-img 
                height = "30px"
                src = '@/assets/kuaishou.png'
                contain
                class = 'ma-0'
                ></v-img>
            </a>
          </v-col>

          <v-col
            cols = 1
            >
            <a href = 'https://www.xuetangx.com'>
              <v-img 
                height = "50px"
                src = '@/assets/xuetang.png'
                contain
                class = 'ma-0'
                ></v-img>
            </a>
          </v-col>

        </v-row>
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn 
        text
        @click = 'openRegisterDialog'
        v-if = '!isLoggedIn()'
        class = 'white--text'
        >
        <span>Sign up</span>
      </v-btn>

      <v-btn 
        text
        @click = 'openLoginDialog'
        v-if = '!isLoggedIn()'
        class = 'white--text'
        >
        <span class = 'font-weight-bold'>Login</span>

      </v-btn>

      <v-btn
        text
        @click = 'logout'
        v-if = 'isLoggedIn()'
        class = 'white--text'
        >
        Logout
      </v-btn>


    </v-app-bar>

    <!-- Sidebar -->

    <v-navigation-drawer
      app
      v-model = 'showSidebar'
      width = '400px'
      >

      <v-card flat tile>
        <v-img 
          src = '@/assets/banner.png'
          class = "white--text align-end"
          gradient = "to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
          >
          <v-card-title v-text = 'sidebarTitle'></v-card-title>
        </v-img>
      </v-card>

      <v-list
        nav
        >

        <v-list-item link v-for = 'link in links' :key = 'link.text' @click = '$router.push(link.route)'>
          <v-list-item-icon>
            <v-icon v-text = 'link.icon'></v-icon>
          </v-list-item-icon>
          <v-list-item-title>{{link.text}}</v-list-item-title>
        </v-list-item>
      </v-list>

    </v-navigation-drawer>

    <LoginDialog />
    <RegisterDialog />

  </nav>
</template>

<script>
import LoginDialog from '@/components/LoginDialog';
import RegisterDialog from '@/components/RegisterDialog';
import { mapGetters, mapActions, mapState } from 'vuex';

export default {
  name: 'Navbar',
  components: {
    LoginDialog,
    RegisterDialog,
  },
  data() {
    return {
      showSidebar: false,
      links: [
        {
          text: '公告栏',
          route: '/',
          icon: 'mdi-view-dashboard',
        },
        {
          text: '报名条款',
          route: '/agreement',
          icon: 'mdi-information',
        }
      ]
    }
  },
  methods: {
    openLoginDialog() {
      this.$store.commit('setStatus', 'loggingIn');
    },
    openRegisterDialog() {
      this.$store.commit('setStatus', 'registering');
    },
    ...mapGetters(['isLoggedIn']),
    ...mapActions(['logout']),
  },
  computed: {
    ...mapState(['user']),
    sidebarTitle() {
      if (this.user) 
        return this.user.teamname;
      return "Not logged in";
    }
  },
  watch: {
    user() {
      if (this.$store.state.user && !this.links.find( link => link.text == 'Profile' )) {
        this.links.push({
          text: 'Profile',
          route: '/profile',
          icon: 'mdi-information',
        });
      }
    }
  }
}
</script>

<style scoped>
.bottom-gradient {
  background-image: linear-gradient(to top, rgba(0, 0, 0, 0.4) 0%, transparent 100px);
}
</style>
