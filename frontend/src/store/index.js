import Vuex from 'vuex';
import Vue from 'vue';

Vue.use(Vuex);

import actions from './actions';
import mutations from './mutations';

const state = {
  status: {},
  token: null,
  notification: {
    show: false,
    type: null,
    message: null,
  }
};

const store = new Vuex.Store({
  state,
  actions,
  mutations,
});

export default store;
