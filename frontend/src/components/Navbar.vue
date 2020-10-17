<template>
  <nav>

    <!-- Top Bar -->

    <v-app-bar
      class = 'pink darken-3 pink--text text--lighten-5'
      dense
      app
      >

      <v-app-bar-nav-icon @click = "showSidebar = !showSidebar" class = 'pink--text text--lighten-5'></v-app-bar-nav-icon>
      <v-toolbar-title>THUPC2020 Registeration System</v-toolbar-title>

    </v-app-bar>

    <!-- Sidebar -->

    <v-navigation-drawer
      app
      v-model = 'showSidebar'
      width = '400px'
      >

      <v-card flat tile>
        <v-img 
          src = '@/assets/sideimg.jpg'
          class="white--text align-end"
          gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
          >
          <v-card-title v-text = 'sidebarTitle'></v-card-title>
        </v-img>
      </v-card>

      <v-list
        nav
        >

        <v-list-item link v-for = 'link in links' :key = 'link.text'>
          <v-list-item-icon>
            <v-icon v-text = 'link.icon'></v-icon>
          </v-list-item-icon>
          <v-list-item-title>{{link.text}}</v-list-item-title>
        </v-list-item>
      </v-list>

    </v-navigation-drawer>

  </nav>
</template>

<script>
export default {
  name: 'Navbar',
  data() {
    return {
      showSidebar: false,
      sidebarTitle: 'Not logged in',
      links: [
        {
          text: 'Dashboard',
          route: '/',
          icon: 'mdi-view-dashboard',
        },
      ]
    }
  }
}
</script>

<style scoped>
.bottom-gradient {
  background-image: linear-gradient(to top, rgba(0, 0, 0, 0.4) 0%, transparent 100px);
}
</style>
