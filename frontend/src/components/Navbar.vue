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
      >
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
