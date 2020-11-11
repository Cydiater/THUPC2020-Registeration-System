import Vue from 'vue';

export default {
  notify(state, { type, message }) {
    state.notification.show = true;
    state.notification.type = type;
    state.notification.message = message;
  },
  toggleNotification(state, value) {
    state.notification.show = value;
  },
  setStatus(state, status) {
    Vue.set(state.status, status, true);
  },
  setToken(state, token) {
    state.token = token;
  },
  clearStatus(state, status) {
    Vue.delete(state.status, status);
  },
  setUser(state, user) {
    state.user = user;
  }
};
