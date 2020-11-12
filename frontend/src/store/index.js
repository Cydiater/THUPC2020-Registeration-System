import Vuex from 'vuex';
import Vue from 'vue';

Vue.use(Vuex);

import actions from './actions';
import mutations from './mutations';
import getters from './getters';

const state = {
  status: {},
  token: localStorage.getItem('token'),
  notification: {
    show: false,
    type: null,
    message: null,
  },
  username: localStorage.getItem('username'),
  user: null,
  announcements: [],
  currentAnnouncement: null,
};

const store = new Vuex.Store({
  state,
  actions,
  mutations,
  getters,
});

export default store;
